from random import Random
from typing import Iterable, Dict, Protocol, List, Tuple, Set

from BaseClasses import Region, Entrance
from . import options
from .strings.entrance_names import Entrance
from .strings.region_names import Region
from .region_classes import RegionData, ConnectionData, RandomizationFlag
from .options import StardewOptions
from .mods.mod_regions import ModDataList
from .data.region_data import vanilla_regions
from .data.connection_data import vanilla_connections

vanilla_outside_regions = [Region.farm, Region.town, Region.beach, Region.mountain, Region.forest, Region.bus_stop,
                           Region.backwoods, Region.railroad, Region.desert]


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


def create_final_regions(world_options: StardewOptions) -> List[RegionData]:
    final_regions = []
    final_regions.extend(vanilla_regions)
    if world_options[options.Mods] is None:
        return final_regions
    for mod in world_options[options.Mods]:
        if mod not in ModDataList:
            continue
        for mod_region in ModDataList[mod].regions:
            existing_region = next(
                (region for region in final_regions if region.name == mod_region.name), None)
            if existing_region:
                final_regions.remove(existing_region)
                final_regions.append(existing_region.get_merged_with(mod_region.exits))
                continue

            final_regions.append(mod_region.get_clone())
    return final_regions


def create_final_connections(world_options: StardewOptions) -> List[ConnectionData]:
    final_connections = []
    final_connections.extend(vanilla_connections)
    if world_options[options.Mods] is None:
        return final_connections
    for mod in world_options[options.Mods]:
        if mod not in ModDataList:
            continue
        final_connections.extend(ModDataList[mod].connections)
    return final_connections


def create_regions(region_factory: RegionFactory, random: Random, world_options: StardewOptions) -> Tuple[
    Iterable[Region], Dict[str, str]]:
    final_regions = create_final_regions(world_options)
    regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in
                                  final_regions}
    entrances: Dict[str: Entrance] = {entrance.name: entrance
                                      for region in regions.values()
                                      for entrance in region.exits}

    regions_by_name: Dict[str, RegionData] = {region.name: region for region in final_regions}
    connections, randomized_data = randomize_connections(random, world_options, regions_by_name)

    for connection in connections:
        if connection.name in entrances:
            entrances[connection.name].connect(regions[connection.destination])

    return regions.values(), randomized_data


def randomize_connections(random: Random, world_options: StardewOptions, regions_by_name) -> Tuple[
                            List[ConnectionData], Dict[str, str]]:
    connections_to_randomize = []
    final_connections = create_final_connections(world_options)
    outside_regions = create_outside_regions(world_options)
    connections_by_name: Dict[str, ConnectionData] = {connection.name: connection for connection in final_connections}
    if world_options[options.EntranceRandomization] == options.EntranceRandomization.option_pelican_town:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.PELICAN_TOWN | RandomizationFlag.ENTRANCE in connection.flag]
    elif world_options[options.EntranceRandomization] == options.EntranceRandomization.option_non_progression:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.NON_PROGRESSION | RandomizationFlag.ENTRANCE in connection.flag]
    elif world_options[options.EntranceRandomization] == options.EntranceRandomization.option_buildings:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.BUILDINGS | RandomizationFlag.ENTRANCE in connection.flag]
    elif world_options[options.EntranceRandomization] == options.EntranceRandomization.option_insanity:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.BUILDINGS in connection.flag]
    elif world_options[options.EntranceRandomization] == options.EntranceRandomization.option_chaos:
        connections_to_randomize = [connection for connection in final_connections if
                                    RandomizationFlag.BUILDINGS in connection.flag]
        connections_to_randomize = exclude_island_if_necessary(connections_to_randomize, world_options)

        # On Chaos, we just add the connections to randomize, unshuffled, and the client does it every day
        randomized_data_for_mod = {}
        for connection in connections_to_randomize:
            randomized_data_for_mod[connection.name] = connection.name
            randomized_data_for_mod[connection.reverse] = connection.reverse
        return final_connections, randomized_data_for_mod
    exclude_island = world_options[options.ExcludeGingerIsland] == options.ExcludeGingerIsland.option_true
    if exclude_island:
        connections_to_randomize = [connection for connection in connections_to_randomize if
                                    RandomizationFlag.GINGER_ISLAND not in connection.flag]
    random.shuffle(connections_to_randomize)
    destination_pool = list(connections_to_randomize)
    random.shuffle(destination_pool)

    randomized_connections = randomize_chosen_connections(connections_to_randomize, destination_pool)
    if not world_options[options.EntranceRandomization] == options.EntranceRandomization.option_insanity:
        add_reverse_connections(final_connections, randomized_connections)
    add_non_randomized_connections(final_connections, connections_to_randomize, randomized_connections)
    if world_options[options.EntranceRandomization] == options.EntranceRandomization.option_insanity:
        swap_connections_until_valid_insanity(regions_by_name, connections_by_name, outside_regions,
                                              randomized_connections, connections_to_randomize, random)
    else:
        swap_connections_until_valid(regions_by_name, connections_by_name, outside_regions, randomized_connections,
                                     connections_to_randomize, random)
    randomized_connections_for_generation = create_connections_for_generation(randomized_connections)
    if world_options[options.EntranceRandomization] == options.EntranceRandomization.option_insanity:
        randomized_data_for_mod = create_data_for_mod_insanity(randomized_connections, connections_to_randomize)
    else:
        randomized_data_for_mod = create_data_for_mod(randomized_connections, connections_to_randomize)

    return randomized_connections_for_generation, randomized_data_for_mod


