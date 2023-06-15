def dig_to_mines_floor(floor: int) -> str:
    return f"Dig to The Mines - Floor {floor}"


def dig_to_skull_floor(floor: int) -> str:
    return f"Mine to Skull Cavern Floor {floor}"


def move_to_woods_depth(depth: int) -> str:
    return f"Enter Deep Woods Depth {depth}"


class SVEntrance:
    to_stardew_valley = "To Stardew Valley"
    to_farmhouse = "To Farmhouse"
    farmhouse_to_farm = "Farmhouse to Farm"
    farm_to_farmhouse = "Farm to Farmhouse"
    downstairs_to_cellar = "Farmhouse to Cellar"
    cellar_to_upstairs = "Cellar to Farmhouse"
    farm_to_backwoods = "Farm to Backwoods"
    backwoods_to_farm = "Backwoods to Farm"
    farm_to_bus_stop = "Farm to Bus Stop"
    bus_stop_to_farm = "Bus Stop to Farm"
    farm_to_forest = "Farm to Forest"
    forest_to_farm = "Forest to Farm"
    farm_to_farmcave = "Farm to Farmcave"
    farmcave_to_farm = "Farmcave to Farm"
    enter_greenhouse = "Farm to Greenhouse"
    leave_greenhouse = "Greenhouse to Farm"
    use_desert_obelisk = "Use Desert Obelisk"
    use_island_obelisk = "Use Island Obelisk"
    use_farm_obelisk = "Use Farm Obelisk"
    
    backwoods_to_mountain = "Backwoods to Mountain"
    mountain_to_backwoods = "Mountain to Backwoods"
    
    bus_stop_to_town = "Bus Stop to Town"
    town_to_bus_stop = "Town to Bus Stop"
    take_bus_to_desert = "Bus Stop to Desert"
    take_bus_to_town = "Desert to Bus Stop"
    bus_stop_to_tunnel_entrance = "Bus Stop to Tunnel Entrance"
    tunnel_entrance_to_bus_stop = "Tunnel Entrance to Bus Stop"
    
    forest_to_town = "Forest to Town"
    town_to_forest = "Town to Forest"
    enter_secret_woods = "Forest to Secret Woods"
    leave_secret_woods = "Secret Woods to Forest"
    forest_to_wizard_tower = "Forest to Wizard Tower"
    wizard_tower_to_forest = "Wizard Tower to Forest"
    forest_to_marnie_ranch = "Forest to Marnie's Ranch"
    marnie_ranch_to_forest = "Marnie's Ranch to Forest"
    forest_to_leah_cottage = "Forest to Leah's Cottage"
    leah_cottage_to_forest = "Leah's Cottage to Forest"
    forest_to_sewers = "Forest to Sewers"
    sewers_to_forest = "Sewers to Forest"
    buy_from_traveling_merchant = "Buy from Traveling Merchant"
    
    mountain_to_railroad = "Mountain to Railroad"
    railroad_to_mountain = "Railroad to Mountain"
    mountain_to_tent = "Mountain to Tent"
    tent_to_mountain = "Tent to Mountain"
    mountain_to_carpenter_shop = "Mountain to Carpenter Shop"
    carpenter_shop_to_mountain= "Carpenter Shop to Mountain"
    mountain_to_maru_room = "Mountain to Maru's Room"
    maru_room_to_mountain = "Maru's Room to Mountain"
    mountain_to_the_mines = "Mountain to The Mines"
    the_mines_to_mountain = "The Mines to Mountain"
    enter_quarry = "Mountain to Quarry"
    leave_quarry = "Quarry to Mountain"
    mountain_to_adventurer_guild = "Mountain to Adventurer's Guild"
    adventurer_guild_to_mountain = "Adventurer's Guild to Mountain"
    mountain_to_town = "Mountain to Town"
    town_to_mountain = "Town to Mountain"
    
    enter_tunnel = "Backwoods to Tunnel"
    leave_tunnel = "Tunnel to Backwoods"
    
    town_to_community_center = "Town to Community Center"
    community_center_to_town = "Community Center to Town"
    access_crafts_room = "Access Crafts Room"
    access_pantry = "Access Pantry"
    access_fish_tank = "Access Fish Tank"
    access_boiler_room = "Access Boiler Room"
    access_bulletin_board = "Access Bulletin Board"
    access_vault = "Access Vault"
    
    town_to_beach = "Town to Beach"
    beach_to_town = "Beach to Town"
    town_to_hospital = "Town to Hospital"
    hospital_to_town = "Hospital to Town"
    town_to_pierre_general_store = "Town to Pierre's General Store"
    pierre_general_store_to_town = "Pierre's General Store to Town"
    town_to_saloon = "Town to Saloon"
    saloon_to_town = "Saloon to Town"
    town_to_alex_house = "Town to Alex's House"
    alex_house_to_town = "Alex's House to Town"
    town_to_trailer = "Town to Trailer"
    trailer_to_town = "Trailer to Town"
    town_to_mayor_manor = "Town to Mayor's Manor"
    mayor_manor_to_town = "Mayor's Manor to Town"
    town_to_sam_house = "Town to Sam's House"
    sam_house_to_town = "Sam's House to Town"
    town_to_haley_house = "Town to Haley's House"
    haley_house_to_town = "Haley's House to Town"
    town_to_sewers = "Town to Sewers"
    sewers_to_town = "Sewers to Town"
    town_to_clint_blacksmith = "Town to Clint's Blacksmith"
    clint_blacksmith_to_town = "Clint's Blacksmith to Town"
    town_to_museum = "Town to Museum"
    museum_to_town = "Museum to Town"
    town_to_jojamart = "Town to JojaMart"
    jojamart_to_town = "JojaMart to Town"
    
    beach_to_willy_fish_shop = "Beach to Willy's Fish Shop"
    willy_fish_shop_to_beach = "Willy's Fish Shop to Beach"
    fish_shop_to_boat_tunnel = "Fish Shop to Boat Tunnel"
    boat_tunnel_to_fish_shop = "Boat Tunnel to Fish Shop"
    enter_elliott_house = "Beach to Elliott's House"
    leave_elliott_house = "Elliott's House to Beach"
    enter_tide_pools = "Beach to Tide Pools"
    
    enter_bathhouse_entrance = "Railroad to Bathhouse Entrance"
    leave_bathhouse = "Bathhouse Entrance to Railroad"
    enter_witch_warp_cave = "Railroad to Witch Warp Cave"
    leave_witch_warp_cave = "Witch Warp Cave to Railroad"
    enter_perfection_cutscene_area = "Railroad to Perfection Cutscene Area"
    leave_perfection_cutscene_area = "Perfection Cutscene Area to Railroad"
    
    enter_sebastian_room = "Carpenter Shop to Sebastian's Room"
    leave_sebastian_room = "Sebastian's Room to Carpenter Shop"
    enter_harvey_room = "Hospital to Harvey's Room"
    leave_harvey_room = "Harvey's Room to Hospital"
    enter_sunroom = "Pierre's General Store to Sunroom"
    leave_sunroom = "Sunroom to Pierre's General Store"
    enter_mutant_bug_lair = "Sewers to Mutant Bug Lair"
    leave_mutant_bug_lair = "Mutant Bug Lair to Sewers"
    enter_wizard_basement = "Wizard Tower to Wizard Basement"
    leave_wizard_basement = "Wizard Basement to Wizard Tower"
    
    play_journey_of_the_prairie_king = "Play Journey of the Prairie King"
    reach_jotpk_world_2 = "Reach JotPK World 2"
    reach_jotpk_world_3 = "Reach JotPK World 3"
    play_junimo_kart = "Play Junimo Kart"
    reach_junimo_kart_2 = "Reach Junimo Kart 2"
    reach_junimo_kart_3 = "Reach Junimo Kart 3"
    
    enter_locker_room = "Bathhouse Entrance to Locker Room"
    leave_locker_room = "Locker Room to Bathhouse Entrance"
    enter_public_bath = "Locker Room to Public Bath"
    leave_public_bath = "Public Bath to Locker Room"
    enter_witch_swamp = "Witch Warp Cave to Witch's Swamp"
    leave_witch_swamp = "Witch's Swamp to Witch Warp Cave"
    enter_witch_hut = "Witch's Swamp to Witch's Hut"
    leave_witch_hut = "Witch's Hut to Witch's Swamp"
    
    enter_quarry_mine_entrance = "Quarry to Quarry Mine Entrance"
    leave_quarry_mine_entrance = "Quarry Mine Entrance to Quarry"
    enter_quarry_mine = "Quarry Mine Entrance to Quarry Mine"
    leave_quarry_mine = "Quarry Mine to Quarry Mine Entrance"
    
    enter_oasis = "Desert to Oasis"
    leave_oasis = "Oasis to Desert"
    enter_casino = "Oasis to Casino"
    leave_casino = "Casino to Oasis"
    enter_skull_cavern_entrance = "Desert to Skull Cavern Entrance"
    leave_skull_cavern_entrance = "Skull Cavern Entrance to Desert"
    enter_skull_cavern = "Skull Cavern Entrance to Skull Cavern"
    
    mine_to_skull_cavern_floor_25 = dig_to_skull_floor(25)
    mine_to_skull_cavern_floor_100 = dig_to_skull_floor(100)
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
    
    boat_to_ginger_island = "Take the Boat to Ginger Island"
    
    island_south_to_west = "Island South to Island West"
    island_west_to_south = "Island West to Island South"
    island_south_to_north = "Island South to Island North"
    island_north_to_south = "Island North to Island South"
    island_south_to_east = "Island South to Island East"
    island_east_to_south = "Island East to Island South"
    island_south_to_southeast = "Island South to Island Southeast"
    island_southeast_to_south = "Island Southeast to Island South"
    island_west_to_islandfarmhouse = "Island West to Island Farmhouse"
    islandfarmhouse_to_west = "Island Farmhouse to Island West"
    island_west_to_gourmand_cave = "Island West to Gourmand Cave"
    gourmand_cave_to_island_west = "Gourmand Cave to Island West"
    island_west_to_crystals_cave = "Island West to Crystal Cave"
    crystals_cave_to_island_west = "Crystal Cave to Island West"
    island_west_to_shipwreck = "Island West to Shipwreck"
    shipwreck_to_island_west = "Shipwreck to Island West"
    island_west_to_qi_walnut_room = "Island West to Qi Walnut Room"
    qi_walnut_room_to_island_west = "Qi Walnut Room to Island West"
    island_east_to_leo_hut = "Island East to Leo Hut"
    leo_hut_to_island_east = "Leo Hut to Island East"
    island_east_to_island_shrine = "Island East to Island Shrine"
    island_shrine_to_island_east = "Island Shrine to Island East"
    island_southeast_to_pirate_cove = "Island Southeast to Pirate Cove"
    pirate_cove_to_island_southeast = "Pirate Cove to Island Southeast"
    island_north_to_field_office = "Island North to Field Office"
    field_office_to_island_north = "Field Office to Island North"
    island_north_to_dig_site = "Island North to Dig Site"
    island_north_to_volcano = "Island North to Volcano"
    volcano_to_island_north = "Volcano to Island North"
    
    talk_to_island_trader = "Talk to Island Trader"
    climb_to_volcano_5 = "Climb to Volcano Floor 5"
    climb_to_volcano_10 = "Climb to Volcano Floor 10"
    
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

