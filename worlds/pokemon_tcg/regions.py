from copy import deepcopy
from BaseClasses import MultiWorld, Region, Entrance, LocationProgressType, ItemClassification
from .items import item_table, item_groups
from .locations import location_data, PokemonTCGLocation
from . import logic
from . import poke_data

map_ids = {
    "Overworld": 0x01,
    "Mason Laboratory Center Room": 0x02,
    "Mason Laboratory Right Room": 0x03,
    "Ishihara's House": 0x04,
    "Water Club Lobby": 0x05,
    "Water Club Lounge": 0x06,
    "Water Club Main Hall": 0x07,
    "Fire Club Lobby": 0x08,
    "Fire Club Lounge": 0x09,
    "Fire Club Main Hall": 0x0A,
    "Lightning Club Lobby": 0x0B,
    "Lightning Club Lounge": 0x0C,
    "Lightning Club Main Hall": 0x0D,
    "Grass Club Lobby": 0x0E,
    "Grass Club Lounge": 0x10,
    "Grass Club Main Hall": 0x11,
    "Rock Club Lobby": 0x12,
    "Rock Club Lounge": 0x13,
    "Rock Club Main Hall": 0x14,
    "Fighting Club Lobby": 0x15,
    "Fighting Club Lounge": 0x16,
    "Fighting Club Main Hall": 0x17,
    "Psychic Club Lobby": 0x18,
    "Psychic Club Lounge": 0x19,
    "Psychic Club Main Hall": 0x1A,
    "Science Club Lobby": 0x1B,
    "Science Club Lounge": 0x1C,
    "Science Club Main Hall": 0x1D,
    "Challenge Hall Lobby": 0x1E,
    "Challenge Hall Lounge": 0x20,
    "Challenge Hall Main Hall": 0x21,
    "Pokemon Dome Lobby": 0x22,
    "Pokemon Dome Main Hall": 0x23,
    "Pokemon Dome Hall of Honor": 0x24,
}

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

def is_pack(original_item):
    return original_item in "Energy Pack", "Mystery Pack", "Laboratory Pack", "Colosseum Pack", "Evolution Pack"

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
            if location.event:
                location_object.place_locked_item(location.item)
            elif world.options.pack_type and is_pack(location.original_item):
                world.item_pool.append(world.create_item(world.next_evoline))
            else:
                world.item_pool.append(world.create_item(location.original_item))

    world.random.shuffle(world.item_pool)

    regions = [create_region(multiworld, player, region, locations_per_region) for region in warp_data]
    multiworld.regions += regions
    if __debug__:
        for region in locations_per_region:
            assert not locations_per_region[region], f"locations not assigned to region {region}"

    connect(multiworld, player, "Menu", "Mason Laboratory Center Room", one_way=True)
    connect(multiworld, player, "Mason Laboratory Center Room", "Overworld")
    connect(multiworld, player, "Mason Laboratory Center Room", "Mason Laboratory Right Room")
    connect(multiworld, player, "Overworld", "Ishihara's House")
    connect(multiworld, player, "Overworld", "Water Club Lobby")
    connect(multiworld, player, "Water Club Lobby", "Water Club Lounge")
    connect(multiworld, player, "Water Club Lobby", "Water Club Main Hall", lambda state: logic.has_item(state, world.options.water_club_unlock))
    connect(multiworld, player, "Overworld", "Fire Club Lobby")
    connect(multiworld, player, "Fire Club Lobby", "Fire Club Lounge")
    connect(multiworld, player, "Fire Club Lobby", "Fire Club Main Hall", lambda state: logic.has_item(state, world.options.fire_club_unlock))
    connect(multiworld, player, "Overworld", "Lightning Club Lobby")
    connect(multiworld, player, "Lightning Club Lobby", "Lightning Club Lounge")
    connect(multiworld, player, "Lightning Club Lobby", "Lightning Club Main Hall", lambda state: logic.has_item(state, world.options.lightning_club_unlock))
    connect(multiworld, player, "Overworld", "Grass Club Lobby")
    connect(multiworld, player, "Grass Club Lobby", "Grass Club Lounge")
    connect(multiworld, player, "Grass Club Lobby", "Grass Club Main Hall", lambda state: logic.has_item(state, world.options.grass_club_unlock))
    connect(multiworld, player, "Overworld", "Rock Club Lobby")
    connect(multiworld, player, "Rock Club Lobby", "Rock Club Lounge")
    connect(multiworld, player, "Rock Club Lobby", "Rock Club Main Hall", lambda state: logic.has_item(state, world.options.rock_club_unlock))
    connect(multiworld, player, "Overworld", "Fighting Club Lobby")
    connect(multiworld, player, "Fighting Club Lobby", "Fighting Club Lounge")
    connect(multiworld, player, "Fighting Club Lobby", "Fighting Club Main Hall", lambda state: logic.has_item(state, world.options.fighting_club_unlock))
    connect(multiworld, player, "Overworld", "Psychic Club Lobby")
    connect(multiworld, player, "Psychic Club Lobby", "Psychic Club Lounge")
    connect(multiworld, player, "Psychic Club Lobby", "Psychic Club Main Hall", lambda state: logic.has_item(state, world.options.psychic_club_unlock))
    connect(multiworld, player, "Overworld", "Science Club Lobby")
    connect(multiworld, player, "Science Club Lobby", "Science Club Lounge")
    connect(multiworld, player, "Science Club Lobby", "Science Club Main Hall", lambda state: logic.has_item(state, world.options.science_club_unlock))
    connect(multiworld, player, "Overworld", "Pokemon Dome Lobby")
    connect(multiworld, player, "Pokemon Dome Lobby", "Pokemon Dome Main Hall", lambda state: logic.medal_count(state) >= world.options.grand_master_medal_count)
    connect(multiworld, player, "Pokemon Dome Main Hall", "Pokemon Dome Hall of Honor", lambda state: state.has("Become Champion"))


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

 class PokemonTCGRegion(Region):
     def __init__(self, name, player, multiworld):
         super().__init__(name, player, multiworld)
         self.distance = None