def exclude_island_if_necessary(connections_to_randomize: List[ConnectionData], world_options) -> List[ConnectionData]:
    exclude_island = world_options[options.ExcludeGingerIsland] == options.ExcludeGingerIsland.option_true
    if exclude_island:
        connections_to_randomize = [connection for connection in connections_to_randomize if
                                    RandomizationFlag.GINGER_ISLAND not in connection.flag]
    return connections_to_randomize


def randomize_chosen_connections(connections_to_randomize: List[ConnectionData],
                                 destination_pool: List[ConnectionData]) -> Dict[ConnectionData, ConnectionData]:
    randomized_connections = {}
    for connection in connections_to_randomize:
        destination = destination_pool.pop()
        randomized_connections[connection] = destination
    return randomized_connections


def create_connections_for_generation(randomized_connections: Dict[ConnectionData, ConnectionData]) -> List[
    ConnectionData]:
    connections = []
    for connection in randomized_connections:
        destination = randomized_connections[connection]
        connections.append(ConnectionData(connection.name, destination.destination, destination.reverse))
    return connections


def create_data_for_mod(randomized_connections: Dict[ConnectionData, ConnectionData],
                        connections_to_randomize: List[ConnectionData]) -> Dict[str, str]:
    randomized_data_for_mod = {}
    for connection in randomized_connections:
        if connection not in connections_to_randomize:
            continue
        destination = randomized_connections[connection]
        add_to_mod_data(connection, destination, randomized_data_for_mod)
    return randomized_data_for_mod


def add_to_mod_data(connection: ConnectionData, destination: ConnectionData, randomized_data_for_mod: Dict[str, str]):
    randomized_data_for_mod[connection.name] = destination.name
    randomized_data_for_mod[destination.reverse] = connection.reverse


def add_non_randomized_connections(connections, connections_to_randomize: List[ConnectionData],
                                   randomized_connections: Dict[ConnectionData, ConnectionData]):
    for connection in connections:
        if connection in connections_to_randomize:
            continue
        randomized_connections[connection] = connection


def swap_connections_until_valid(regions_by_name, connections_by_name, outside_region,
                                 randomized_connections: Dict[ConnectionData, ConnectionData],
                                 connections_to_randomize: List[ConnectionData], random: Random):
    while True:
        reachable_regions, unreachable_regions = find_reachable_regions(regions_by_name, connections_by_name,
                                                                        outside_region, randomized_connections)
        if not unreachable_regions:
            return randomized_connections
        swap_one_connection(regions_by_name, connections_by_name, randomized_connections, reachable_regions,
                            unreachable_regions, connections_to_randomize, random)