# Skull Cavern Elevator


class DeepWoodsEntrance:
    secret_woods_to_deep_woods = "Woods to Deep Woods"
    deep_woods_to_secret_woods = "Deep Woods to Woods"
    use_woods_obelisk = "Use Woods Obelisk"
    deep_woods_house = "Deep Woods to Deep Woods House"
    leave_deep_woods_house = "Deep Woods House to Deep Woods"
    deep_woods_depth_10 = move_to_woods_depth(10)
    deep_woods_depth_30 = move_to_woods_depth(30)
    deep_woods_depth_50 = move_to_woods_depth(50)
    deep_woods_depth_70 = move_to_woods_depth(70)
    deep_woods_depth_90 = move_to_woods_depth(90)
    deep_woods_depth_100 = move_to_woods_depth(100)


class EugeneEntrance:
    forest_to_garden = "Forest to Eugene's Garden"
    garden_to_forest = "Eugene's Garden to Forest"
    garden_to_bedroom = "Eugene's Garden to Eugene's Bedroom"
    bedroom_to_garden = "Eugene's Bedroom to Eugene's Garden"


class JasperEntrance:
    museum_to_bedroom = "Museum to Jasper's Bedroom"
    bedroom_to_museum = "Jasper's Bedroom to Museum"


class AlecEntrance:
    forest_to_petshop = "Forest to Alec's Pet Shop"
    petshop_to_forest = "Alec's Pet Shop to Forest"
    petshop_to_bedroom = "Alec's Pet Shop to Alec's Bedroom"
    bedroom_to_petshop = "Alec's Bedroom to Alec's Pet Shop"


class YobaEntrance:
    secret_woods_to_clearing = "Woods to Yoba Clearing"
    clearing_to_secret_woods = "Yoba Clearing to Woods"


class JunaEntrance:
    forest_to_juna_cave = "Forest to Juna's Cave"
    juna_cave_to_forest = "Juna's Cave to Forest"

