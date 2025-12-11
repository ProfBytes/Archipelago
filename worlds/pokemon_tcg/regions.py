from copy import deepcopy
from BaseClasses import MultiWorld, Region, Entrance, LocationProgressType, ItemClassification
from .items import item_table, item_groups
from .locations import location_data, PokemonTCGLocation
from . import logic
from . import poke_data

map_ids = {
    "Overworld": 0x00,
    "Mason Laboratory Center Room": 0x00,
    "Mason Laboratory Right Room": 0x00,
    "Ishihara's House": 0x00,
    "Water Club Lobby": 0x00,
    "Water Club Lounge": 0x00,
    "Water Club Main Hall": 0x00,
    "Fire Club Lobby": 0x00,
    "Fire Club Lounge": 0x00,
    "Fire Club Main Hall": 0x00,
    "Lightning Club Lobby": 0x00,
    "Lightning Club Lounge": 0x00,
    "Lightning Club Main Hall": 0x00,
    "Grass Club Lobby": 0x00,
    "Grass Club Lounge": 0x00,
    "Grass Club Main Hall": 0x00,
    "Rock Club Lobby": 0x00,
    "Rock Club Lounge": 0x00,
    "Rock Club Main Hall": 0x00,
    "Fighting Club Lobby": 0x00,
    "Fighting Club Lounge": 0x00,
    "Fighting Club Main Hall": 0x00,
    "Psychic Club Lobby": 0x00,
    "Psychic Club Lounge": 0x00,
    "Psychic Club Main Hall": 0x00,
    "Science Club Lobby": 0x00,
    "Science Club Lounge": 0x00,
    "Science Club Main Hall": 0x00,
    "Challenge Hall Lobby": 0x00,
    "Challenge Hall Lounge": 0x00,
    "Challenge Hall Main Hall": 0x00,
    "Pokemon Dome Lobby": 0x00,
    "Pokemon Dome Main Hall": 0x00,
    "Pokemon Dome Hall of Honor": 0x00,

def pair(a, b):
    return f"{a} to {b}", f"{b} to {a}"


mandatory_connections = {
    pair("Challenge Hall Lobby", "Challenge Hall Lounge"),
    pair("Challenge Hall Lounge", "Challenge Hall Main Hall"),
}


def create_region(multiworld: MultiWorld, player: int, name: str, locations_per_region=None, exits=None):
    ret = PokemonTCGRegion(name, player, multiworld)
    for location in locations_per_region.get(name, []):
        location.parent_region = ret
        ret.locations.append(location)
        if multiworld.worlds[player].options.randomize_hidden_items == "exclude" and "Hidden" in location.name:
            location.progress_type = LocationProgressType.EXCLUDED
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))
    locations_per_region[name] = []
    return ret

