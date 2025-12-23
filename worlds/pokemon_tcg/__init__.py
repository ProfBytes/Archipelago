import os

import Options
import settings
import typing
import threading
import base64
import random
from copy import deepcopy
from typing import TextIO

from Utils import __version__
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, LocationProgressType
from Fill import fill_restrictive, FillError, sweep_from_pool
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_item_rule
from .items import item_table, item_groups
from .locations import location_data, PokemonTCGLocation
from .regions import create_regions
from .options import PokemonTCGOptions
from .rom_addresses import rom_addresses
from .text import encode_text
from .rom import generate_output, PokemonTCGProcedurePatch
from .rules import set_rules
from . import logic
from . import client
from .data import card_list, colorless_pokemon, primary, secondary, tertiary, starting_deck_trainers, eevee_deck


class PokemonSettings(settings.Group):
    class TCGRomFile(settings.UserFilePath):
        """File names of the Pokemon TCG rom"""
        description = "Pokemon Trading Card Game ROM File"
        copy_to = "Pokemon Trading Card Game.gbc"
        md5s = [PokemonTCGProcedurePatch.hash]

    rom_file: TCGRomFile = TCGRomFile(TCGRomFile.copy_to)


class PokemonWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pokémon TCG with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["PrimePentad", "ProfBytes"]
    )

    tutorials = [setup_en]


class PokemonTCGWorld(World):
    """"""
    game = "Pokemon TCG"

    options_dataclass = PokemonTCGOptions
    options: PokemonTCGOptions

    settings: typing.ClassVar[PokemonSettings]

    required_client_version = (0, 6, 4)

    topology_present = True

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {location.name: location.address for location in location_data if location.type == "Item"
                           and location.address is not None}
    item_name_groups = item_groups

    web = PokemonWebWorld()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.item_pool = []
        self.local_locs = []
        self.water_club_trade = None
        self.grass_club_trade = None
        self.fighting_club_trade = None
        self.ishihara_1_trade = None
        self.ishihara_2_trade = None
        self.ishihara_3_trade = None
        self.lightning_club_trade = None
        self.fire_club_trade = None
        self.psychic_club_trade = None

        self.water_club_door = None
        self.fire_club_door = None
        self.lightning_club_door = None
        self.science_club_door = None
        self.psychic_club_door = None
        self.grass_club_door = None
        self.rock_club_door = None
        self.fighting_club_door = None

        self.psychic_medal_count = 4
        self.fire_card_count = 650
        self.goal_medal_count = 8
        self.doors_open = 0

        self.starting_deck_type_1 = "Fire"
        self.starting_deck_type_2 = "Water"
        self.starting_deck_type_3 = "Grass"

        self.pack_type = "Evoline"
        self.trade_rando = "vanilla"

    def generate_early(self): # Set the starting deck types here if there's overlap
        # Use self.random for consistency
        valid_cards = card_list
