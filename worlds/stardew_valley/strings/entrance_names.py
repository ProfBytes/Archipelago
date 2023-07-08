def dig_to_mines_floor(floor: int) -> str:
    return f"Dig to The Mines - Floor {floor}"


def dig_to_skull_floor(floor: int) -> str:
    return f"Mine to Skull Cavern Floor {floor}"


def move_to_woods_depth(depth: int) -> str:
    return f"Enter Deep Woods Depth {depth}"


class Entrance:
    # Menus
    to_stardew_valley = "To Stardew Valley"
    to_farmhouse = "To Farmhouse"

    # Farmhouse Entrances
    farmhouse_to_farm = "Farmhouse to Farm"
    downstairs_to_cellar = "Farmhouse to Cellar"
    cellar_to_upstairs = "Cellar to Farmhouse"

    # Farm Entrances
    farm_to_farmhouse = "Farm to Farmhouse"
    farm_to_backwoods = "Farm to Backwoods"
    farm_to_bus_stop = "Farm to Bus Stop"
    farm_to_forest = "Farm to Forest"
    farm_to_farmcave = "Farm to Farmcave"
    enter_greenhouse = "Farm to Greenhouse"
    use_desert_obelisk = "Use Desert Obelisk"
    use_island_obelisk = "Use Island Obelisk"
    use_farm_obelisk = "Use Farm Obelisk"

    # Misc. Entrances on Farm
    farmcave_to_farm = "Farmcave to Farm"
    leave_greenhouse = "Greenhouse to Farm"

    # Bus Stop Entrances
    bus_stop_to_farm = "Bus Stop to Farm"
    bus_stop_to_tunnel_entrance = "Bus Stop to Tunnel Entrance"
    bus_stop_to_town = "Bus Stop to Town"
    take_bus_to_desert = "Bus Stop to Desert"

    # Tunnel and Backwoods Entrances
    tunnel_entrance_to_bus_tunnel = "Tunnel Entrance to Bus Tunnel"
    leave_tunnel = "Bus Tunnel to Tunnel Entrance"
    tunnel_entrance_to_bus_stop = "Tunnel Entrance to Bus Stop"
    backwoods_to_mountain = "Backwoods to Mountain"
    backwoods_to_farm = "Backwoods to Farm"

    # Forest Entrances
    forest_to_farm = "Forest to Farm"
    forest_to_town = "Forest to Town"
    enter_secret_woods = "Forest to Secret Woods"
    forest_to_wizard_tower = "Forest to Wizard Tower"
    forest_to_marnie_ranch = "Forest to Marnie's Ranch"
    forest_to_leah_cottage = "Forest to Leah's Cottage"
    forest_to_sewer = "Forest to Sewer"
    buy_from_traveling_merchant = "Buy from Traveling Merchant"

    # Misc. Entrances in Forest
    leave_secret_woods = "Secret Woods to Forest"
    enter_wizard_basement = "Wizard Tower to Wizard Basement"
    leave_wizard_basement = "Wizard Basement to Wizard Tower"
    wizard_tower_to_forest = "Wizard Tower to Forest"
    marnie_ranch_to_forest = "Marnie's Ranch to Forest"
    leah_cottage_to_forest = "Leah's Cottage to Forest"

    # Mountain Entrances
    mountain_to_backwoods = "Mountain to Backwoods"
    mountain_to_railroad = "Mountain to Railroad"
    mountain_to_tent = "Mountain to Tent"
    mountain_to_carpenter_shop = "Mountain to Carpenter Shop"
    mountain_to_maru_room = "Mountain to Maru's Room"
    mountain_to_the_mines = "Mountain to The Mines"
    enter_quarry = "Mountain to Quarry"
    mountain_to_adventurer_guild = "Mountain to Adventurer's Guild"
    mountain_to_town = "Mountain to Town"
    mountain_to_leo_treehouse = "Mountain to Leo's TreeHouse"

    # Misc. Entrances in Mountain
    tent_to_mountain = "Tent to Mountain"
    carpenter_shop_to_mountain= "Carpenter Shop to Mountain"
    maru_room_to_mountain = "Maru's Room to Mountain"
    carpenter_to_maru_room = "Carpenter to Maru's Room"
    maru_room_to_carpenter = "Maru's Room to Carpenter"
    the_mines_to_mountain = "The Mines to Mountain"
    leave_quarry = "Quarry to Mountain"
    adventurer_guild_to_mountain = "Adventurer's Guild to Mountain"
    leo_treehouse_to_mountain = "Leo's TreeHouse to Mountain"

    # Town Entrances
    town_to_forest = "Town to Forest"
    town_to_bus_stop = "Town to Bus Stop"
    town_to_mountain = "Town to Mountain"
    town_to_community_center = "Town to Community Center"
    town_to_beach = "Town to Beach"
    town_to_hospital = "Town to Hospital"
    town_to_pierre_general_store = "Town to Pierre's General Store"
    town_to_saloon = "Town to Saloon"
    town_to_alex_house = "Town to Alex's House"
    town_to_trailer = "Town to Trailer"
    town_to_mayor_manor = "Town to Mayor's Manor"
    town_to_sam_house = "Town to Sam's House"
    town_to_haley_house = "Town to Haley's House"
    town_to_sewer = "Town to Sewer"
    town_to_clint_blacksmith = "Town to Clint's Blacksmith"
    town_to_museum = "Town to Museum"
    town_to_jojamart = "Town to JojaMart"

    # Misc. Entrances in Town
    community_center_to_town = "Community Center to Town"
    hospital_to_town = "Hospital to Town"
    pierre_general_store_to_town = "Pierre's General Store to Town"
    saloon_to_town = "Saloon to Town"
    alex_house_to_town = "Alex's House to Town"
    trailer_to_town = "Trailer to Town"
    mayor_manor_to_town = "Mayor's Manor to Town"
    sam_house_to_town = "Sam's House to Town"
    haley_house_to_town = "Haley's House to Town"
    clint_blacksmith_to_town = "Clint's Blacksmith to Town"
    museum_to_town = "Museum to Town"
    jojamart_to_town = "JojaMart to Town"

    # Community Center Bundles
    access_crafts_room = "Access Crafts Room"
    access_pantry = "Access Pantry"
    access_fish_tank = "Access Fish Tank"
    access_boiler_room = "Access Boiler Room"
    access_bulletin_board = "Access Bulletin Board"
    access_vault = "Access Vault"

    # Beach Entrances
    beach_to_town = "Beach to Town"
    beach_to_willy_fish_shop = "Beach to Willy's Fish Shop"
    enter_elliott_house = "Beach to Elliott's House"
    enter_tide_pools = "Beach to Tide Pools"

    # Misc. Entrances on Beach
    willy_fish_shop_to_beach = "Willy's Fish Shop to Beach"
    fish_shop_to_boat_tunnel = "Willy's Fish Shop to Boat Tunnel"
    boat_tunnel_to_fish_shop = "Boat Tunnel to Willy's Fish Shop"
    leave_elliott_house = "Elliott's House to Beach"
    boat_to_ginger_island = "Take the Boat to Ginger Island"

    # Railroad Entrances
    railroad_to_mountain = "Railroad to Mountain"
    enter_bathhouse_entrance = "Railroad to Bathhouse Entrance"
    leave_bathhouse = "Bathhouse Entrance to Railroad"
    enter_witch_warp_cave = "Railroad to Witch Warp Cave"
    leave_witch_warp_cave = "Witch Warp Cave to Railroad"
    enter_perfection_cutscene_area = "Railroad to Perfection Cutscene Area"
    leave_perfection_cutscene_area = "Perfection Cutscene Area to Railroad"
    enter_locker_room = "Bathhouse Entrance to Locker Room"
    leave_locker_room = "Locker Room to Bathhouse Entrance"
    enter_public_bath = "Locker Room to Public Bath"
    leave_public_bath = "Public Bath to Locker Room"
    enter_witch_swamp = "Witch Warp Cave to Witch's Swamp"
    leave_witch_swamp = "Witch's Swamp to Witch Warp Cave"
    enter_witch_hut = "Witch's Swamp to Witch's Hut"
    leave_witch_hut = "Witch's Hut to Witch's Swamp"
    witch_warp_to_wizard_basement = "Witch's Hut to Wizard Basement"
    wizard_basement_to_witch_warp = "Wizard Basement to Witch's Hut"

    # Friendship locked Entrances
    enter_sebastian_room = "Carpenter Shop to Sebastian's Room"
    leave_sebastian_room = "Sebastian's Room to Carpenter Shop"
    enter_harvey_room = "Hospital to Harvey's Room"
    leave_harvey_room = "Harvey's Room to Hospital"
    enter_sunroom = "Pierre's General Store to Sunroom"
    leave_sunroom = "Sunroom to Pierre's General Store"

    # Sewers Entrances
    enter_mutant_bug_lair = "Sewer to Mutant Bug Lair"
    leave_mutant_bug_lair = "Mutant Bug Lair to Sewer"
    sewers_to_forest = "Sewer to Forest"
    sewers_to_town = "Sewer to Town"

    # Arcade Machine
    play_journey_of_the_prairie_king = "Play Journey of the Prairie King"
    reach_jotpk_world_2 = "Reach JotPK World 2"
    reach_jotpk_world_3 = "Reach JotPK World 3"
    play_junimo_kart = "Play Junimo Kart"
    reach_junimo_kart_2 = "Reach Junimo Kart 2"
    reach_junimo_kart_3 = "Reach Junimo Kart 3"

    # Quarry Entrances
    enter_quarry_mine_entrance = "Quarry to Quarry Mine Entrance"
    leave_quarry_mine_entrance = "Quarry Mine Entrance to Quarry"
    enter_quarry_mine = "Quarry Mine Entrance to Quarry Mine"
    leave_quarry_mine = "Quarry Mine to Quarry Mine Entrance"

    # Desert Entrances
    take_bus_to_town = "Desert to Bus Stop"
    enter_oasis = "Desert to Oasis"
    leave_oasis = "Oasis to Desert"
    enter_skull_cavern_entrance = "Desert to Skull Cavern Entrance"
    leave_skull_cavern_entrance = "Skull Cavern Entrance to Desert"
    enter_casino = "Oasis to Casino"
    leave_casino = "Casino to Oasis"

    # Skull Cavern
    enter_skull_cavern = "Skull Cavern Entrance to Skull Cavern"
    mine_to_skull_cavern_floor_25 = dig_to_skull_floor(25)
    mine_to_skull_cavern_floor_50 = dig_to_skull_floor(50)
    mine_to_skull_cavern_floor_75 = dig_to_skull_floor(75)
    mine_to_skull_cavern_floor_100 = dig_to_skull_floor(100)
    mine_to_skull_cavern_floor_125 = dig_to_skull_floor(125)
    mine_to_skull_cavern_floor_150 = dig_to_skull_floor(150)
    mine_to_skull_cavern_floor_175 = dig_to_skull_floor(175)
    mine_to_skull_cavern_floor_200 = dig_to_skull_floor(200)

    # Mines
    talk_to_mines_dwarf = "Talk to Mines Dwarf"
    dig_to_mines_floor_5 = dig_to_mines_floor(5)
    dig_to_mines_floor_10 = dig_to_mines_floor(10)
    dig_to_mines_floor_15 = dig_to_mines_floor(15)
    dig_to_mines_floor_20 = dig_to_mines_floor(20)
    dig_to_mines_floor_25 = dig_to_mines_floor(25)
    dig_to_mines_floor_30 = dig_to_mines_floor(30)
    dig_to_mines_floor_35 = dig_to_mines_floor(35)
    dig_to_mines_floor_40 = dig_to_mines_floor(40)
    dig_to_mines_floor_45 = dig_to_mines_floor(45)
    dig_to_mines_floor_50 = dig_to_mines_floor(50)
    dig_to_mines_floor_55 = dig_to_mines_floor(55)
    dig_to_mines_floor_60 = dig_to_mines_floor(60)
    dig_to_mines_floor_65 = dig_to_mines_floor(65)
    dig_to_mines_floor_70 = dig_to_mines_floor(70)
    dig_to_mines_floor_75 = dig_to_mines_floor(75)
    dig_to_mines_floor_80 = dig_to_mines_floor(80)
    dig_to_mines_floor_85 = dig_to_mines_floor(85)
    dig_to_mines_floor_90 = dig_to_mines_floor(90)
    dig_to_mines_floor_95 = dig_to_mines_floor(95)
    dig_to_mines_floor_100 = dig_to_mines_floor(100)
    dig_to_mines_floor_105 = dig_to_mines_floor(105)
    dig_to_mines_floor_110 = dig_to_mines_floor(110)
    dig_to_mines_floor_115 = dig_to_mines_floor(115)
    dig_to_mines_floor_120 = dig_to_mines_floor(120)

    # Island Entrances
    boat_to_boat_tunnel = "Take the Boat to Boat Tunnel"
    island_south_to_west = "Island South to West"
    island_south_to_north = "Island South to North"
    island_south_to_east = "Island South to East"
    island_south_to_southeast = "Island South to Southeast"

    use_island_resort = "Use Island Resort"

    island_west_to_south = "Island West to Island South"
    island_west_to_islandfarmhouse = "Island West to Island Farmhouse"
    island_west_to_gourmand_cave = "Island West to Gourmand Cave"
    island_west_to_crystals_cave = "Island West to Crystal Cave"
    island_west_to_shipwreck = "Island West to Shipwreck"
    island_west_to_qi_walnut_room = "Island West to Qi Walnut Room"

    islandfarmhouse_to_west = "Island Farmhouse to Island West"
    gourmand_cave_to_island_west = "Gourmand Cave to Island West"
    crystals_cave_to_island_west = "Crystal Cave to Island West"
    shipwreck_to_island_west = "Shipwreck to Island West"
    qi_walnut_room_to_island_west = "Qi Walnut Room to Island West"

    island_east_to_south = "Island East to Island South"
    island_east_to_leo_hut = "Island East to Leo Hut"
    island_east_to_island_shrine = "Island East to Island Shrine"

    leo_hut_to_island_east = "Leo Hut to Island East"
    island_shrine_to_island_east = "Island Shrine to Island East"

    island_southeast_to_south = "Island Southeast to Island South"
    island_southeast_to_pirate_cove = "Island Southeast to Pirate Cove"
    pirate_cove_to_island_southeast = "Pirate Cove to Island Southeast"

    island_north_to_south = "Island North to Island South"
    island_north_to_field_office = "Island North to Field Office"
    island_north_to_dig_site = "Island North to Dig Site"
    dig_site_to_professor_snail_cave = "Dig Site to Professor Snail Cave"
    island_north_to_volcano = "Island North to Volcano Entrance"
    volcano_to_secret_beach = "Volcano River to Secret Beach"
    talk_to_island_trader = "Talk to Island Trader"
    climb_to_volcano_5 = "Climb to Volcano Floor 5"
    talk_to_volcano_dwarf = "Talk to Volcano Dwarf"
    climb_to_volcano_10 = "Climb to Volcano Floor 10"

    field_office_to_island_north = "Field Office to Island North"
    dig_site_to_island_north = "Dig Site to Island North"
    professor_snail_cave_to_dig_site = "Professor Snail Cave to Dig Site"
    volcano_to_island_north = "Volcano Entrance to Island North"
    secret_beach_to_volcano = "Secret Beach to Volcano River"

    parrot_express_docks_to_volcano = "Parrot Express Docks to Volcano"
    parrot_express_jungle_to_volcano = "Parrot Express Jungle to Volcano"
    parrot_express_dig_site_to_volcano = "Parrot Express Dig Site to Volcano"
    parrot_express_docks_to_dig_site = "Parrot Express Docks to Dig Site"
    parrot_express_jungle_to_dig_site = "Parrot Express Jungle to Dig Site"
    parrot_express_volcano_to_dig_site = "Parrot Express Volcano to Dig Site"
    parrot_express_docks_to_jungle = "Parrot Express Docks to Jungle"
    parrot_express_dig_site_to_jungle = "Parrot Express Dig Site to Jungle"
    parrot_express_volcano_to_jungle = "Parrot Express Volcano to Jungle"
    parrot_express_jungle_to_docks = "Parrot Express Jungle to Docks"
    parrot_express_dig_site_to_docks = "Parrot Express Dig Site to Docks"
    parrot_express_volcano_to_docks = "Parrot Express Volcano to Docks"

    # TODO make these connections
    hospital_to_back = "Hospital to Hospital Back Area"
    hospital_to_front = "Hospital Back Area to Hospital"
    volcano_river_to_entrance = "Volcano River to Volcano Entrance"
    volcano_entrance_to_river = "Volcano Entrance to Volcano River"