def find_reachable_regions(regions_by_name, connections_by_name, outside_regions,
                           randomized_connections: Dict[ConnectionData, ConnectionData]):
    connections = {}
    for connection in randomized_connections:
        connections[connection] = connection
    reachable_regions = {Region.menu}
    unreachable_regions = {region for region in regions_by_name.keys()}
    unreachable_regions.remove(Region.menu)
    exits_to_explore = list(regions_by_name[Region.menu].exits)
    item_exits = list()
    found_outside = False

    while exits_to_explore:
        exit_name = exits_to_explore.pop()
        exit_connection = connections_by_name[exit_name]
        replaced_connection = randomized_connections[exit_connection]
        target_region_name = replaced_connection.destination
        if target_region_name in reachable_regions:
            continue

        if RandomizationFlag.ITEMLESS_ENTRANCE in exit_connection.flag or found_outside:
            target_region = regions_by_name[target_region_name]
            reachable_regions.add(target_region_name)
            unreachable_regions.remove(target_region_name)
            exits_to_explore.extend(target_region.exits)
            if target_region_name in outside_regions:
                found_outside = True
        else:
            item_exits.extend([exit_name])

    while item_exits and found_outside:
        exit_name = item_exits.pop()
        exit_connection = connections_by_name[exit_name]
        replaced_connection = connections[exit_connection]
        target_region_name = replaced_connection.destination
        if target_region_name in reachable_regions:
            continue

        target_region = regions_by_name[target_region_name]
        reachable_regions.add(target_region_name)
        unreachable_regions.remove(target_region_name)
        item_exits.extend(target_region.exits)

    return reachable_regions, unreachable_regions


def swap_one_connection(regions_by_name, connections_by_name,
                        randomized_connections: Dict[ConnectionData, ConnectionData],
                        reachable_regions: Set[str], unreachable_regions: Set[str],
                        connections_to_randomize: List[ConnectionData], random: Random):
    randomized_connections_already_shuffled = {connection: randomized_connections[connection]
                                               for connection in randomized_connections
                                               if connection != randomized_connections[connection]}
    unreachable_regions_names_leading_somewhere = tuple([region for region in unreachable_regions
                                                         if len(regions_by_name[region].exits) > 0])
    unreachable_regions_leading_somewhere = [regions_by_name[region_name] for region_name in
                                             unreachable_regions_names_leading_somewhere]
    unreachable_regions_exits_names = [exit_name for region in unreachable_regions_leading_somewhere for exit_name in
                                       region.exits]
    unreachable_connections = [connections_by_name[exit_name] for exit_name in unreachable_regions_exits_names]
    unreachable_connections_that_can_be_randomized = [connection for connection in unreachable_connections if
                                                      connection in connections_to_randomize]

    chosen_unreachable_entrance = random.choice(unreachable_connections_that_can_be_randomized)

    chosen_reachable_entrance = None
    while chosen_reachable_entrance is None or chosen_reachable_entrance not in randomized_connections_already_shuffled:
        chosen_reachable_region_name = random.choice(tuple(reachable_regions))
        chosen_reachable_region = regions_by_name[chosen_reachable_region_name]
        if not any(chosen_reachable_region.exits):
            continue
        chosen_reachable_entrance_name = random.choice(chosen_reachable_region.exits)
        chosen_reachable_entrance = connections_by_name[chosen_reachable_entrance_name]

    reachable_destination = randomized_connections[chosen_reachable_entrance]
    unreachable_destination = randomized_connections[chosen_unreachable_entrance]
    randomized_connections[chosen_reachable_entrance] = unreachable_destination
    randomized_connections[chosen_unreachable_entrance] = reachable_destination


