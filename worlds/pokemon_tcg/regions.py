from copy import deepcopy
from BaseClasses import MultiWorld, Region, Entrance, LocationProgressType, ItemClassification
from .items import item_table, item_groups, evoline_pack_list, vanilla_items
from .locations import location_data, PokemonTCGLocation
from . import logic

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
    "Grass Club Lounge": 0x0F,
    "Grass Club Main Hall": 0x10,
    "Rock Club Lobby": 0x11,
    "Rock Club Lounge": 0x12,
    "Rock Club Main Hall": 0x13,
    "Fighting Club Lobby": 0x14,
    "Fighting Club Lounge": 0x15,
    "Fighting Club Main Hall": 0x16,
    "Psychic Club Lobby": 0x17,
    "Psychic Club Lounge": 0x18,
    "Psychic Club Main Hall": 0x9A,
    "Science Club Lobby": 0x1A,
    "Science Club Lounge": 0x1B,
    "Science Club Main Hall": 0x1C,
    "Challenge Hall Lobby": 0x1D,
    "Challenge Hall Lounge": 0x1E,
    "Challenge Hall Main Hall": 0x1F,
    "Pokemon Dome Lobby": 0x20,
    "Pokemon Dome Main Hall": 0x21,
    "Pokemon Dome Hall of Honor": 0x22,
}

warp_data = {
    'Menu': [],
    'Overworld': [],
    'Mason Laboratory Center Room': [],
    'Mason Laboratory Right Room': [],
    'Ishihara\'s House': [],
    'Water Club Lobby': [],
    'Water Club Lounge': [],
    'Water Club Main Hall': [],
    'Fire Club Lobby': [],
    'Fire Club Lounge': [],
    'Fire Club Main Hall': [],
    'Lightning Club Lobby': [],
    'Lightning Club Lounge': [],
    'Lightning Club Main Hall': [],
    'Grass Club Lobby': [],
    'Grass Club Lounge': [],
    'Grass Club Main Hall': [],
    'Rock Club Lobby': [],
    'Rock Club Lounge': [],
    'Rock Club Main Hall': [],
    'Fighting Club Lobby': [],
    'Fighting Club Lounge': [],
    'Fighting Club Main Hall': [],
    'Psychic Club Lobby': [],
    'Psychic Club Lounge': [],
    'Psychic Club Main Hall': [],
    'Science Club Lobby': [],
    'Science Club Lounge': [],
    'Science Club Main Hall': [],
    'Challenge Hall Lobby': [],
    'Challenge Hall Lounge': [],
    'Challenge Hall Main Hall': [],
    'Pokemon Dome Lobby': [],
    'Pokemon Dome Main Hall': [],
    'Pokemon Dome Hall of Honor': [],
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
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))
    locations_per_region[name] = []
    return ret


def is_vanilla_pack(original_item):
    return original_item in vanilla_items


def next_evoline(evoline_index: int):
    if evoline_index >= len(evoline_pack_list):
        return "Energy Pack"
    return evoline_pack_list[evoline_index]


def create_regions(world):
    multiworld = world.multiworld
    player = world.player
    locations_per_region = {}

    start_inventory = world.options.start_inventory.value.copy()
    evoline_index = 0

    for location in location_data:
        locations_per_region.setdefault(location.region, [])
        # The check for list is so that we don't try to check the item table with a list as a key
        if location.inclusion(world, player):
            location_object = PokemonTCGLocation(player, location.name, location.address, location.rom_address)
            locations_per_region[location.region].append(location_object)
            if location.event:
                location_object.place_locked_item(world.create_item(location.original_item))
            elif world.options.pack_type and is_vanilla_pack(location.original_item):
                world.item_pool.append(world.create_item(next_evoline(evoline_index)))
                evoline_index += 1
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
    print(world.options.water_club_unlock.value)
    connect(multiworld, player, "Water Club Lobby", "Water Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.water_club_unlock.value))
    connect(multiworld, player, "Overworld", "Fire Club Lobby")
    connect(multiworld, player, "Fire Club Lobby", "Fire Club Lounge")
    print(world.options.fire_club_unlock.value)
    connect(multiworld, player, "Fire Club Lobby", "Fire Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.fire_club_unlock.value))
    connect(multiworld, player, "Overworld", "Lightning Club Lobby")
    connect(multiworld, player, "Lightning Club Lobby", "Lightning Club Lounge")
    print(world.options.lightning_club_unlock.value)
    connect(multiworld, player, "Lightning Club Lobby", "Lightning Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.lightning_club_unlock.value))
    connect(multiworld, player, "Overworld", "Grass Club Lobby")
    connect(multiworld, player, "Grass Club Lobby", "Grass Club Lounge")
    print(world.options.grass_club_unlock.value)
    connect(multiworld, player, "Grass Club Lobby", "Grass Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.grass_club_unlock.value))
    connect(multiworld, player, "Overworld", "Rock Club Lobby")
    connect(multiworld, player, "Rock Club Lobby", "Rock Club Lounge")
    print(world.options.rock_club_unlock.value)
    connect(multiworld, player, "Rock Club Lobby", "Rock Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.rock_club_unlock.value))
    connect(multiworld, player, "Overworld", "Fighting Club Lobby")
    connect(multiworld, player, "Fighting Club Lobby", "Fighting Club Lounge")
    print(world.options.fighting_club_unlock.value)
    connect(multiworld, player, "Fighting Club Lobby", "Fighting Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.fighting_club_unlock.value))
    connect(multiworld, player, "Overworld", "Psychic Club Lobby")
    connect(multiworld, player, "Psychic Club Lobby", "Psychic Club Lounge")
    print(world.options.psychic_club_unlock.value)
    connect(multiworld, player, "Psychic Club Lobby", "Psychic Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.psychic_club_unlock.value))
    connect(multiworld, player, "Overworld", "Science Club Lobby")
    connect(multiworld, player, "Science Club Lobby", "Science Club Lounge")
    print(world.options.science_club_unlock.value)
    connect(multiworld, player, "Science Club Lobby", "Science Club Main Hall",
            lambda state: logic.has_item(state, world, player, world.options.science_club_unlock.value))
    connect(multiworld, player, "Overworld", "Pokemon Dome Lobby")
    connect(multiworld, player, "Pokemon Dome Lobby", "Pokemon Dome Main Hall",
            lambda state: logic.medal_count(state, world, player) >= world.options.grand_master_medal_count.value)
    connect(multiworld, player, "Pokemon Dome Main Hall", "Pokemon Dome Hall of Honor",
            lambda state: state.has("Become Champion", player))


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