# Skull Cavern Elevator


class DeepWoodsEntrance:
    secret_woods_to_deep_woods = "Woods to Deep Woods"
    deep_woods_to_secret_woods = "Deep Woods to Woods"
    use_woods_obelisk = "Use Woods Obelisk"
    deep_woods_house = "Deep Woods to Deep Woods House"
    leave_deep_woods_house = "Deep Woods House to Deep Woods"
    deep_woods_depth_1 = move_to_woods_depth(1)
    deep_woods_depth_10 = move_to_woods_depth(10)
    deep_woods_depth_20 = move_to_woods_depth(20)
    deep_woods_depth_30 = move_to_woods_depth(30)
    deep_woods_depth_40 = move_to_woods_depth(40)
    deep_woods_depth_50 = move_to_woods_depth(50)
    deep_woods_depth_60 = move_to_woods_depth(60)
    deep_woods_depth_70 = move_to_woods_depth(70)
    deep_woods_depth_80 = move_to_woods_depth(80)
    deep_woods_depth_90 = move_to_woods_depth(90)
    deep_woods_depth_100 = move_to_woods_depth(100)


class EugeneEntrance:
    forest_to_garden = "Forest to Eugene's Garden"
    garden_to_forest = "Eugene's Garden to Forest"
    garden_to_bedroom = "Eugene's Garden to Eugene's Bedroom"
    bedroom_to_garden = "Eugene's Bedroom to Eugene's Garden"


class MagicEntrance:
    store_to_altar = "Pierre's General Store to Magic Altar"


class JasperEntrance:
    museum_to_bedroom = "Museum to Jasper's Bedroom"
    bedroom_to_museum = "Jasper's Bedroom to Museum"


class AlecEntrance:
    forest_to_petshop = "Forest to Alec's Pet Shop"
    petshop_to_forest = "Alec's Pet Shop to Forest"
    petshop_to_bedroom = "Alec's Pet Shop to Alec's Bedroom"
    bedroom_to_petshop = "Alec's Bedroom to Alec's Pet Shop"


class YobaEntrance:
    secret_woods_to_clearing = "Woods to Yoba's Clearing"
    clearing_to_secret_woods = "Yoba's Clearing to Woods"


class JunaEntrance:
    forest_to_juna_cave = "Forest to Juna's Cave"
    juna_cave_to_forest = "Juna's Cave to Forest"


class AyeishaEntrance:
    bus_stop_to_mail_van = "Bus Stop to Ayeisha's Mail Van"
    mail_van_to_bus_stop = "Ayeisha's Mail Van to Bus Stop"


class RileyEntrance:
    town_to_riley = "Town to Riley's House"
    riley_to_town = "Riley's House to Town"