def add_reverse_connections(connections, randomized_connections: Dict[ConnectionData, ConnectionData]):
    reversed_connections = {}
    for key, value in randomized_connections.items():
        reverse = find_reversed_connection(connections, value)
        reverse_key = find_reversed_connection(connections, key)
        reversed_connections[reverse] = reverse_key
    return reversed_connections


def find_reversed_connection(connections, connection: ConnectionData):
    for reversed in connections:
        if connection.reverse == reversed.name:
            return reversed


def create_data_for_mod_insanity(randomized_connections: Dict[ConnectionData, ConnectionData],
                                 connections_to_randomize: List[ConnectionData]) -> Dict[str, str]:
    randomized_data_for_mod = {}
    for connection in randomized_connections:
        if connection not in connections_to_randomize:
            continue
        destination = randomized_connections[connection]
        randomized_data_for_mod[connection.name] = destination.name
    return randomized_data_for_mod


def swap_connections_until_valid_insanity(regions_by_name, connections_by_name, outside_regions,
                                          randomized_connections: Dict[ConnectionData, ConnectionData],
                                          connections_to_randomize: List[ConnectionData], random: Random):
    while True:
        reachable_regions, unreachable_regions = find_reachable_regions(regions_by_name, connections_by_name,
                                                                        outside_regions, randomized_connections)
        print(unreachable_regions)
        if not unreachable_regions and not has_self_connection(randomized_connections):
            return randomized_connections
        if unreachable_regions:
            swap_one_connection_insanity(regions_by_name, connections_by_name, randomized_connections, reachable_regions,
                                unreachable_regions, connections_to_randomize, random)
        swap_self_connections(randomized_connections, random)


def swap_one_connection_insanity(regions_by_name, connections_by_name,
                        randomized_connections: Dict[ConnectionData, ConnectionData],
                        reachable_regions: Set[str], unreachable_regions: Set[str],
                        connections_to_randomize: List[ConnectionData], random: Random):
    randomized_connections_already_shuffled = {connection: randomized_connections[connection]
                                               for connection in randomized_connections
                                               if connection != randomized_connections[connection]}
    unreachable_connections = [connection for connection in connections_to_randomize if
                               connection.destination in unreachable_regions]
    unreachable_connections_that_can_be_randomized = [connection for connection in unreachable_connections if
                                                      connection in connections_to_randomize]

    chosen_unreachable_entrance = random.choice(unreachable_connections_that_can_be_randomized)

    chosen_reachable_entrance = random.choice(connections_to_randomize)

    reachable_destination = randomized_connections[chosen_reachable_entrance]
    unreachable_destination = randomized_connections[chosen_unreachable_entrance]
    randomized_connections[chosen_reachable_entrance] = unreachable_destination
    randomized_connections[chosen_unreachable_entrance] = reachable_destination


def swap_self_connections(randomized_connections: Dict[ConnectionData, ConnectionData], random: Random):
    for origin, destination in randomized_connections.items():
        if not RandomizationFlag.BUILDINGS in origin.flag:
            continue
        if origin.reverse == destination.name:
            new_origin, new_destination = random.choice(list(randomized_connections.items()))
            while not RandomizationFlag.BUILDINGS in new_origin.flag:
                new_origin, new_destination = random.choice(list(randomized_connections.items()))
            randomized_connections[origin] = new_destination
            randomized_connections[new_origin] = destination


def has_self_connection(randomized_connections: Dict[ConnectionData, ConnectionData]):
    for origin, destination in randomized_connections.items():
        if origin.reverse == destination.name and RandomizationFlag.BUILDINGS in origin.flag:
            return True
    return False


def create_outside_regions(world_options: StardewOptions) -> List[RegionData]:
    outside_regions = []
    outside_regions.extend(vanilla_outside_regions)
    if world_options[options.Mods] is None:
        return outside_regions
    for mod in world_options[options.Mods]:
        if mod not in ModDataList:
            continue
        if ModDataList[mod].outside_regions:
            outside_regions.extend(ModDataList[mod].outside_regions)

    return outside_regions