def create_regions(world):
    multiworld = world.multiworld
    player = world.player
    locations_per_region = {}

    start_inventory = world.options.start_inventory.value.copy()


    for location in location_data:
        locations_per_region.setdefault(location.region, [])
        # The check for list is so that we don't try to check the item table with a list as a key
        if location.inclusion(world, player) and isinstance(location.original_item, list):
            location_object = PokemonTCGLocation(player, location.name, location.address, location.rom_address,
                                                location.type, location.level, location.level_address)
            locations_per_region[location.region].append(location_object)
            if location.type in ("Item", "Trainer Parties"):
                event = location.event
                if world.options.exp_all

                if location.original_item is None:
                    item = world.create_filler()
                elif location.original_item == "Exp. All" and world.options.exp_all == "remove":
                    item = world.create_filler()
                elif location.original_item == "Pokedex":
                    if world.options.randomize_pokedex == "vanilla":
                        location_object.event = True
                        event = True
                    item = world.create_item("Pokedex")
                elif location.original_item == "Moon Stone" and world.options.stonesanity:
                    stone = stones.pop()
                    item = world.create_item(stone)
                elif location.original_item.startswith("TM"):
                    if world.options.randomize_tm_moves:
                        item = world.create_item(location.original_item.split(" ")[0])
                    else:
                        item = world.create_item(location.original_item)
                elif location.original_item == "Card Key" and world.options.split_card_key == "on":
                    item = world.create_item("Card Key 3F")
                elif "Card Key" in location.original_item and world.options.split_card_key == "progressive":
                    item = world.create_item("Progressive Card Key")
                else:
                    item = world.create_item(location.original_item)
                    if (item.classification == ItemClassification.filler and world.random.randint(1, 100)
                            <= world.options.trap_percentage.value and combined_traps != 0):
                        item = world.create_item(world.select_trap())

                if (world.options.key_items_only and (location.original_item != "Exp. All")
                        and not (location.event or item.advancement)):
                    continue

                if item.name in start_inventory and start_inventory[item.name] > 0 and \
                        location.original_item in item_groups["Unique"]:
                    start_inventory[location.original_item] -= 1
                    item = world.create_filler()

                if event:
                    location_object.place_locked_item(item)
                    if location.type == "Trainer Parties":
                        location_object.party_data = deepcopy(location.party_data)
                else:
                    world.item_pool.append(item)

    world.random.shuffle(world.item_pool)
    if not world.options.key_items_only:
        def acceptable_item(item):
            return ("Badge" not in item.name and "Trap" not in item.name and item.name != "Pokedex"
                    and "Coins" not in item.name and "Progressive" not in item.name
                    and ("Player's House 2F - Player's PC" not in world.options.exclude_locations or item.excludable)
                    and ("Player's House 2F - Player's PC" in world.options.exclude_locations or
                         "Player's House 2F - Player's PC" not in world.options.priority_locations or item.advancement))
        for i, item in enumerate(world.item_pool):
            if acceptable_item(item) and (item.name not in world.options.non_local_items.value):
                world.pc_item = world.item_pool.pop(i)
                break
        else:
            for i, item in enumerate(world.item_pool):
                if acceptable_item(item):
                    world.pc_item = world.item_pool.pop(i)
                    break


    advancement_items = [item.name for item in world.item_pool if item.advancement] \
                        + [item.name for item in world.multiworld.precollected_items[world.player] if
                           item.advancement]
    world.total_key_items = len(
        # The stonesanity items are not checked for here and instead just always added as the `+ 4`
        # They will always exist, but if stonesanity is off, then only as events.
        # We don't want to just add 4 if stonesanity is off while still putting them in this list in case
        # the player puts stones in their start inventory, in which case they would be double-counted here.
        [item for item in ["Bicycle", "Silph Scope", "Item Finder", "Super Rod", "Good Rod",
                           "Old Rod", "Lift Key", "Card Key", "Town Map", "Coin Case", "S.S. Ticket",
                           "Secret Key", "Poke Flute", "Mansion Key", "Safari Pass", "Plant Key",
                           "Hideout Key", "Card Key 2F", "Card Key 3F", "Card Key 4F", "Card Key 5F",
                           "Card Key 6F", "Card Key 7F", "Card Key 8F", "Card Key 9F", "Card Key 10F",
                           "Card Key 11F", "Exp. All", "Moon Stone", "Oak's Parcel", "Helix Fossil", "Dome Fossil",
                           "Old Amber", "Tea", "Gold Teeth", "Bike Voucher"] if item in advancement_items]) + 4
    if "Progressive Card Key" in advancement_items:
        world.total_key_items += 10

    world.options.cerulean_cave_key_items_condition.total = \
        int((world.total_key_items / 100) * world.options.cerulean_cave_key_items_condition.value)

    world.options.elite_four_key_items_condition.total = \
        int((world.total_key_items / 100) * world.options.elite_four_key_items_condition.value)

    regions = [create_region(multiworld, player, region, locations_per_region) for region in warp_data]
    multiworld.regions += regions
    if __debug__:
        for region in locations_per_region:
            assert not locations_per_region[region], f"locations not assigned to region {region}"

    connect(multiworld, player, "Menu", "Pallet Town", one_way=True)
    connect(multiworld, player, "Menu", "Pokedex", one_way=True)
    connect(multiworld, player, "Menu", "Evolution", one_way=True)
    connect(multiworld, player, "Menu", "Fossil", lambda state: logic.fossil_checks(state,
        world.options.second_fossil_check_condition.value, player), one_way=True)
    connect(multiworld, player, "Pallet Town", "Route 1")
    connect(multiworld, player, "Route 1", "Viridian City")
    connect(multiworld, player, "Viridian City", "Route 22")
    connect(multiworld, player, "Route 22", "Route 22-F", lambda state: state.has("Defeat Viridian Gym Giovanni", player), one_way=True)
    connect(multiworld, player, "Route 2-SW", "Route 2-Grass", one_way=True)
    connect(multiworld, player, "Route 2-NW", "Route 2-Grass", one_way=True)
    connect(multiworld, player, "Route 22 Gate-S", "Route 22 Gate-N",
            lambda state: logic.has_badges(state, world.options.route_22_gate_condition.value, player))
    connect(multiworld, player, "Route 23-Grass", "Route 23-C", lambda state: logic.has_badges(state, world.options.victory_road_condition.value, player))
    connect(multiworld, player, "Route 23-Grass", "Route 23-S", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Viridian City-N", "Viridian City-G", lambda state:
                     logic.has_badges(state, world.options.viridian_gym_condition.value, player))
    connect(multiworld, player, "Route 2-SW", "Route 2-SE", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Route 2-NW", "Route 2-NE", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Route 2-E", "Route 2-NE", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Route 2-SW", "Viridian City-N")
    connect(multiworld, player, "Route 2-NW", "Pewter City")
    connect(multiworld, player, "Pewter City", "Pewter City-E")
    connect(multiworld, player, "Pewter City-M", "Pewter City", one_way=True)
    connect(multiworld, player, "Pewter City", "Pewter City-M", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Pewter City-E", "Route 3", lambda state: logic.route(state, world, player), one_way=True)
    connect(multiworld, player, "Route 3", "Pewter City-E", one_way=True)
    connect(multiworld, player, "Route 4-W", "Route 3")
    connect(multiworld, player, "Route 24", "Cerulean City-Water", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Cerulean City-Water", "Route 4-Lass", lambda state: logic.can_surf(state, world, player), one_way=True)
    connect(multiworld, player, "Mt Moon B2F", "Mt Moon B2F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B2F-NE", "Mt Moon B2F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B2F-C", "Mt Moon B2F-Wild", one_way=True)
    connect(multiworld, player, "Route 4-Lass", "Route 4-C", one_way=True)
    connect(multiworld, player, "Route 4-C", "Route 4-E", one_way=True)
    connect(multiworld, player, "Route 4-E", "Cerulean City")
    connect(multiworld, player, "Cerulean City", "Route 24")
    connect(multiworld, player, "Cerulean City", "Cerulean City-T", lambda state: state.has("Help Bill", player))
    connect(multiworld, player, "Cerulean City-Outskirts", "Cerulean City", one_way=True)
    connect(multiworld, player, "Cerulean City", "Cerulean City-Outskirts", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Cerulean City-Outskirts", "Route 9", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Cerulean City-Outskirts", "Route 5")
    connect(multiworld, player, "Cerulean Cave B1F", "Cerulean Cave B1F-E", lambda state: logic.can_surf(state, world, player), one_way=True)
    connect(multiworld, player, "Route 24", "Route 25")
    connect(multiworld, player, "Route 9", "Route 10-N")
    connect(multiworld, player, "Route 10-N", "Route 10-C", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 10-C", "Route 10-P", lambda state: state.has("Plant Key", player) or not world.options.extra_key_items.value)
    connect(multiworld, player, "Pallet Town", "Pallet/Viridian Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Viridian City", "Pallet/Viridian Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 22", "Route 22 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 24", "Route 24/25/Cerulean/Cerulean Gym Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 25", "Route 24/25/Cerulean/Cerulean Gym Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean City", "Route 24/25/Cerulean/Cerulean Gym Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Gym", "Route 24/25/Cerulean/Cerulean Gym Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 6", "Route 6/11/Vermilion/Dock Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 11", "Route 6/11/Vermilion/Dock Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Vermilion City", "Route 6/11/Vermilion/Dock Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Vermilion Dock", "Route 6/11/Vermilion/Dock Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 10-N", "Route 10/Celadon Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 10-C", "Route 10/Celadon Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Celadon City", "Route 10/Celadon Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone Center-NW", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone Center-NE", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone Center-S", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone West", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone West-NW", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone East", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Safari Zone North", "Safari Zone Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 12-N", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 12-S", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 13", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 13-E", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 17", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 18-W", "Route 12/13/17/18 Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 21", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cinnabar Island", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 20-IW", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 20-IE", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 19-N", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Seafoam Islands B4F", "Sea Routes/Cinnabar/Seafoam Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 23-S", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Route 23-Grass", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-SE", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-NE", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-N", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-SW", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Cerulean Cave B1F", "Route 23/Cerulean Cave Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Fuchsia City", "Fuchsia Fishing", lambda state: state.has("Super Rod", player), one_way=True)
    connect(multiworld, player, "Pallet Town", "Old Rod Fishing", lambda state: state.has("Old Rod", player), one_way=True)
    connect(multiworld, player, "Pallet Town", "Good Rod Fishing", lambda state: state.has("Good Rod", player), one_way=True)
    connect(multiworld, player, "Cinnabar Lab Fossil Room", "Fossil Level", lambda state: logic.fossil_checks(state, 1, player), one_way=True)
    connect(multiworld, player, "Route 5 Gate-N", "Route 5 Gate-S", lambda state: logic.can_pass_guards(state, world, player))
    connect(multiworld, player, "Route 6 Gate-N", "Route 6 Gate-S", lambda state: logic.can_pass_guards(state, world, player))
    connect(multiworld, player, "Route 7 Gate-W", "Route 7 Gate-E", lambda state: logic.can_pass_guards(state, world, player))
    connect(multiworld, player, "Route 8 Gate-W", "Route 8 Gate-E", lambda state: logic.can_pass_guards(state, world, player))
    connect(multiworld, player, "Saffron City", "Route 5-S")
    connect(multiworld, player, "Saffron City", "Route 6-N")
    connect(multiworld, player, "Saffron City", "Route 7-E")
    connect(multiworld, player, "Saffron City", "Route 8-W")
    connect(multiworld, player, "Saffron City", "Saffron City-Copycat", lambda state: state.has("Silph Co Liberated", player))
    connect(multiworld, player, "Saffron City", "Saffron City-Pidgey", lambda state: state.has("Silph Co Liberated", player))
    connect(multiworld, player, "Saffron City", "Saffron City-G", lambda state: state.has("Silph Co Liberated", player))
    connect(multiworld, player, "Saffron City", "Saffron City-Silph", lambda state: state.has("Fuji Saved", player))
    connect(multiworld, player, "Route 6", "Vermilion City")
    connect(multiworld, player, "Vermilion City", "Vermilion City-G", lambda state: logic.can_surf(state, world, player) or logic.can_cut(state, world, player))
    connect(multiworld, player, "Vermilion City", "Vermilion City-Dock", lambda state: state.has("S.S. Ticket", player))
    connect(multiworld, player, "Vermilion City", "Route 11")
    connect(multiworld, player, "Route 12-N", "Route 12-S", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 12-W", "Route 11-E")
    connect(multiworld, player, "Route 12-W", "Route 12-N", lambda state: state.has("Poke Flute", player))
    connect(multiworld, player, "Route 12-W", "Route 12-S", lambda state: state.has("Poke Flute", player))
    connect(multiworld, player, "Route 12-S", "Route 12-Grass", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Route 12-L", "Lavender Town")
    connect(multiworld, player, "Route 10-S", "Lavender Town")
    connect(multiworld, player, "Route 8", "Lavender Town")
    connect(multiworld, player, "Pokemon Tower 6F", "Pokemon Tower 6F-S", lambda state: state.has("Silph Scope", player) or (state.has("Buy Poke Doll", player) and world.options.poke_doll_skip))
    connect(multiworld, player, "Route 8", "Route 8-Grass", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Route 7", "Celadon City")
    connect(multiworld, player, "Celadon City", "Celadon City-G", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Celadon City", "Route 16-E")
    connect(multiworld, player, "Route 18 Gate 1F-W", "Route 18 Gate 1F-E", lambda state: state.has("Bicycle", player) or world.options.bicycle_gate_skips == "in_logic")
    connect(multiworld, player, "Route 16 Gate 1F-W", "Route 16 Gate 1F-E", lambda state: state.has("Bicycle", player) or world.options.bicycle_gate_skips == "in_logic")
    connect(multiworld, player, "Route 16-E", "Route 16-NE", lambda state: logic.can_cut(state, world, player))
    connect(multiworld, player, "Route 16-E", "Route 16-C", lambda state: state.has("Poke Flute", player))
    connect(multiworld, player, "Route 17", "Route 16-SW")
    connect(multiworld, player, "Route 17", "Route 18-W")
    # connect(multiworld, player, "Pokemon Mansion 2F", "Pokemon Mansion 2F-NW", one_way=True)
    connect(multiworld, player, "Safari Zone Gate-S", "Safari Zone Gate-N", lambda state: state.has("Safari Pass", player) or not world.options.extra_key_items.value, one_way=True)
    connect(multiworld, player, "Fuchsia City", "Route 15-W")
    connect(multiworld, player, "Fuchsia City", "Route 18-E")
    connect(multiworld, player, "Route 15", "Route 14")
    connect(multiworld, player, "Route 14", "Route 15-N", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Route 14", "Route 14-Grass", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Route 13", "Route 13-Grass", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Route 14", "Route 13")
    connect(multiworld, player, "Route 13", "Route 13-E", lambda state: logic.can_strength(state, world, player) or logic.can_surf(state, world, player) or not world.options.extra_strength_boulders.value)
    connect(multiworld, player, "Route 12-S", "Route 13-E")
    connect(multiworld, player, "Fuchsia City", "Route 19-N")
    connect(multiworld, player, "Route 19-N", "Route 19-S", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 20-E", "Route 20-IW", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 20-E", "Route 19-S")
    connect(multiworld, player, "Route 20-W", "Cinnabar Island", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 20-IE", "Route 20-W", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Route 20-E", "Route 19/20-Water", one_way=True)
    connect(multiworld, player, "Route 20-W", "Route 19/20-Water", one_way=True)
    connect(multiworld, player, "Route 19-S", "Route 19/20-Water", one_way=True)
    connect(multiworld, player, "Safari Zone West-NW", "Safari Zone West", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Safari Zone West", "Safari Zone West-Wild", one_way=True)
    connect(multiworld, player, "Safari Zone West-NW", "Safari Zone West-Wild", one_way=True)
    connect(multiworld, player, "Safari Zone Center-NW", "Safari Zone Center-C", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Safari Zone Center-NE", "Safari Zone Center-C", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Safari Zone Center-S", "Safari Zone Center-C", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Safari Zone Center-S", "Safari Zone Center-Wild", one_way=True)
    connect(multiworld, player, "Safari Zone Center-NW", "Safari Zone Center-Wild", one_way=True)
    connect(multiworld, player, "Safari Zone Center-NE", "Safari Zone Center-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 3F-S", "Victory Road 3F", lambda state: logic.can_strength(state, world, player))
    connect(multiworld, player, "Victory Road 3F-SE", "Victory Road 3F-S", lambda state: logic.can_strength(state, world, player), one_way=True)
    connect(multiworld, player, "Victory Road 3F", "Victory Road 3F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 3F-SE", "Victory Road 3F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 3F-S", "Victory Road 3F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-W", "Victory Road 2F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-NW", "Victory Road 2F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-C", "Victory Road 2F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-E", "Victory Road 2F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-SE", "Victory Road 2F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 2F-W", "Victory Road 2F-C", lambda state: logic.can_strength(state, world, player), one_way=True)
    connect(multiworld, player, "Victory Road 2F-NW", "Victory Road 2F-W", lambda state: logic.can_strength(state, world, player), one_way=True)
    connect(multiworld, player, "Victory Road 2F-C", "Victory Road 2F-SE", lambda state: logic.can_strength(state, world, player) and state.has("Victory Road Boulder", player), one_way=True)
    connect(multiworld, player, "Victory Road 1F-S", "Victory Road 1F", lambda state: logic.can_strength(state, world, player))
    connect(multiworld, player, "Victory Road 1F", "Victory Road 1F-Wild", one_way=True)
    connect(multiworld, player, "Victory Road 1F-S", "Victory Road 1F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B1F-W", "Mt Moon B1F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B1F-C", "Mt Moon B1F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B1F-NE", "Mt Moon B1F-Wild", one_way=True)
    connect(multiworld, player, "Mt Moon B1F-SE", "Mt Moon B1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 2F-N", "Cerulean Cave 2F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 2F-E", "Cerulean Cave 2F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 2F-W", "Cerulean Cave 2F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands 1F", "Seafoam Islands 1F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands 1F-SE", "Seafoam Islands 1F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B1F", "Seafoam Islands B1F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B1F-SE", "Seafoam Islands B1F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B1F-NE", "Seafoam Islands B1F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NW", "Seafoam Islands B2F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NE", "Seafoam Islands B2F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-SW", "Seafoam Islands B2F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-SE", "Seafoam Islands B2F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F", "Seafoam Islands B3F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F-NE", "Seafoam Islands B3F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F-SE", "Seafoam Islands B3F-Wild", one_way=True)
    connect(multiworld, player, "Seafoam Islands B4F", "Seafoam Islands B4F-W", lambda state: logic.can_surf(state, world, player), one_way=True)
    connect(multiworld, player, "Seafoam Islands B4F-W", "Seafoam Islands B4F", one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F", "Seafoam Islands B3F-SE", lambda state: logic.can_surf(state, world, player) and logic.can_strength(state, world, player) and state.has("Seafoam Exit Boulder", player, 6))
    connect(multiworld, player, "Viridian City", "Viridian City-N", lambda state: state.has("Oak's Parcel", player) or world.options.old_man.value == 2 or logic.can_cut(state, world, player))
    connect(multiworld, player, "Route 11", "Route 11-C", lambda state: logic.can_strength(state, world, player) or not world.options.extra_strength_boulders)
    connect(multiworld, player, "Cinnabar Island", "Cinnabar Island-G", lambda state: state.has("Secret Key", player))
    connect(multiworld, player, "Cinnabar Island", "Cinnabar Island-M", lambda state: state.has("Mansion Key", player) or not world.options.extra_key_items.value)
    connect(multiworld, player, "Route 21", "Cinnabar Island", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Pallet Town", "Route 21", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Celadon Gym", "Celadon Gym-C", lambda state: logic.can_cut(state, world, player), one_way=True)
    connect(multiworld, player, "Celadon Game Corner", "Celadon Game Corner-Hidden Stairs", lambda state: (not world.options.extra_key_items) or state.has("Hideout Key", player), one_way=True)
    connect(multiworld, player, "Celadon Game Corner-Hidden Stairs", "Celadon Game Corner", one_way=True)
    connect(multiworld, player, "Rocket Hideout B1F-SE", "Rocket Hideout B1F", one_way=True)
    connect(multiworld, player, "Indigo Plateau Lobby", "Indigo Plateau Lobby-N", lambda state: logic.has_badges(state, world.options.elite_four_badges_condition.value, player) and logic.has_pokemon(state, world.options.elite_four_pokedex_condition.total, player) and logic.has_key_items(state, world.options.elite_four_key_items_condition.total, player) and (state.has("Pokedex", player, int(world.options.elite_four_pokedex_condition.total > 1) * world.options.require_pokedex.value)))
    connect(multiworld, player, "Pokemon Mansion 3F", "Pokemon Mansion 3F-Wild", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 3F-SW", "Pokemon Mansion 3F-Wild", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 3F-SE", "Pokemon Mansion 3F-Wild", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 2F-E", "Pokemon Mansion 2F-Wild", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 1F-SE", "Pokemon Mansion 1F-Wild", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 1F", "Pokemon Mansion 1F-Wild", one_way=True)
    connect(multiworld, player, "Rock Tunnel 1F-S 1", "Rock Tunnel 1F-S", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-S 2", "Rock Tunnel 1F-S", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-NW 1", "Rock Tunnel 1F-NW", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-NW 2", "Rock Tunnel 1F-NW", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-NE 1", "Rock Tunnel 1F-NE", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-NE 2", "Rock Tunnel 1F-NE", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel B1F-W 1", "Rock Tunnel B1F-W", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel B1F-W 2", "Rock Tunnel B1F-W", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel B1F-E 1", "Rock Tunnel B1F-E", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel B1F-E 2", "Rock Tunnel B1F-E", lambda state: logic.rock_tunnel(state, world, player))
    connect(multiworld, player, "Rock Tunnel 1F-S", "Rock Tunnel 1F-Wild", lambda state: logic.rock_tunnel(state, world, player), one_way=True)
    connect(multiworld, player, "Rock Tunnel 1F-NW", "Rock Tunnel 1F-Wild", lambda state: logic.rock_tunnel(state, world, player), one_way=True)
    connect(multiworld, player, "Rock Tunnel 1F-NE", "Rock Tunnel 1F-Wild", lambda state: logic.rock_tunnel(state, world, player), one_way=True)
    connect(multiworld, player, "Rock Tunnel B1F-W", "Rock Tunnel B1F-Wild", lambda state: logic.rock_tunnel(state, world, player), one_way=True)
    connect(multiworld, player, "Rock Tunnel B1F-E", "Rock Tunnel B1F-Wild", lambda state: logic.rock_tunnel(state, world, player), one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-SE", "Cerulean Cave 1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-SW", "Cerulean Cave 1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-NE", "Cerulean Cave 1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-N", "Cerulean Cave 1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-NW", "Cerulean Cave 1F-Wild", one_way=True)
    connect(multiworld, player, "Cerulean Cave 1F-SE", "Cerulean Cave 1F-Water", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Cerulean Cave 1F-SW", "Cerulean Cave 1F-Water", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Cerulean Cave 1F-N", "Cerulean Cave 1F-Water", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Cerulean Cave 1F-NE", "Cerulean Cave 1F-Water", lambda state: logic.can_surf(state, world, player))
    connect(multiworld, player, "Pokemon Mansion 3F", "Pokemon Mansion 3F-SE", one_way=True)
    connect(multiworld, player, "Silph Co 2F", "Silph Co 2F-NW", lambda state: logic.card_key(state, 2, player))
    connect(multiworld, player, "Silph Co 2F", "Silph Co 2F-SW", lambda state: logic.card_key(state, 2, player))
    connect(multiworld, player, "Silph Co 3F", "Silph Co 3F-C", lambda state: logic.card_key(state, 3, player))
    connect(multiworld, player, "Silph Co 3F-W", "Silph Co 3F-C", lambda state: logic.card_key(state, 3, player))
    connect(multiworld, player, "Silph Co 4F", "Silph Co 4F-N", lambda state: logic.card_key(state, 4, player))
    connect(multiworld, player, "Silph Co 4F", "Silph Co 4F-W", lambda state: logic.card_key(state, 4, player))
    connect(multiworld, player, "Silph Co 5F", "Silph Co 5F-NW", lambda state: logic.card_key(state, 5, player))
    connect(multiworld, player, "Silph Co 5F", "Silph Co 5F-SW", lambda state: logic.card_key(state, 5, player))
    connect(multiworld, player, "Silph Co 6F", "Silph Co 6F-SW", lambda state: logic.card_key(state, 6, player))
    connect(multiworld, player, "Silph Co 7F", "Silph Co 7F-E", lambda state: logic.card_key(state, 7, player))
    connect(multiworld, player, "Silph Co 7F-SE", "Silph Co 7F-E", lambda state: logic.card_key(state, 7, player))
    connect(multiworld, player, "Silph Co 8F", "Silph Co 8F-W", lambda state: logic.card_key(state, 8, player), one_way=True, name="Silph Co 8F to Silph Co 8F-W (Card Key)")
    connect(multiworld, player, "Silph Co 8F-W", "Silph Co 8F", lambda state: logic.card_key(state, 8, player), one_way=True, name="Silph Co 8F-W to Silph Co 8F (Card Key)")
    connect(multiworld, player, "Silph Co 9F", "Silph Co 9F-SW", lambda state: logic.card_key(state, 9, player))
    connect(multiworld, player, "Silph Co 9F-NW", "Silph Co 9F-SW", lambda state: logic.card_key(state, 9, player))
    connect(multiworld, player, "Silph Co 10F", "Silph Co 10F-SE", lambda state: logic.card_key(state, 10, player))
    connect(multiworld, player, "Silph Co 11F-W", "Silph Co 11F-C", lambda state: logic.card_key(state, 11, player))
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-1F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-2F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-3F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-4F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-5F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-6F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-7F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-8F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-9F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-10F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Silph Co Elevator", "Silph Co Elevator-11F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Rocket Hideout Elevator", "Rocket Hideout Elevator-B1F", lambda state: state.has("Lift Key", player))
    connect(multiworld, player, "Rocket Hideout Elevator", "Rocket Hideout Elevator-B2F", lambda state: state.has("Lift Key", player))
    connect(multiworld, player, "Rocket Hideout Elevator", "Rocket Hideout Elevator-B4F", lambda state: state.has("Lift Key", player))
    connect(multiworld, player, "Celadon Department Store Elevator", "Celadon Department Store Elevator-1F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Celadon Department Store Elevator", "Celadon Department Store Elevator-2F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Celadon Department Store Elevator", "Celadon Department Store Elevator-3F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Celadon Department Store Elevator", "Celadon Department Store Elevator-4F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Celadon Department Store Elevator", "Celadon Department Store Elevator-5F", lambda state: (not world.options.all_elevators_locked) or state.has("Lift Key", player)),
    connect(multiworld, player, "Route 23-N", "Indigo Plateau")
    connect(multiworld, player, "Cerulean City-Water", "Cerulean City-Cave", lambda state:
    logic.has_badges(state, world.options.cerulean_cave_badges_condition.value, player) and
    logic.has_key_items(state, world.options.cerulean_cave_key_items_condition.total, player) and logic.can_surf(state, world, player))

    # access to any part of a city will enable flying to the Pokemon Center
    connect(multiworld, player, "Cerulean City-Cave", "Cerulean City", lambda state: logic.can_fly(state, world, player), one_way=True)
    connect(multiworld, player, "Cerulean City-Badge House Backyard", "Cerulean City", lambda state: logic.can_fly(state, world, player), one_way=True)
    connect(multiworld, player, "Cerulean City-T", "Cerulean City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Cerulean City-T to Cerulean City (Fly)")
    connect(multiworld, player, "Fuchsia City-Good Rod House Backyard", "Fuchsia City", lambda state: logic.can_fly(state, world, player), one_way=True)
    connect(multiworld, player, "Saffron City-G", "Saffron City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Saffron City-G to Saffron City (Fly)")
    connect(multiworld, player, "Saffron City-Pidgey", "Saffron City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Saffron City-Pidgey to Saffron City (Fly)")
    connect(multiworld, player, "Saffron City-Silph", "Saffron City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Saffron City-Silph to Saffron City (Fly)")
    connect(multiworld, player, "Saffron City-Copycat", "Saffron City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Saffron City-Copycat to Saffron City (Fly)")
    connect(multiworld, player, "Celadon City-G", "Celadon City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Celadon City-G to Celadon City (Fly)")
    connect(multiworld, player, "Vermilion City-G", "Vermilion City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Vermilion City-G to Vermilion City (Fly)")
    connect(multiworld, player, "Vermilion City-Dock", "Vermilion City", lambda state: logic.can_fly(state, world, player), one_way=True, name="Vermilion City-Dock to Vermilion City (Fly)")
    connect(multiworld, player, "Cinnabar Island-G", "Cinnabar Island", lambda state: logic.can_fly(state, world, player), one_way=True, name="Cinnabar Island-G to Cinnabar Island (Fly)")
    connect(multiworld, player, "Cinnabar Island-M", "Cinnabar Island", lambda state: logic.can_fly(state, world, player), one_way=True, name="Cinnabar Island-M to Cinnabar Island (Fly)")

    # drops
    connect(multiworld, player, "Seafoam Islands 1F", "Seafoam Islands B1F", one_way=True, name="Seafoam Islands 1F to Seafoam Islands B1F (Drop)")
    connect(multiworld, player, "Seafoam Islands 1F", "Seafoam Islands B1F-NE", one_way=True, name="Seafoam Islands 1F to Seafoam Islands B1F-NE (Drop)")
    connect(multiworld, player, "Seafoam Islands B1F", "Seafoam Islands B2F-NW", one_way=True, name="Seafoam Islands 1F to Seafoam Islands B2F-NW (Drop)")
    connect(multiworld, player, "Seafoam Islands B1F-NE", "Seafoam Islands B2F-NE", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NW", "Seafoam Islands B3F", lambda state: logic.can_strength(state, world, player) and state.has("Seafoam Exit Boulder", player, 6), one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NE", "Seafoam Islands B3F", lambda state: logic.can_strength(state, world, player) and state.has("Seafoam Exit Boulder", player, 6), one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NW", "Seafoam Islands B3F-SE", lambda state: logic.can_strength(state, world, player) and state.has("Seafoam Exit Boulder", player, 6), one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NE", "Seafoam Islands B3F-SE", lambda state: logic.can_strength(state, world, player) and state.has("Seafoam Exit Boulder", player, 6), one_way=True)
    # If you haven't dropped the boulders, you'll go straight to B4F
    connect(multiworld, player, "Seafoam Islands B2F-NW", "Seafoam Islands B4F-W", one_way=True)
    connect(multiworld, player, "Seafoam Islands B2F-NE", "Seafoam Islands B4F-W", one_way=True)
    connect(multiworld, player, "Seafoam Islands B3F", "Seafoam Islands B4F", one_way=True, name="Seafoam Islands B1F to Seafoam Islands B4F (Drop)")
    connect(multiworld, player, "Seafoam Islands B3F", "Seafoam Islands B4F-W", lambda state: logic.can_surf(state, world, player), one_way=True)
    connect(multiworld, player, "Pokemon Mansion 3F-SE", "Pokemon Mansion 2F", one_way=True)
    connect(multiworld, player, "Pokemon Mansion 3F-SE", "Pokemon Mansion 1F-SE", one_way=True)
    connect(multiworld, player, "Victory Road 3F-S", "Victory Road 2F-C", one_way=True)

    if world.fly_map != "Pallet Town":
        connect(multiworld, player, "Menu", world.fly_map,
                lambda state: logic.can_fly(state, world, player), one_way=True, name="Free Fly Location")

    if world.town_map_fly_map != "Pallet Town":
        connect(multiworld, player, "Menu", world.town_map_fly_map,
                lambda state: logic.can_fly(state, world, player) and state.has("Town Map", player), one_way=True,
                name="Town Map Fly Location")

    cache = multiworld.regions.entrance_cache[world.player].copy()
    if world.options.badgesanity or world.options.door_shuffle in ("off", "simple"):
        badges = None
        badge_locs = None
    else:
        badges = [item for item in world.item_pool if "Badge" in item.name]
        for badge in badges:
            world.item_pool.remove(badge)
        badge_locs = [multiworld.get_location(loc, player) for loc in [
            "Pewter Gym - Brock Prize", "Cerulean Gym - Misty Prize", "Vermilion Gym - Lt. Surge Prize",
            "Celadon Gym - Erika Prize", "Fuchsia Gym - Koga Prize", "Saffron Gym - Sabrina Prize",
            "Cinnabar Gym - Blaine Prize", "Viridian Gym - Giovanni Prize"
        ]]
    for attempt in range(10):
        try:
            door_shuffle(world, multiworld, player, badges, badge_locs)
        except DoorShuffleException as e:
            if attempt == 9:
                raise e
            for region in world.multiworld.get_regions(player):
                for entrance in reversed(region.exits):
                    if isinstance(entrance, PokemonTCGWarp):
                        region.exits.remove(entrance)
                for entrance in reversed(region.entrances):
                    if isinstance(entrance, PokemonTCGWarp):
                        region.entrances.remove(entrance)
            multiworld.regions.entrance_cache[world.player] = cache.copy()
            if badge_locs:
                for loc in badge_locs:
                    loc.item = None
                    loc.locked = False
        else:
            break


def door_shuffle(world, multiworld, player, badges, badge_locs):
    entrances = []
    full_interiors = []
    for region_name, region_entrances in warp_data.items():
        region = multiworld.get_region(region_name, player)
        for entrance_data in region_entrances:
            shuffle = True
            interior = False
            if not outdoor_map(region.name) and not outdoor_map(entrance_data['to']['map']):
                if world.options.door_shuffle not in ("full", "insanity", "decoupled"):
                    shuffle = False
                interior = True
            if world.options.door_shuffle == "simple":
                if sorted([entrance_data['to']['map'], region.name]) == ["Celadon Game Corner-Hidden Stairs",
                                                                         "Rocket Hideout B1F"]:
                    shuffle = True
                elif sorted([entrance_data['to']['map'], region.name]) == ["Celadon City", "Celadon Game Corner"]:
                    shuffle = False
            if (world.options.randomize_rock_tunnel and "Rock Tunnel" in region.name and "Rock Tunnel" in
                    entrance_data['to']['map']):
                shuffle = False
            elif (f"{region.name} to {entrance_data['to']['map']}" if "name" not in entrance_data else
                    entrance_data["name"]) in silph_co_warps + saffron_gym_warps:
                if world.options.warp_tile_shuffle:
                    shuffle = True
                    if world.options.warp_tile_shuffle == "mixed" and world.options.door_shuffle == "full":
                        interior = True
                    else:
                        interior = False
                else:
                    shuffle = False
            elif not world.options.door_shuffle:
                shuffle = False
            if shuffle:
                entrance = PokemonTCGWarp(player, f"{region.name} to {entrance_data['to']['map']}" if "name" not in
                                         entrance_data else entrance_data["name"], region, entrance_data["id"],
                                         entrance_data["address"], entrance_data["flags"] if "flags" in
                                         entrance_data else "")
                if interior and world.options.door_shuffle == "full":
                    full_interiors.append(entrance)
                else:
                    entrances.append(entrance)
                region.exits.append(entrance)
            else:
                connect(multiworld, player, region.name, entrance_data["to"]["map"], one_way=True,
                        name=entrance_data["name"] if "name" in entrance_data else None)

    forced_connections = set()
    one_way_forced_connections = set()

    if world.options.door_shuffle:
        if world.options.door_shuffle in ("full", "insanity", "decoupled"):
            safari_zone_doors = [door for pair in safari_zone_connections for door in pair]
            safari_zone_doors.sort()
            order = ["Center", "East", "North", "West"]
            world.random.shuffle(order)
            usable_doors = ["Safari Zone Gate-N to Safari Zone Center-S"]
            for section in order:
                section_doors = [door for door in safari_zone_doors if door.startswith(f"Safari Zone {section}")]
                connect_door_a = world.random.choice(usable_doors)
                connect_door_b = world.random.choice(section_doors)
                usable_doors.remove(connect_door_a)
                section_doors.remove(connect_door_b)
                forced_connections.add((connect_door_a, connect_door_b))
                usable_doors += section_doors
                world.random.shuffle(usable_doors)
            while usable_doors:
                forced_connections.add((usable_doors.pop(), usable_doors.pop()))
        else:
            forced_connections.update(safari_zone_connections)

        usable_safe_rooms = safe_rooms.copy()

        if world.options.door_shuffle == "simple":
            forced_connections.update(simple_mandatory_connections)
        else:
            usable_safe_rooms += pokemarts
            if world.options.key_items_only:
                usable_safe_rooms.remove("Viridian Pokemart to Viridian City")
        if world.options.door_shuffle in ("full", "insanity", "decoupled"):
            forced_connections.update(full_mandatory_connections)
            r = world.random.randint(0, 3)
            if r == 2:
                forced_connections.add(("Pokemon Mansion 1F-SE to Pokemon Mansion B1F",
                                        "Pokemon Mansion 3F-SE to Pokemon Mansion 2F-E"))
                forced_connections.add(("Pokemon Mansion 2F to Pokemon Mansion 3F",
                                        world.random.choice(mansion_stair_destinations + mansion_dead_ends
                                                                 + ["Pokemon Mansion B1F to Pokemon Mansion 1F-SE"])))
                if world.options.door_shuffle == "full":
                    forced_connections.add(("Pokemon Mansion 1F to Pokemon Mansion 2F",
                                            "Pokemon Mansion 3F to Pokemon Mansion 2F"))
            elif r == 3:
                dead_end = world.random.randint(0, 1)
                forced_connections.add(("Pokemon Mansion 3F-SE to Pokemon Mansion 2F-E",
                                        mansion_dead_ends[dead_end]))
                forced_connections.add(("Pokemon Mansion 1F-SE to Pokemon Mansion B1F",
                                        "Pokemon Mansion B1F to Pokemon Mansion 1F-SE"))
                forced_connections.add(("Pokemon Mansion 2F to Pokemon Mansion 3F",
                                        world.random.choice(mansion_stair_destinations
                                                                 + [mansion_dead_ends[dead_end ^ 1]])))
            else:
                forced_connections.add(("Pokemon Mansion 3F-SE to Pokemon Mansion 2F-E",
                                        mansion_dead_ends[r]))
                forced_connections.add(("Pokemon Mansion 1F-SE to Pokemon Mansion B1F",
                                        mansion_dead_ends[r ^ 1]))
                forced_connections.add(("Pokemon Mansion 2F to Pokemon Mansion 3F",
                                        world.random.choice(mansion_stair_destinations
                                                                 + ["Pokemon Mansion B1F to Pokemon Mansion 1F-SE"])))

            if world.options.door_shuffle in ("insanity", "decoupled"):
                usable_safe_rooms += insanity_safe_rooms

        safe_rooms_sample = world.random.sample(usable_safe_rooms, 6)
        pallet_safe_room = safe_rooms_sample[-1]

        for a, b in zip(world.random.sample(["Pallet Town to Player's House 1F", "Pallet Town to Oak's Lab",
                                                  "Pallet Town to Rival's House"], 3), ["Oak's Lab to Pallet Town",
                                                  "Player's House 1F to Pallet Town", pallet_safe_room]):
            one_way_forced_connections.add((a, b))

        if world.options.door_shuffle == "decoupled":
            for a, b in zip(["Oak's Lab to Pallet Town", "Player's House 1F to Pallet Town", pallet_safe_room],
                            world.random.sample(["Pallet Town to Player's House 1F", "Pallet Town to Oak's Lab",
                                                      "Pallet Town to Rival's House"], 3)):
                one_way_forced_connections.add((a, b))

        for a, b in zip(safari_zone_houses, safe_rooms_sample):
            one_way_forced_connections.add((a, b))
        if world.options.door_shuffle == "decoupled":
            for a, b in zip(world.random.sample(safe_rooms_sample[:-1], len(safe_rooms_sample) - 1),
                            safari_zone_houses):
                one_way_forced_connections.add((a, b))

        if world.options.door_shuffle == "simple":
            # force Indigo Plateau Lobby to vanilla location on simple, otherwise shuffle with Pokemon Centers.
            for a, b in zip(world.random.sample(pokemon_center_entrances[0:-1], 11), pokemon_centers[0:-1]):
                forced_connections.add((a, b))
            forced_connections.add((pokemon_center_entrances[-1], pokemon_centers[-1]))
            forced_pokemarts = world.random.sample(pokemart_entrances, 8)
            if world.options.key_items_only:
                forced_pokemarts.sort(key=lambda i: i[0] != "Viridian Pokemart to Viridian City")
            for a, b in zip(forced_pokemarts, pokemarts):
                forced_connections.add((a, b))
        else:
            # Pokemon Centers must be reached from the Cities and Routes that have programmed coordinates for
            # fly / blackout warps. Rather than mess with those coordinates (besides in Pallet Town) or have players
            # warping outside an entrance that isn't the Pokemon Center, just always put Pokemon Centers at Pokemon
            # Center entrances
            for a, b in zip(world.random.sample(pokemon_center_entrances, 12), pokemon_centers):
                one_way_forced_connections.add((a, b))
            # Ensure a Pokemart is available at the beginning of the game
            if world.options.key_items_only:
                one_way_forced_connections.add((world.random.choice(initial_doors),
                                                "Viridian Pokemart to Viridian City"))

            elif "Pokemart" not in pallet_safe_room:
                one_way_forced_connections.add((world.random.choice(initial_doors), world.random.choice(
                        [mart for mart in pokemarts if mart not in safe_rooms_sample])))

    if world.options.warp_tile_shuffle == "shuffle" or (world.options.warp_tile_shuffle == "mixed"
                                                        and world.options.door_shuffle
                                                        in ("off", "simple", "interiors")):
        warps = world.random.sample(silph_co_warps, len(silph_co_warps))
        # The only warp tiles never reachable from the stairs/elevators are the two 7F-NW warps (where the rival is)
        # and the final 11F-W warp. As long as the two 7F-NW warps aren't connected to each other, everything should
        # always be reachable.
        warps.sort(key=lambda i: 0 if i == "Silph Co 7F-NW to Silph Co 3F-C" else
                   2 if i == "Silph Co 7F-NW to Silph Co 11F-W" else 1)
        while warps:
            forced_connections.add((warps.pop(), warps.pop(),))

        # Shuffle Saffron Gym sections, then connect one warp from each section to the next.
        # Then connect the rest at random.
        warps = world.random.sample(saffron_gym_warps, len(saffron_gym_warps))
        solution = ["SW", "W", "NW", "N", "NE", "E", "SE"]
        world.random.shuffle(solution)
        solution = ["S"] + solution + ["C"]
        for i in range(len(solution) - 1):
            f, t = solution[i], solution[i + 1]
            fw = None
            tw = None
            for warp in warps:
                if fw is None and warp.split(" to ")[0].endswith(f"-{f}"):
                    fw = warp
                if tw is None and warp.split(" to ")[0].endswith(f"-{t}"):
                    tw = warp
                if fw is not None and tw is not None:
                    break
            warps.remove(fw)
            warps.remove(tw)
            forced_connections.add((fw, tw))
        while warps:
            forced_connections.add((warps.pop(), warps.pop(),))

    dc_destinations = None
    if world.options.door_shuffle == "decoupled":
        dc_destinations = entrances.copy()
        for pair in one_way_forced_connections:
            entrance_a = multiworld.get_entrance(pair[0], player)
            entrance_b = multiworld.get_entrance(pair[1], player)
            entrance_a.connect(entrance_b)
            entrances.remove(entrance_a)
            dc_destinations.remove(entrance_b)
    else:
        forced_connections.update(one_way_forced_connections)

    for pair in forced_connections:
        entrance_a = multiworld.get_entrance(pair[0], player)
        entrance_b = multiworld.get_entrance(pair[1], player)
        entrance_a.connect(entrance_b)
        entrance_b.connect(entrance_a)
        if entrance_a in entrances:
            entrances.remove(entrance_a)
        elif entrance_a in full_interiors:
            full_interiors.remove(entrance_a)
        else:
            raise DoorShuffleException("Attempted to force connection with entrance not in any entrance pool, likely because it tried to force an entrance to connect twice.")
        if entrance_b in entrances:
            entrances.remove(entrance_b)
        elif entrance_b in full_interiors:
            full_interiors.remove(entrance_b)
        else:
            raise DoorShuffleException("Attempted to force connection with entrance not in any entrance pool, likely because it tried to force an entrance to connect twice.")
        if world.options.door_shuffle == "decoupled":
            dc_destinations.remove(entrance_a)
            dc_destinations.remove(entrance_b)

    if world.options.door_shuffle == "simple":
        def connect_connecting_interiors(interior_exits, exterior_entrances):
            for interior, exterior in zip(interior_exits, exterior_entrances):
                for a, b in zip(interior, exterior):
                    entrance_a = multiworld.get_entrance(a, player)
                    if b is None:
                        # entrance_b = multiworld.get_entrance(entrances[0], player)
                        # should just be able to use the entrance_b from the previous link?
                        pass
                    else:
                        entrance_b = multiworld.get_entrance(b, player)
                        entrance_b.connect(entrance_a)
                        entrances.remove(entrance_b)
                    entrance_a.connect(entrance_b)
                    entrances.remove(entrance_a)

        def connect_interiors(interior_exits, exterior_entrances):
            for a, b in zip(interior_exits, exterior_entrances):
                if isinstance(a, list):
                    entrance_a = multiworld.get_entrance(a[0], player)
                else:
                    entrance_a = multiworld.get_entrance(a, player)
                entrance_b = multiworld.get_entrance(b, player)
                entrance_a.connect(entrance_b)
                entrance_b.connect(entrance_a)
                entrances.remove(entrance_b)
                entrances.remove(entrance_a)
                if isinstance(a, list):
                    entrance_a = multiworld.get_entrance(a[1], player)
                    entrance_a.connect(entrance_b)
                    entrances.remove(entrance_a)

        placed_connecting_interior_dungeons = safe_connecting_interior_dungeons + unsafe_connecting_interior_dungeons
        interior_dungeon_entrances = connecting_interior_dungeon_entrances.copy()

        placed_single_entrance_dungeons = dungeons.copy()
        single_entrance_dungeon_entrances = dungeon_entrances.copy()

        for i in range(2):
            if not world.random.randint(0, 2):
                placed_connecting_interior_dungeons.append(multi_purpose_dungeons[i])
                interior_dungeon_entrances.append([multi_purpose_dungeon_entrances[i], None])
            else:
                placed_single_entrance_dungeons.append(multi_purpose_dungeons[i])
                single_entrance_dungeon_entrances.append(multi_purpose_dungeon_entrances[i])

        world.random.shuffle(placed_connecting_interior_dungeons)
        while placed_connecting_interior_dungeons[0] in unsafe_connecting_interior_dungeons:
            world.random.shuffle(placed_connecting_interior_dungeons)
        connect_connecting_interiors(placed_connecting_interior_dungeons, interior_dungeon_entrances)

        interiors = connecting_interiors.copy()
        world.random.shuffle(interiors)
        while ((connecting_interiors[2] in (interiors[2], interiors[10], interiors[11])  # Dept Store at Dept Store
                                                                                         # or Rt 16 Gate S or N
                and (interiors[11] in connecting_interiors[13:17]  # Saffron Gate at Rt 16 Gate S
                     or interiors[12] in connecting_interiors[13:17]))  # Saffron Gate at Rt 18 Gate
                and interiors[15] in connecting_interiors[13:17]  # Saffron Gate at Rt 7 Gate
                and interiors[1] in connecting_interiors[13:17]  # Saffron Gate at Rt 7-8 Underground Path
                and (not world.options.tea) and world.fly_map != "Celadon City"
                and world.town_map_fly_map != "Celadon City"):
            world.random.shuffle(interiors)

        connect_connecting_interiors(interiors, connecting_interior_entrances)
        placed_gyms = gyms.copy()
        world.random.shuffle(placed_gyms)

        # Celadon Gym requires Cut access to reach the Gym Leader. There are some scenarios where its placement
        # could make badge placement impossible
        def celadon_gym_problem():
            # Badgesanity or no badges needed for HM moves means gyms can go anywhere
            if world.options.badgesanity or not world.options.badges_needed_for_hm_moves:
                return False

            # Celadon Gym in Pewter City and need one or more badges for Viridian City gym.
            # No gym leaders would be reachable.
            if gyms[3] == placed_gyms[0] and world.options.viridian_gym_condition > 0:
                return True

            # Celadon Gym not on Cinnabar Island or can access Viridian City gym with one badge
            if not gyms[3] == placed_gyms[6] and world.options.viridian_gym_condition > 1:
                return False

            # At this point we need to see if we can get beyond Pewter/Cinnabar with just one badge

            # Can get Fly access from Pewter City gym and fly beyond Pewter/Cinnabar
            if world.fly_map not in ("Pallet Town", "Viridian City", "Cinnabar Island",
                    "Indigo Plateau") and world.town_map_fly_map not in ("Pallet Town",
                    "Viridian City", "Cinnabar Island", "Indigo Plateau"):
                return False

            # Route 3 condition is boulder badge but Mt Moon entrance leads to safe dungeons or Rock Tunnel
            if world.options.route_3_condition == "boulder_badge" and placed_connecting_interior_dungeons[2] not \
                    in (unsafe_connecting_interior_dungeons[0], unsafe_connecting_interior_dungeons[2]):
                return False

            # Route 3 condition is Defeat Brock and he is in Pewter City, or any other condition besides Boulder Badge.
            # Any badge can land in Pewter City, so the only problematic dungeon at Mt Moon is Seafoam Islands since
            # it requires two badges
            if (((world.options.route_3_condition == "defeat_brock" and gyms[0] == placed_gyms[0])
                    or world.options.route_3_condition not in ("defeat_brock", "boulder_badge"))
                    and placed_connecting_interior_dungeons[2] != unsafe_connecting_interior_dungeons[0]):
                return False

            # If dungeon at Diglett's Cave does not require a badge, we can get Cut access and make it through
            if placed_connecting_interior_dungeons[1] in safe_connecting_interior_dungeons:
                return False

            # If dungeon at Seafoam Islands does not require a badge, we can get Surf access and make it through
            if placed_connecting_interior_dungeons[3] in safe_connecting_interior_dungeons:
                return False

            # No apparent way to proceed, reshuffle
            return True

        # Also check for a very specific situation where Brock or vending machines are needed to access
        # Cerulean City, but they are placed in Cerulean City
        def cerulean_city_problem():
            if (gyms[0] == placed_gyms[1]  # Pewter Gym in Cerulean City
                    and interiors[0] in connecting_interiors[13:17]  # Saffron Gate at Underground Path North South
                    and interiors[13] in connecting_interiors[13:17]  # Saffron Gate at Route 5 Saffron Gate
                    and multi_purpose_dungeons[0] == placed_connecting_interior_dungeons[4]  # Pokémon Mansion at Rock Tunnel, which is
                    and (not world.options.tea)                                         # not traversable backwards
                    and world.options.route_3_condition == "defeat_brock"
                    and world.fly_map != "Cerulean City"
                    and world.town_map_fly_map != "Cerulean City"):
                return True

        while celadon_gym_problem() or cerulean_city_problem():
            world.random.shuffle(placed_gyms)

        connect_interiors(placed_gyms, gym_entrances)

        world.random.shuffle(placed_single_entrance_dungeons)
        while dungeons[4] == placed_single_entrance_dungeons[0]:  # Pokémon Tower at Silph Co
            world.random.shuffle(placed_single_entrance_dungeons)
        connect_interiors(placed_single_entrance_dungeons, single_entrance_dungeon_entrances)

        remaining_entrances = [entrance for entrance in entrances if outdoor_map(entrance.parent_region.name)]
        world.random.shuffle(remaining_entrances)
        remaining_interiors = [entrance for entrance in entrances if entrance not in remaining_entrances]
        for entrance_a, entrance_b in zip(remaining_entrances, remaining_interiors):
            entrance_a.connect(entrance_b)
            entrance_b.connect(entrance_a)
    elif world.options.door_shuffle:
        if world.options.door_shuffle == "full":
            world.random.shuffle(full_interiors)

            def search_for_exit(entrance, region, checked_regions):
                checked_regions.add(region)
                for exit_candidate in region.exits:
                    if ((not exit_candidate.connected_region)
                            and exit_candidate in entrances and exit_candidate is not entrance):
                        return exit_candidate
                for entrance_candidate in region.entrances:
                    if entrance_candidate.parent_region not in checked_regions:
                        found_exit = search_for_exit(entrance, entrance_candidate.parent_region, checked_regions)
                        if found_exit is not None:
                            return found_exit
                return None

            e = multiworld.get_entrance("Underground Path Route 5 to Underground Path North South", player)
            while True:
                for entrance_a in full_interiors:
                    if search_for_exit(entrance_a, entrance_a.parent_region, set()) is None:
                        for entrance_b in full_interiors:
                            if search_for_exit(entrance_b, entrance_b.parent_region, set()):
                                entrance_a.connect(entrance_b)
                                entrance_b.connect(entrance_a)
                                # Yes, it removes from full_interiors while iterating through it, but it immediately
                                # breaks out, from both loops.
                                full_interiors.remove(entrance_a)
                                full_interiors.remove(entrance_b)
                                break
                        else:
                            raise DoorShuffleException("No non-dead end interior sections found in Pokemon Red and Blue door shuffle.")
                        break
                else:
                    break

            loop_out_interiors = []
            world.random.shuffle(entrances)
            for entrance in reversed(entrances):
                if not outdoor_map(entrance.parent_region.name):
                    found_exit = search_for_exit(entrance, entrance.parent_region, set())
                    if found_exit is None:
                        continue
                    loop_out_interiors.append([found_exit, entrance])
                    entrances.remove(entrance)

                    if len(loop_out_interiors) == 2:
                        break

            for entrance_a, entrance_b in zip(full_interiors[:len(full_interiors) // 2],
                                              full_interiors[len(full_interiors) // 2:]):
                entrance_a.connect(entrance_b)
                entrance_b.connect(entrance_a)

        elif world.options.door_shuffle == "interiors":
            loop_out_interiors = [[multiworld.get_entrance(e[0], player), multiworld.get_entrance(e[1], player)] for e
                                  in world.random.sample(unsafe_connecting_interior_dungeons
                                                         + safe_connecting_interior_dungeons, 2)]
            entrances.remove(loop_out_interiors[0][1])
            entrances.remove(loop_out_interiors[1][1])
        if not world.options.badgesanity:
            world.random.shuffle(badges)
            while badges[3].name == "Cascade Badge" and world.options.badges_needed_for_hm_moves:
                world.random.shuffle(badges)
            for badge, loc in zip(badges, badge_locs):
                loc.place_locked_item(badge)

        state = multiworld.state.copy()
        state.allow_partial_entrances = True
        for item, data in item_table.items():
            if (data.id or item in poke_data.pokemon_data) and data.classification == ItemClassification.progression \
                    and ("Badge" not in item or world.options.badgesanity):
                state.collect(world.create_item(item))

        world.random.shuffle(entrances)
        reachable_entrances = []

        relevant_events = [
            "Boulder Badge",
            "Cascade Badge",
            "Thunder Badge",
            "Rainbow Badge",
            "Soul Badge",
            "Marsh Badge",
            "Volcano Badge",
            "Earth Badge",
            "Seafoam Exit Boulder",
            "Victory Road Boulder",
            "Silph Co Liberated",
        ]
        if world.options.robbed_house_officer:
            relevant_events.append("Help Bill")
        if world.options.tea:
            relevant_events.append("Vending Machine Drinks")
        if world.options.route_3_condition == "defeat_brock":
            relevant_events.append("Defeat Brock")
        elif world.options.route_3_condition == "defeat_any_gym":
            relevant_events += [
                "Defeat Brock",
                "Defeat Misty",
                "Defeat Lt. Surge",
                "Defeat Erika",
                "Defeat Koga",
                "Defeat Sabrina",
                "Defeat Blaine",
                "Defeat Viridian Gym Giovanni",
            ]

        event_locations = multiworld.get_filled_locations(player)

        def adds_reachable_entrances(item):

            state_copy = state.copy()
            state_copy.collect(item, True)
            state.sweep_for_advancements(locations=event_locations)
            new_reachable_entrances = len([entrance for entrance in entrances if entrance in reachable_entrances or
                                           entrance.parent_region.can_reach(state_copy)])
            return new_reachable_entrances > len(reachable_entrances)

        def dead_end(e):
            if e.can_reach(state):
                return True
            elif world.options.door_shuffle == "decoupled":
                # Any unreachable exit in decoupled is not a dead end
                return False
            region = e.parent_region
            check_warps = set()
            checked_regions = {region}
            check_warps.update(region.exits)
            check_warps.remove(e)
            for location in region.locations:
                if location.item and location.item.name in relevant_events and \
                                 adds_reachable_entrances(location.item):
                    return False
            while check_warps:
                warp = check_warps.pop()
                warp = warp
                if warp not in reachable_entrances:
                    # confirm warp is in entrances list to ensure it's not a loop-out interior
                    if warp.connected_region is None and warp in entrances:
                        return False
                    elif isinstance(warp, PokemonTCGWarp) or warp.access_rule(state):
                        if warp.connected_region and warp.connected_region not in checked_regions:
                            checked_regions.add(warp.connected_region)
                            check_warps.update(warp.connected_region.exits)
                            for location in warp.connected_region.locations:
                                if (location.item and location.item.name in relevant_events and
                                        adds_reachable_entrances(location.item)):
                                    return False
            return True

        starting_entrances = len(entrances)

        while entrances:
            state.update_reachable_regions(player)
            state.sweep_for_advancements(locations=event_locations)

            world.random.shuffle(entrances)

            if world.options.door_shuffle == "decoupled":
                world.random.shuffle(dc_destinations)
            else:
                entrances.sort(key=lambda e: e.name not in entrance_only)

            reachable_entrances = [entrance for entrance in entrances if entrance in reachable_entrances or
                                   entrance.parent_region.can_reach(state)]

            entrances.sort(key=lambda e: e in reachable_entrances)

            if not reachable_entrances:
                raise DoorShuffleException("Ran out of reachable entrances in Pokemon Red and Blue door shuffle")

            entrance_a = reachable_entrances.pop(0)
            entrances.remove(entrance_a)

            is_outdoor_map = outdoor_map(entrance_a.parent_region.name)

            if world.options.door_shuffle in ("interiors", "full") or len(entrances) != len(reachable_entrances):

                find_dead_end = False
                if (len(reachable_entrances) >
                        (1 if world.options.door_shuffle in ("insanity", "decoupled") else 8) and len(entrances)
                        <= (starting_entrances - 3)):
                    find_dead_end = True

                if (world.options.door_shuffle in ("interiors", "full") and len(entrances) < 48
                        and not is_outdoor_map):
                    # Try to prevent a situation where the only remaining outdoor entrances are ones that cannot be
                    # reached except by connecting directly to it.
                    entrances.sort(key=lambda e: e.name not in unreachable_outdoor_entrances)
                    if entrances[0].name in unreachable_outdoor_entrances and len([entrance for entrance
                            in reachable_entrances if not outdoor_map(entrance.parent_region.name)]) > 1:
                        find_dead_end = True

                if world.options.door_shuffle == "decoupled":
                    destinations = dc_destinations
                elif world.options.door_shuffle in ("interiors", "full"):
                    destinations = [entrance for entrance in entrances if outdoor_map(entrance.parent_region.name) is
                                    not is_outdoor_map]
                    if not destinations:
                        raise DoorShuffleException("Ran out of connectable destinations in Pokemon Red and Blue door shuffle")
                else:
                    destinations = entrances

                destinations.sort(key=lambda e: e == entrance_a)
                for entrance in destinations:
                    if (dead_end(entrance) is find_dead_end and (world.options.door_shuffle != "decoupled"
                                                                 or entrance.parent_region.name.split("-")[0] !=
                                                                 entrance_a.parent_region.name.split("-")[0])):
                        entrance_b = entrance
                        destinations.remove(entrance)
                        break
                else:
                    entrance_b = destinations.pop(0)

                if world.options.door_shuffle in ("interiors", "full"):
                    # on Interiors/Full, the destinations variable does not point to the entrances list, so we need to
                    # remove from that list here.
                    entrances.remove(entrance_b)
            else:
                # Everything is reachable. Just start connecting the rest of the doors at random.
                if world.options.door_shuffle == "decoupled":
                    entrance_b = dc_destinations.pop(0)
                else:
                    entrance_b = entrances.pop(0)

            entrance_a.connect(entrance_b)
            if world.options.door_shuffle != "decoupled":
                entrance_b.connect(entrance_a)

        if world.options.door_shuffle in ("interiors", "full"):
            for pair in loop_out_interiors:
                pair[1].connected_region = pair[0].connected_region
                pair[1].parent_region.entrances.append(pair[0])
                pair[1].target = pair[0].target

    if world.options.door_shuffle:
        for region in multiworld.get_regions(player):
            checked_regions = {region}

            def check_region(region_to_check):
                if "Safari Zone" not in region_to_check.name and outdoor_map(region_to_check.name):
                    return True
                for entrance in region_to_check.entrances:
                    if entrance.parent_region not in checked_regions:
                        checked_regions.add(entrance.parent_region)
                        x = check_region(entrance.parent_region)
                        if x is True:
                            return entrance.name.split(" to ")[1].split("-")[0]
                        elif x is not None:
                            return x
                return None

            if region.name.split("-")[0] not in map_ids or ("Safari Zone" not in region.name and
                                                            outdoor_map(region.name)):
                region.entrance_hint = None
            else:
                region.entrance_hint = check_region(region)


def connect(multiworld: MultiWorld, player: int, source: str, target: str, rule: callable = lambda state: True,
            one_way=False, name=None):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    if name is None:
        name = source + " to " + target

    connection = Entrance(
        player,
        name,
        source_region
    )

    connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
    if not one_way:
        connect(multiworld, player, target, source, rule, True)


class PokemonTCGWarp(Entrance):
    def __init__(self, player, name, parent, warp_id, address, flags):
        super().__init__(player, name, parent)
        self.warp_id = warp_id
        self.address = address
        self.flags = flags
        self.addresses = None
        self.target = None

    def connect(self, entrance):
        super().connect(entrance.parent_region)
        self.addresses = None
        self.target = entrance.warp_id

    def access_rule(self, state):
        if self.connected_region is None:
            return False
        if "Elevator" in self.parent_region.name and (
                (state.multiworld.worlds[self.player].options.all_elevators_locked
                 or "Rocket Hideout" in self.parent_region.name)
                and not state.has("Lift Key", self.player)):
            return False
        return True


class DoorShuffleException(Exception):
    pass


 class PokemonTCGRegion(Region):
     def __init__(self, name, player, multiworld):
         super().__init__(name, player, multiworld)
         self.distance = None