# if the player chooses fire, lightning, water, have a chance to have an Eevee deck
        starter_deck = {}
        if self.options.special_deck == "Prof Special":
            starter_deck = eevee_deck
            self.starting_deck_type_1 = options.StartingDeck1.option_fire
            self.starting_deck_type_2 = options.StartingDeck1.option_water
            self.starting_deck_type_3 = options.StartingDeck1.option_lightning
        else:
            while self.starting_deck_type_2 == self.starting_deck_type_1:
                self.starting_deck_type_2 = options.StartingDeck2[self.random.sample(0, 5)]
            while self.starting_deck_type_3 == self.starting_deck_type_2 or self.starting_deck_type_3 == self.starting_deck_type_1:
                self.starting_deck_type_3 = options.StartingDeck3[self.random.sample(0, 5)]
            starter_deck.update(self.random.choice(primary[self.options.starting_deck_1.current_option_name]))
            starter_deck.update(self.random.choice(secondary[self.options.starting_deck_2.current_option_name]))
            starter_deck.update(self.random.choice(tertiary[self.options.starting_deck_3.current_option_name]))
            starter_deck.update(self.random.choice(colorless_pokemon))
            trainers = {}
            while len(trainers) < 3:
                trainers.update({self.random.choice(starting_deck_trainers): 3})
            starter_deck.update(trainers)

        for key in starter_deck.keys():
            if key in valid_cards:
                valid_cards.remove(key)
        self.options.starter_deck = Options.OptionDict(starter_deck)

        doors_to_generate = 0
        open_doors_to_gen = self.options.open_doors
        item_list = []
        item_list.extend(valid_cards)
        item_list.extend(items.medals)
        item_list.append("Nothing")

        if not self.options.water_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.water_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.water_club_unlock.value = "Fire Energy"
        if not self.options.grass_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.grass_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.grass_club_unlock.value = "Fire Energy"
        if not self.options.fire_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.fire_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.fire_club_unlock.value = "Fire Energy"
        if not self.options.lightning_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.lightning_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.lightning_club_unlock.value = "Fire Energy"
        if not self.options.rock_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.rock_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.rock_club_unlock.value = "Fire Energy"
        if not self.options.science_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.science_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.science_club_unlock.value = "Fire Energy"
        if not self.options.psychic_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.psychic_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.psychic_club_unlock.value = "Fire Energy"
        if not self.options.fighting_club_unlock.value in item_list:
            doors_to_generate += 1
        if self.options.fighting_club_unlock.value == "Nothing":
            open_doors_to_gen -= 1
            self.options.fighting_club_unlock.value = "Fire Energy"

        doors = []
        while len(doors) < doors_to_generate:
            if open_doors_to_gen > 0:
                doors.append("Fire Energy")
                open_doors_to_gen -= 1
            else:
                if self.random.choice(range(0, 9)) < 2:
                    doors.append(self.random.choice(items.medals))
                else:
                    doors.append((self.random.choice(valid_cards)))

        while len(doors) < 8:
            doors.append("Fire Energy")

        self.random.shuffle(doors)
        if not self.options.water_club_unlock.value in item_list:
            self.options.water_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.grass_club_unlock.value in item_list:
            self.options.grass_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.fire_club_unlock.value in item_list:
            self.options.fire_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.lightning_club_unlock.value in item_list:
            self.options.lightning_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.rock_club_unlock.value in item_list:
            self.options.rock_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.science_club_unlock.value in item_list:
            self.options.science_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.psychic_club_unlock.value in item_list:
            self.options.psychic_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])
        if not self.options.fighting_club_unlock.value in item_list:
            self.options.fighting_club_unlock = Options.FreeText(doors[0])
            doors.remove(doors[0])

        # def encode_name(name, t):
        #     try:
        #         if len(encode_text(name)) > 7:
        #             raise IndexError(f"{t} name too long for player {self.multiworld.player_name[self.player]}. Must be 7 characters or fewer.")
        #         return encode_text(name, length=8, whitespace="@", safety=True)
        #     except KeyError as e:
        #         raise KeyError(f"Invalid character(s) in {t} name for player {self.multiworld.player_name[self.player]}") from e
        # if self.options.trainer_name == "choose_in_game":
        #     self.trainer_name = "choose_in_game"
        # else:
        #     self.trainer_name = encode_name(self.options.trainer_name.value, "Player")
        # if self.options.rival_name == "choose_in_game":
        #     self.rival_name = "choose_in_game"
        # else:
        #     self.rival_name = encode_name(self.options.rival_name.value, "Rival")

        #if not self.options.medal_sanity:
        #    self.options.non_local_items.value -= self.item_name_groups["Medals"]

    def create_items(self):
        self.multiworld.itempool += self.item_pool

    # @classmethod
    # def stage_fill_hook(cls, multiworld, progitempool, usefulitempool, filleritempool, fill_locations):
    #     locs = []
    #     for world in multiworld.get_game_worlds("Pokemon TCG"):
    #         locs += world.local_locs
    #     for loc in sorted(locs):
    #         if loc.item:
    #             continue
    #         itempool = progitempool + usefulitempool + filleritempool
    #         multiworld.random.shuffle(itempool)
    #         unplaced_items = []
    #         for i, item in enumerate(itempool):
    #             if ((item.player == loc.player or (item.player in multiworld.groups
    #                                                and loc.player in multiworld.groups[item.player]["players"]))
    #                     and loc.can_fill(multiworld.state, item, False)):
    #                 if item.advancement:
    #                     pool = progitempool
    #                 elif item.useful:
    #                     pool = usefulitempool
    #                 else:
    #                     pool = filleritempool
    #                 for i, check_item in enumerate(pool):
    #                     if item is check_item:
    #                         pool.pop(i)
    #                         break
    #                 if item.advancement:
    #                     state = sweep_from_pool(multiworld.state, progitempool + unplaced_items)
    #                 if (not item.advancement) or state.can_reach(loc, "Location", loc.player):
    #                     multiworld.push_item(loc, item, False)
    #                     fill_locations.remove(loc)
    #                     break
    #                 else:
    #                     unplaced_items.append(item)
    #         progitempool += [item for item in unplaced_items if item.advancement]
    #         usefulitempool += [item for item in unplaced_items if item.useful]
    #         filleritempool += [item for item in unplaced_items if (not item.advancement) and (not item.useful)]

    #def fill_hook(self, progitempool, usefulitempool, filleritempool, fill_locations):
        # if not self.options.badgesanity:
        #     # Door Shuffle options besides Simple place badges during door shuffling
        #     if self.options.door_shuffle in ("off", "simple"):
        #         badges = [item for item in progitempool if "Badge" in item.name and item.player == self.player]
        #         for badge in badges:
        #             self.multiworld.itempool.remove(badge)
        #             progitempool.remove(badge)
        #         for attempt in range(6):
        #             badgelocs = [
        #                 self.multiworld.get_location(loc, self.player) for loc in [
        #                     "Pewter Gym - Brock Prize", "Cerulean Gym - Misty Prize",
        #                     "Vermilion Gym - Lt. Surge Prize", "Celadon Gym - Erika Prize",
        #                     "Fuchsia Gym - Koga Prize", "Saffron Gym - Sabrina Prize",
        #                     "Cinnabar Gym - Blaine Prize", "Viridian Gym - Giovanni Prize"
        #                 ] if self.multiworld.get_location(loc, self.player).item is None]
        #             state = self.multiworld.get_all_state(False, True, False)
        #             # Give it two tries to place badges with wild Pokemon and learnsets as-is.
        #             # If it can't, then try with all Pokemon collected, and we'll try to fix HM move availability after.
        #             if attempt > 1:
        #                 for mon in poke_data.pokemon_data.keys():
        #                     state.collect(self.create_item(mon), True)
        #             state.sweep_for_advancements()
        #             self.random.shuffle(badges)
        #             self.random.shuffle(badgelocs)
        #             badgelocs_copy = badgelocs.copy()
        #             # allow_partial so that unplaced badges aren't lost, for debugging purposes
        #             fill_restrictive(self.multiworld, state, badgelocs_copy, badges, True, True, allow_partial=True)
        #             if len(badges) > 8 - len(badgelocs):
        #                 for location in badgelocs:
        #                     if location.item:
        #                         badges.append(location.item)
        #                         location.item = None
        #                 continue
        #             else:
        #                 for location in badgelocs:
        #                     if location.item:
        #                         fill_locations.remove(location)
        #                 progitempool += badges
        #                 break
        #         else:
        #             raise FillError(f"Failed to place badges for player {self.player}")
        #     verify_hm_moves(self.multiworld, self, self.player)
        #
        # if self.options.key_items_only:
        #     return
        #
        # tms = [item for item in usefulitempool + filleritempool if item.name.startswith("TM") and (item.player ==
        #        self.player or (item.player in self.multiworld.groups and self.player in
        #                        self.multiworld.groups[item.player]["players"]))]
        # if len(tms) > 7:
        #     for gym_leader in (("Pewter Gym", "Brock"), ("Cerulean Gym", "Misty"), ("Vermilion Gym", "Lt. Surge"),
        #                        ("Celadon Gym-C", "Erika"), ("Fuchsia Gym", "Koga"), ("Saffron Gym-C", "Sabrina"),
        #                        ("Cinnabar Gym", "Blaine"), ("Viridian Gym", "Giovanni")):
        #         loc = self.multiworld.get_location(f"{gym_leader[0].split('-')[0]} - {gym_leader[1]} TM",
        #                                            self.player)
        #         if loc.item:
        #             continue
        #         for party in self.multiworld.get_location(gym_leader[0] + " - Trainer Parties", self.player).party_data:
        #             if party["party_address"] == \
        #                     f"Trainer_Party_{gym_leader[1].replace('. ', '').replace('Giovanni', 'Viridian_Gym_Giovanni')}_A":
        #                 mon = party["party"][-1]
        #                 learnable_tms = [tm for tm in tms if self.local_poke_data[mon]["tms"][
        #                     int((int(tm.name[2:4]) - 1) / 8)] & 1 << ((int(tm.name[2:4]) - 1) % 8)]
        #                 if not learnable_tms:
        #                     learnable_tms = tms
        #                 tm = self.random.choice(learnable_tms)
        #
        #                 loc.place_locked_item(tm)
        #                 fill_locations.remove(loc)
        #                 tms.remove(tm)
        #                 if tm.useful:
        #                     usefulitempool.remove(tm)
        #                 else:
        #                     filleritempool.remove(tm)
        #                 break
        #         else:
        #             raise Exception("Missing Gym Leader data")

    # def pre_fill(self) -> None:
    #     process_pokemon_locations(self)
    #     process_trainer_data(self)
    #     locs = [location.name for location in location_data if location.type != "Item"]
    #     for location in self.multiworld.get_locations(self.player):
    #         if location.name in locs:
    #             location.show_in_spoiler = False
    #     verify_hm_moves(self.multiworld, self, self.player)
    #
    #     # Delete evolution events for Pokémon that are not in logic in an all_state so that accessibility check does not
    #     # fail. Re-use test_state from previous final loop.
    #     all_state = self.multiworld.get_all_state(False, True, False)
    #     evolutions_region = self.multiworld.get_region("Evolution", self.player)
    #     for location in evolutions_region.locations.copy():
    #         if not all_state.can_reach(location, player=self.player):
    #             evolutions_region.locations.remove(location)
    #
    #     if self.options.old_man == "early_parcel":
    #         self.multiworld.local_early_items[self.player]["Oak's Parcel"] = 1
    #         if self.options.dexsanity:
    #             for i, mon in enumerate(poke_data.pokemon_data):
    #                 if self.dexsanity_table[i]:
    #                     location = self.multiworld.get_location(f"Pokedex - {mon}", self.player)
    #                     add_item_rule(location, lambda item: item.name != "Oak's Parcel" or item.player != self.player)
    #
    #     # Place local items in some locations to prevent save-scumming. Also Oak's PC to prevent an "AP Item" from
    #     # entering the player's inventory.
    #
    #     locs = {self.multiworld.get_location("Fossil - Choice A", self.player),
    #             self.multiworld.get_location("Fossil - Choice B", self.player)}
    #
    #     if not self.options.key_items_only:
    #         rule = None
    #         if self.options.fossil_check_item_types == "key_items":
    #             rule = lambda i: i.advancement
    #         elif self.options.fossil_check_item_types == "unique_items":
    #             rule = lambda i: i.name in item_groups["Unique"]
    #         elif self.options.fossil_check_item_types == "no_key_items":
    #             rule = lambda i: not i.advancement
    #         if rule:
    #             for loc in locs:
    #                 add_item_rule(loc, rule)
    #
    #     for mon in ([" ".join(self.multiworld.get_location(
    #             f"Oak's Lab - Starter {i}", self.player).item.name.split(" ")[1:]) for i in range(1, 4)]
    #             + [" ".join(self.multiworld.get_location(
    #             f"Saffron Fighting Dojo - Gift {i}", self.player).item.name.split(" ")[1:]) for i in range(1, 3)]
    #             + ["Vaporeon", "Jolteon", "Flareon"]):
    #         if self.dexsanity_table[poke_data.pokemon_dex[mon] - 1]:
    #             loc = self.multiworld.get_location(f"Pokedex - {mon}", self.player)
    #             if loc.item is None:
    #                 locs.add(loc)
    #
    #     for loc in sorted(locs):
    #         if loc.name in self.options.priority_locations.value:
    #             add_item_rule(loc, lambda i: i.advancement)
    #         add_item_rule(loc, lambda i: i.player == self.player
    #                                      or (i.player in self.multiworld.groups
    #                                          and self.player in self.multiworld.groups[i.player]["players"]))
    #         if self.options.old_man == "early_parcel" and loc.name != "Player's House 2F - Player's PC":
    #             add_item_rule(loc, lambda i: i.name != "Oak's Parcel")
    #
    #     self.local_locs = locs
    #
    #     all_state = self.multiworld.get_all_state(False, True, False)
    #
    #     reachable_mons = set()
    #     for mon in poke_data.pokemon_data:
    #         if all_state.has(mon, self.player) or all_state.has(f"Static {mon}", self.player):
    #             reachable_mons.add(mon)
    #
    #     # The large number of wild Pokemon can make sweeping for events time-consuming, and is especially bad in
    #     # the spoiler playthrough calculation because it removes each advancement item one at a time to verify
    #     # if the game is beatable without it. We go through each zone and flag any duplicates as useful.
    #     # Especially with area 1-to-1 mapping / vanilla wild Pokémon, this should cut down significantly on wasted time.
    #     for region in self.multiworld.get_regions(self.player):
    #         region_mons = set()
    #         for location in region.locations:
    #             if "Wild Pokemon" in location.name:
    #                 if location.item.name in region_mons:
    #                     location.item.classification = ItemClassification.useful
    #                 else:
    #                     region_mons.add(location.item.name)
    #
    #     self.options.elite_four_pokedex_condition.total = \
    #         int((len(reachable_mons) / 100) * self.options.elite_four_pokedex_condition.value)
    #
    #     if self.options.accessibility == "full":
    #         balls = [self.create_item(ball) for ball in ["Poke Ball", "Great Ball", "Ultra Ball"]]
    #         traps = [self.create_item(trap) for trap in item_groups["Traps"]]
    #         locations = [location for location in self.multiworld.get_locations(self.player) if "Pokedex - " in
    #                      location.name]
    #         pokedex = self.multiworld.get_region("Pokedex", self.player)
    #         remove_items = 0
    #
    #         for location in locations:
    #             if not location.can_reach(all_state):
    #                 pokedex.locations.remove(location)
    #                 if location in self.local_locs:
    #                     self.local_locs.remove(location)
    #                 self.dexsanity_table[poke_data.pokemon_dex[location.name.split(" - ")[1]] - 1] = False
    #                 remove_items += 1
    #
    #         for _ in range(remove_items):
    #             balls.append(balls.pop(0))
    #             for ball in balls:
    #                 try:
    #                     self.multiworld.itempool.remove(ball)
    #                 except ValueError:
    #                     continue
    #                 else:
    #                     break
    #             else:
    #                 self.random.shuffle(traps)
    #                 for trap in traps:
    #                     try:
    #                         self.multiworld.itempool.remove(trap)
    #                     except ValueError:
    #                         continue
    #                     else:
    #                         break
    #                 else:
    #                     raise Exception("Failed to remove corresponding item while deleting unreachable Dexsanity location")
    #
    #     if not self.options.key_items_only:
    #         loc = self.multiworld.get_location("Player's House 2F - Player's PC", self.player)
    #         # Absolutely cannot have another player's item
    #         if loc.item is not None and loc.item.player != self.player:
    #             self.multiworld.itempool.append(loc.item)
    #             loc.item = None
    #         loc.place_locked_item(self.pc_item)
    #
    # def get_pre_fill_items(self) -> typing.List["Item"]:
    #     pool = [self.create_item(mon) for mon in poke_data.pokemon_data]
    #     pool.append(self.pc_item)
    #     return pool
    #
    # @classmethod
    # def stage_post_fill(cls, multiworld):
    #     # Convert all but one of each instance of a wild Pokemon to useful classification.
    #     # This cuts down on time spent calculating the spoiler playthrough.
    #     found_mons = set()
    #     for sphere in multiworld.get_spheres():
    #         mon_locations_in_sphere = {}
    #         for location in sphere:
    #             if (location.game == location.item.game == "Pokemon TCG"
    #                     and (location.item.name in poke_data.pokemon_data.keys() or "Static " in location.item.name)
    #                     and location.item.advancement):
    #                 key = (location.player, location.item.name)
    #                 if key in found_mons:
    #                     location.item.classification = ItemClassification.useful
    #                 else:
    #                     mon_locations_in_sphere.setdefault(key, []).append(location)
    #         for key, mon_locations in mon_locations_in_sphere.items():
    #             found_mons.add(key)
    #             if len(mon_locations) > 1:
    #                 # Sort for deterministic results.
    #                 mon_locations.sort()
    #                 # Convert all but the first to useful classification.
    #                 for location in mon_locations[1:]:
    #                     location.item.classification = ItemClassification.useful

    def create_regions(self):
        create_regions(self)
    #     if (self.options.old_man == "vanilla" or
    #             self.options.door_shuffle in ("full", "insanity")):
    #         fly_map_codes = self.random.sample(range(2, 11), 2)
    #     elif (self.options.door_shuffle == "simple" or
    #             self.options.route_3_condition == "boulder_badge" or
    #           (self.options.route_3_condition == "any_badge" and
    #            self.options.badgesanity)):
    #         fly_map_codes = self.random.sample(range(3, 11), 2)
    #
    #     else:
    #         fly_map_codes = self.random.sample([4, 6, 7, 8, 9, 10], 2)
    #     if self.options.free_fly_location:
    #         fly_map_code = fly_map_codes[0]
    #     else:
    #         fly_map_code = 0
    #     if self.options.town_map_fly_location:
    #         town_map_fly_map_code = fly_map_codes[1]
    #     else:
    #         town_map_fly_map_code = 0
    #     fly_maps = ["Pallet Town", "Viridian City", "Pewter City", "Cerulean City", "Lavender Town",
    #                 "Vermilion City", "Celadon City", "Fuchsia City", "Cinnabar Island", "Indigo Plateau",
    #                 "Saffron City"]
    #     self.fly_map = fly_maps[fly_map_code]
    #     self.town_map_fly_map = fly_maps[town_map_fly_map_code]
    #     self.fly_map_code = fly_map_code
    #     self.town_map_fly_map_code = town_map_fly_map_code
    #
    #     self.multiworld.completion_condition[self.player] = lambda state, player=self.player: state.has("Become Champion", player=player)

    def set_rules(self):
        set_rules(self.multiworld, self, self.player)

    def create_item(self, name: str) -> Item:
        return PokemonTCGItem(name, self.player)

    def generate_output(self, output_directory: str):
        generate_output(self, output_directory)

    #def modify_multidata(self, multidata: dict):
        # rom_name = bytearray(f'AP{__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0',
        #                      'utf8')[:21]
        # rom_name.extend([0] * (21 - len(rom_name)))
        # new_name = base64.b64encode(bytes(rom_name)).decode()
        # multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    #def write_spoiler_header(self, spoiler_handle: TextIO):
        # spoiler_handle.write(f"Cerulean Cave Total Key Items:   {self.options.cerulean_cave_key_items_condition.total}\n")
        # spoiler_handle.write(f"Elite Four Total Key Items:      {self.options.elite_four_key_items_condition.total}\n")
        # spoiler_handle.write(f"Elite Four Total Pokemon:        {self.options.elite_four_pokedex_condition.total}\n")
        # if self.options.free_fly_location:
        #     spoiler_handle.write(f"Free Fly Location:               {self.fly_map}\n")
        # if self.options.town_map_fly_location:
        #     spoiler_handle.write(f"Town Map Fly Location:           {self.town_map_fly_map}\n")
        # if self.extra_badges:
        #     for hm_move, badge in self.extra_badges.items():
        #         spoiler_handle.write(hm_move + " enabled by: " + (" " * 20)[:20 - len(hm_move)] + badge + "\n")

    #def write_spoiler(self, spoiler_handle):
        # if self.options.randomize_type_chart:
        #     spoiler_handle.write(f"\n\nType matchups ({self.multiworld.player_name[self.player]}):\n\n")
        #     for matchup in self.type_chart:
        #         spoiler_handle.write(f"{matchup[0]} deals {matchup[2] * 10}% damage to {matchup[1]}\n")
        # spoiler_handle.write(f"\n\nPokémon locations ({self.multiworld.player_name[self.player]}):\n\n")
        # pokemon_locs = [location.name for location in location_data if location.type not in ("Item", "Trainer Parties")]
        # for location in self.multiworld.get_locations(self.player):
        #     if location.name in pokemon_locs:
        #         spoiler_handle.write(location.name + ": " + location.item.name + "\n")

    def get_filler_item_name(self) -> str:
        return item_table["Energy Pack"]

    #def extend_hint_information(self, hint_data):
        # if self.options.dexsanity or self.options.door_shuffle:
        #     hint_data[self.player] = {}
        # if self.options.dexsanity:
        #     mon_locations = {mon: set() for mon in poke_data.pokemon_data.keys()}
        #     for loc in location_data:
        #         if loc.type in ["Wild Encounter", "Static Pokemon", "Legendary Pokemon", "Missable Pokemon"]:
        #             mon = self.multiworld.get_location(loc.name, self.player).item.name
        #             if mon.startswith("Static ") or mon.startswith("Missable "):
        #                 mon = " ".join(mon.split(" ")[1:])
        #             mon_locations[mon].add(loc.name.split(" -")[0])
        #     for i, mon in enumerate(mon_locations):
        #         if self.dexsanity_table[i] and mon_locations[mon]:
        #             hint_data[self.player][self.multiworld.get_location(f"Pokedex - {mon}", self.player).address] =\
        #                 ", ".join(mon_locations[mon])
        #
        # if self.options.door_shuffle:
        #     for location in self.multiworld.get_locations(self.player):
        #         if location.parent_region.entrance_hint and location.address:
        #             hint_data[self.player][location.address] = location.parent_region.entrance_hint

    # def fill_slot_data(self) -> dict: # save door details here
    #     ret = {
    #         "second_fossil_check_condition": self.options.second_fossil_check_condition.value,
    #         "require_item_finder": self.options.require_item_finder.value,
    #         "randomize_hidden_items": self.options.randomize_hidden_items.value,
    #         "badges_needed_for_hm_moves": self.options.badges_needed_for_hm_moves.value,
    #         "oaks_aide_rt_2": self.options.oaks_aide_rt_2.value,
    #         "oaks_aide_rt_11": self.options.oaks_aide_rt_11.value,
    #         "oaks_aide_rt_15": self.options.oaks_aide_rt_15.value,
    #         "extra_key_items": self.options.extra_key_items.value,
    #         "extra_strength_boulders": self.options.extra_strength_boulders.value,
    #         "tea": self.options.tea.value,
    #         "old_man": self.options.old_man.value,
    #         "elite_four_badges_condition": self.options.elite_four_badges_condition.value,
    #         "elite_four_key_items_condition": self.options.elite_four_key_items_condition.total,
    #         "elite_four_pokedex_condition": self.options.elite_four_pokedex_condition.total,
    #         "victory_road_condition": self.options.victory_road_condition.value,
    #         "route_22_gate_condition": self.options.route_22_gate_condition.value,
    #         "route_3_condition": self.options.route_3_condition.value,
    #         "robbed_house_officer": self.options.robbed_house_officer.value,
    #         "viridian_gym_condition": self.options.viridian_gym_condition.value,
    #         "cerulean_cave_badges_condition": self.options.cerulean_cave_badges_condition.value,
    #         "cerulean_cave_key_items_condition": self.options.cerulean_cave_key_items_condition.total,
    #         "free_fly_map": self.fly_map_code,
    #         "town_map_fly_map": self.town_map_fly_map_code,
    #         "extra_badges": self.extra_badges,
    #         "randomize_pokedex": self.options.randomize_pokedex.value,
    #         "trainersanity": self.options.trainersanity.value,
    #         "death_link": self.options.death_link.value,
    #         "prizesanity": self.options.prizesanity.value,
    #         "key_items_only": self.options.key_items_only.value,
    #         "poke_doll_skip": self.options.poke_doll_skip.value,
    #         "bicycle_gate_skips": self.options.bicycle_gate_skips.value,
    #         "stonesanity": self.options.stonesanity.value,
    #         "door_shuffle": self.options.door_shuffle.value,
    #         "warp_tile_shuffle": self.options.warp_tile_shuffle.value,
    #         "dark_rock_tunnel_logic": self.options.dark_rock_tunnel_logic.value,
    #         "split_card_key": self.options.split_card_key.value,
    #         "all_elevators_locked": self.options.all_elevators_locked.value,
    #         "require_pokedex": self.options.require_pokedex.value,
    #         "area_1_to_1_mapping": self.options.area_1_to_1_mapping.value,
    #         "blind_trainers": self.options.blind_trainers.value,
    #         "v5_update": True,
    #
    #     }
    #     if self.options.type_chart_seed == "random" or self.options.type_chart_seed.value.isdigit():
    #         ret["type_chart"] = self.type_chart
    #
    #     return ret

class PokemonTCGItem(Item):
    game = "Pokemon TCG"
    type = None

    def __init__(self, name: str, player: int = None):
        item_data = item_table[name]
        super(PokemonTCGItem, self).__init__(
            name,
            item_data.classification,
            item_data.id, player
        )
