
from BaseClasses import Location
from .rom_addresses import rom_addresses
from . import poke_data
loc_id_start = 172000000


def trainersanity(world, player):
    include = world.trainersanity_table.pop(0)
    world.trainersanity_table.append(include)
    return include


def dexsanity(world, player):
    include = world.dexsanity_table.pop(0)
    world.dexsanity_table.append(include)
    return include


def hidden_items(world, player):
    return world.options.randomize_hidden_items


def hidden_moon_stones(world, player):
    return world.options.randomize_hidden_items or world.options.stonesanity


def tea(world, player):
    return world.options.tea


def extra_key_items(world, player):
    return world.options.extra_key_items


def always_on(world, player):
    return True


def prizesanity(world, player):
    return world.options.prizesanity


def split_card_key(world, player):
    return world.options.split_card_key.value > 0


def not_stonesanity(world, player):
    return not world.options.stonesanity


class LocationData:
    def __init__(self, region, name, original_item, rom_address=None, ram_address=None, event=False, type="Item",
                 inclusion=always_on, level=None, level_address=None):
        self.region = region
        self.name = region if name == "" else region.split("-")[0] + " - " + name if name != "Trainer Parties" else region + " - Trainer Parties"
        self.original_item = original_item
        self.rom_address = rom_address
        self.ram_address = ram_address
        self.event = event
        self.type = type
        self.inclusion = inclusion
        self.level = level
        self.address = None
        if level_address:
            self.level_address = level_address
        elif level:
            self.level_address = rom_address - 1
        else:
            self.level_address = None


class EventFlag:
    def __init__(self, flag):
        self.byte = int(flag / 8)
        self.bit = flag % 8
        self.flag = flag


class Missable:
    def __init__(self, flag):
        self.byte = int(flag / 8)
        self.bit = flag % 8
        self.flag = flag


class Hidden:
    def __init__(self, flag):
        self.byte = int(flag / 8)
        self.bit = flag % 8
        self.flag = flag


class Rod:
    def __init__(self, flag):
        self.byte = 0
        self.bit = flag
        self.flag = flag


class DexSanityFlag:
    def __init__(self, flag):
        self.byte = int(flag / 8)
        self.bit = flag % 8
        self.flag = flag


location_data = [ # TODO add trades/promoes
    LocationData("Mason Laboratory Center Room", "Sam Reward 1", "Energy Pack", rom_addresses["Sam_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Sam Reward 2", "Energy Pack", rom_addresses["Sam_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Beat Sam", "Beat Sam", event=True),
    LocationData("Mason Laboratory Center Room", "Sam Rematch Reward 1", "Energy Pack", rom_addresses["Sam_Rematch_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Sam Rematch Reward 2", "Energy Pack", rom_addresses["Sam_Rematch_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 1", "Energy Pack", rom_addresses["Aaron_LF_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 2", "Energy Pack", rom_addresses["Aaron_LF_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Beat Aaron LF", "Beat Aaron LF", event=True),
    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 1", "Energy Pack", rom_addresses["Aaron_Rematch_LF_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 2", "Energy Pack", rom_addresses["Aaron_Rematch_LF_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 1", "Energy Pack", rom_addresses["Aaron_WF_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 2", "Energy Pack", rom_addresses["Aaron_WF_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Beat Aaron WF", "Beat Aaron WF", event=True),
    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 1", "Energy Pack", rom_addresses["Aaron_Rematch_WF_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 2", "Energy Pack", rom_addresses["Aaron_Rematch_WF_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 1", "Energy Pack", rom_addresses["Aaron_GP_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 2", "Energy Pack", rom_addresses["Aaron_GP_Reward_2"]),
    LocationData("Mason Laboratory Center Room", "Beat Aaron GP", "Beat Aaron GP", event=True),
    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 1", "Energy Pack", rom_addresses["Aaron_Rematch_GP_Reward_1"]),
    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 2", "Energy Pack", rom_addresses["Aaron_Rematch_GP_Reward_2"]),

    LocationData("Grass Club Main Hall", "Heather Reward 1", "Colosseum Pack", rom_addresses["Heather_Reward_1"]),
    LocationData("Grass Club Main Hall", "Heather Reward 2", "Colosseum Pack", rom_addresses["Heather_Reward_2"]),
    LocationData("Grass Club Main Hall", "Beat Heather", "Beat Heather", event=True),
    LocationData("Grass Club Main Hall", "Heather Rematch Reward 1", "Colosseum Pack", rom_addresses["Heather_Rematch_Reward_1"]),
    LocationData("Grass Club Main Hall", "Heather Rematch Reward 2", "Colosseum Pack", rom_addresses["Heather_Rematch_Reward_2"]),
    LocationData("Grass Club Main Hall", "Kristin Reward 1", "Evolution Pack", rom_addresses["Kristin_Reward_1"]),
    LocationData("Grass Club Main Hall", "Kristin Reward 2", "Evolution Pack", rom_addresses["Kristin_Reward_2"]),
    LocationData("Grass Club Main Hall", "Beat Kristin", "Beat Kristin", event=True),
    LocationData("Grass Club Main Hall", "Kristin Rematch Reward 1", "Evolution Pack", rom_addresses["Kristin_Rematch_Reward_1"]),
    LocationData("Grass Club Main Hall", "Kristin Rematch Reward 2", "Evolution Pack", rom_addresses["Kristin_Rematch_Reward_2"]),
    LocationData("Grass Club Lounge", "Brittany Reward 1", "Mystery Pack", rom_addresses["Brittany_Reward_1"]),
    LocationData("Grass Club Lounge", "Brittany Reward 2", "Mystery Pack", rom_addresses["Brittany_Reward_2"]),
    LocationData("Grass Club Lounge", "Beat Brittany", "Beat Brittany", event=True),
    LocationData("Grass Club Lounge", "Brittany Rematch Reward 1", "Mystery Pack", rom_addresses["Brittany_Rematch_Reward_1"]),
    LocationData("Grass Club Lounge", "Brittany Rematch Reward 2", "Mystery Pack", rom_addresses["Brittany_Rematch_Reward_2"]),
    LocationData("Grass Club Main Hall", "Nikki Reward 1", "Laboratory Pack", rom_addresses["Nikki_Reward_1"]),
    LocationData("Grass Club Main Hall", "Nikki Reward 2", "Laboratory Pack", rom_addresses["Nikki_Reward_2"]),
    LocationData("Grass Club Main Hall", "Beat Nikki", "Beat Nikki", event=True),
    LocationData("Grass Club Main Hall", "Nikki Rematch Reward 1", "Laboratory Pack", rom_addresses["Nikki_Rematch_Reward_1"]),
    LocationData("Grass Club Main Hall", "Nikki Rematch Reward 2", "Laboratory Pack", rom_addresses["Nikki_Rematch_Reward_2"]),

    LocationData("Science Club Main Hall", "Joseph Reward 1", "Laboratory Pack", rom_addresses["Joseph_Reward_1"]),
    LocationData("Science Club Main Hall", "Joseph Reward 2", "Laboratory Pack", rom_addresses["Joseph_Reward_2"]),
    LocationData("Science Club Main Hall", "Beat Joseph", "Beat Joseph", event=True),
    LocationData("Science Club Main Hall", "Joseph Rematch Reward 1", "Laboratory Pack", rom_addresses["Joseph_Rematch_Reward_1"]),
    LocationData("Science Club Main Hall", "Joseph Rematch Reward 2", "Laboratory Pack", rom_addresses["Joseph_Rematch_Reward_2"]),
    LocationData("Science Club Main Hall", "David Reward 1", "Mystery Pack", rom_addresses["David_Reward_1"]),
    LocationData("Science Club Main Hall", "David Reward 2", "Mystery Pack", rom_addresses["David_Reward_2"]),
    LocationData("Science Club Main Hall", "Beat David", "Beat David", event=True),
    LocationData("Science Club Main Hall", "David Rematch Reward 1", "Mystery Pack", rom_addresses["David_Rematch_Reward_1"]),
    LocationData("Science Club Main Hall", "David Rematch Reward 2", "Mystery Pack", rom_addresses["David_Rematch_Reward_2"]),
    LocationData("Science Club Main Hall", "Erik Reward 1", "Evolution Pack", rom_addresses["Erik_Reward_1"]),
    LocationData("Science Club Main Hall", "Erik Reward 2", "Evolution Pack", rom_addresses["Erik_Reward_2"]),
    LocationData("Science Club Main Hall", "Beat Erik", "Beat Erik", event=True),
    LocationData("Science Club Main Hall", "Erik Rematch Reward 1", "Evolution Pack", rom_addresses["Erik_Rematch_Reward_1"]),
    LocationData("Science Club Main Hall", "Erik Rematch Reward 2", "Evolution Pack", rom_addresses["Erik_Rematch_Reward_2"]),
    LocationData("Science Club Main Hall", "Rick Reward 1", "Laboratory Pack", rom_addresses["Rick_Reward_1"]),
    LocationData("Science Club Main Hall", "Rick Reward 2", "Laboratory Pack", rom_addresses["Rick_Reward_2"]),
    LocationData("Science Club Main Hall", "Beat Rick", "Beat Rick", event=True),
    LocationData("Science Club Main Hall", "Rick Rematch Reward 1", "Laboratory Pack",  rom_addresses["Rick_Rematch_Reward_1"]),
    LocationData("Science Club Main Hall", "Rick Rematch Reward 2", "Laboratory Pack",  rom_addresses["Rick_Rematch_Reward_2"]),

    LocationData("Fire Club Main Hall", "Jonathan Reward 1", "Colosseum Pack", rom_addresses["Jonathan_Reward_1"]),
    LocationData("Fire Club Main Hall", "Jonathan Reward 2", "Colosseum Pack", rom_addresses["Jonathan_Reward_2"]),
    LocationData("Fire Club Main Hall", "Beat Jonathan", "Beat Jonathan", event=True),
    LocationData("Fire Club Main Hall", "Jonathan Rematch Reward 1", "Colosseum Pack", rom_addresses["Jonathan_Rematch_Reward_1"]),
    LocationData("Fire Club Main Hall", "Jonathan Rematch Reward 2", "Colosseum Pack", rom_addresses["Jonathan_Rematch_Reward_2"]),
    LocationData("Fire Club Main Hall", "Adam Reward 1", "Colosseum Pack", rom_addresses["Adam_Reward_1"]),
    LocationData("Fire Club Main Hall", "Adam Reward 2", "Colosseum Pack", rom_addresses["Adam_Reward_2"]),
    LocationData("Fire Club Main Hall", "Beat Adam", "Beat Adam", event=True),
    LocationData("Fire Club Main Hall", "Adam Rematch Reward 1", "Colosseum Pack", rom_addresses["Adam_Rematch_Reward_1"]),
    LocationData("Fire Club Main Hall", "Adam Rematch Reward 2", "Colosseum Pack", rom_addresses["Adam_Rematch_Reward_2"]),
    LocationData("Fire Club Main Hall", "John Reward 1", "Evolution Pack", rom_addresses["John_Reward_1"]),
    LocationData("Fire Club Main Hall", "John Reward 2", "Evolution Pack", rom_addresses["John_Reward_2"]),
    LocationData("Fire Club Main Hall", "Beat John", "Beat John", event=True),
    LocationData("Fire Club Main Hall", "John Rematch Reward 1", "Evolution Pack", rom_addresses["John_Rematch_Reward_1"]),
    LocationData("Fire Club Main Hall", "John Rematch Reward 2", "Evolution Pack", rom_addresses["John_Rematch_Reward_2"]),
    LocationData("Fire Club Main Hall", "Ken Reward 1", "Mystery Pack", rom_addresses["Ken_Reward_1"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Ken Reward 2", "Mystery Pack", rom_addresses["Ken_Reward_2"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Beat Ken", "Beat Ken", event=True),
    LocationData("Fire Club Main Hall", "Ken Rematch Reward 1", "Mystery Pack", rom_addresses["Ken_Rematch_Reward_1"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Ken Rematch Reward 2", "Mystery Pack", rom_addresses["Ken_Rematch_Reward_2"]), # Needs 300 cards

    LocationData("Water Club Main Hall", "Joshua Reward 1", "Mystery Pack", rom_addresses["Joshua_Reward_1"]),
    LocationData("Water Club Main Hall", "Joshua Reward 2", "Mystery Pack", rom_addresses["Joshua_Reward_2"]),
    LocationData("Water Club Main Hall", "Beat Joshua", "Beat Joshua", event=True),
    LocationData("Water Club Main Hall", "Joshua Rematch Reward 1", "Mystery Pack", rom_addresses["Joshua_Rematch_Reward_1"]),
    LocationData("Water Club Main Hall", "Joshua Rematch Reward 2", "Mystery Pack", rom_addresses["Joshua_Rematch_Reward_2"]),
    LocationData("Water Club Main Hall", "Amanda Reward 1", "Mystery Pack", rom_addresses["Amanda_Reward_1"]),
    LocationData("Water Club Main Hall", "Amanda Reward 2", "Mystery Pack", rom_addresses["Amanda_Reward_2"]),
    LocationData("Water Club Main Hall", "Beat Amanda", "Beat Amanda", event=True),
    LocationData("Water Club Main Hall", "Amanda Rematch Reward 1", "Mystery Pack", rom_addresses["Amanda_Rematch_Reward_1"]),
    LocationData("Water Club Main Hall", "Amanda Rematch Reward 2", "Mystery Pack", rom_addresses["Amanda_Rematch_Reward_2"]),
    LocationData("Water Club Main Hall", "Sara Reward 1", "Colosseum Pack", rom_addresses["Sara_Reward_1"]),
    LocationData("Water Club Main Hall", "Sara Reward 2", "Colosseum Pack", rom_addresses["Sara_Reward_2"]),
    LocationData("Water Club Main Hall", "Beat Sara", "Beat Sara", event=True),
    LocationData("Water Club Main Hall", "Sara Rematch Reward 1", "Colosseum Pack", rom_addresses["Sara_Rematch_Reward_1"]),
    LocationData("Water Club Main Hall", "Sara Rematch Reward 2", "Colosseum Pack", rom_addresses["Sara_Rematch_Reward_2"]),
    LocationData("Water Club Main Hall", "Amy Reward 1", "Laboratory Pack", rom_addresses["Amy_Reward_1"]),
    LocationData("Water Club Main Hall", "Amy Reward 2", "Laboratory Pack", rom_addresses["Amy_Reward_2"]),
    LocationData("Water Club Main Hall", "Beat Amy", "Beat Amy", event=True),
    LocationData("Water Club Main Hall", "Amy Rematch Reward 1", "Laboratory Pack", rom_addresses["Amy_Rematch_Reward_1"]),
    LocationData("Water Club Main Hall", "Amy Rematch Reward 2", "Laboratory Pack", rom_addresses["Amy_Rematch_Reward_2"]),

    LocationData("Lightning Club Main Hall", "Nicholas Reward 1", "Colosseum Pack", rom_addresses["Nicholas_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Nicholas Reward 2", "Colosseum Pack", rom_addresses["Nicholas_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Beat Nicholas", "Beat Nicholas", event=True),
    LocationData("Lightning Club Main Hall", "Nicholas Rematch Reward 1", "Colosseum Pack", rom_addresses["Nicholas_Rematch_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Nicholas Rematch Reward 2", "Colosseum Pack", rom_addresses["Nicholas_Rematch_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Brandon Reward 1", "Colosseum Pack", rom_addresses["Brandon_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Brandon Reward 2", "Colosseum Pack", rom_addresses["Brandon_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Beat Brandon", "Beat Brandon", event=True),
    LocationData("Lightning Club Main Hall", "Brandon Rematch Reward 1", "Colosseum Pack", rom_addresses["Brandon_Rematch_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Brandon Rematch Reward 2", "Colosseum Pack", rom_addresses["Brandon_Rematch_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Jennifer Reward 1", "Mystery Pack", rom_addresses["Jennifer_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Jennifer Reward 2", "Mystery Pack", rom_addresses["Jennifer_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Beat Jennifer", "Beat Jennifer", event=True),
    LocationData("Lightning Club Main Hall", "Jennifer Rematch Reward 1", "Mystery Pack", rom_addresses["Jennifer_Rematch_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Jennifer Rematch Reward 2", "Mystery Pack", rom_addresses["Jennifer_Rematch_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Isaac Reward 1", "Mystery Pack", rom_addresses["Isaac_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Isaac Reward 2", "Mystery Pack", rom_addresses["Isaac_Reward_2"]),
    LocationData("Lightning Club Main Hall", "Beat Isaac", "Beat Isaac", event=True),
    LocationData("Lightning Club Main Hall", "Isaac Rematch Reward 1", "Mystery Pack", rom_addresses["Isaac_Rematch_Reward_1"]),
    LocationData("Lightning Club Main Hall", "Isaac Rematch Reward 2", "Mystery Pack", rom_addresses["Isaac_Rematch_Reward_2"]),

    LocationData("Psychic Club Main Hall", "Daniel Reward 1", "Evolution Pack", rom_addresses["Daniel_Reward_1"]),
    LocationData("Psychic Club Main Hall", "Daniel Reward 2", "Evolution Pack", rom_addresses["Daniel_Reward_2"]),
    LocationData("Psychic Club Main Hall", "Beat Daniel", "Beat Daniel", event=True),
    LocationData("Psychic Club Main Hall", "Daniel Rematch Reward 1", "Evolution Pack", rom_addresses["Daniel_Rematch_Reward_1"]),
    LocationData("Psychic Club Main Hall", "Daniel Rematch Reward 2", "Evolution Pack", rom_addresses["Daniel_Rematch_Reward_2"]),
    LocationData("Psychic Club Main Hall", "Stephanie Reward 1", "Laboratory Pack", rom_addresses["Stephanie_Reward_1"]),
    LocationData("Psychic Club Main Hall", "Stephanie Reward 2", "Laboratory Pack", rom_addresses["Stephanie_Reward_2"]),
    LocationData("Psychic Club Main Hall", "Beat Stephanie", "Beat Stephanie", event=True),
    LocationData("Psychic Club Main Hall", "Stephanie Rematch Reward 1", "Laboratory Pack", rom_addresses["Stephanie_Rematch_Reward_1"]),
    LocationData("Psychic Club Main Hall", "Stephanie Rematch Reward 2", "Laboratory Pack", rom_addresses["Stephanie_Rematch_Reward_2"]),
    LocationData("Psychic Club Lounge", "Robert Reward 1", "Evolution Pack", rom_addresses["Robert_Reward_1"]),
    LocationData("Psychic Club Lounge", "Robert Reward 2", "Evolution Pack", rom_addresses["Robert_Reward_2"]),
    LocationData("Psychic Club Lounge", "Beat Robert", "Beat Robert", event=True),
    LocationData("Psychic Club Lounge", "Robert Rematch Reward 1", "Evolution Pack", rom_addresses["Robert_Rematch_Reward_1"]),
    LocationData("Psychic Club Lounge", "Robert Rematch Reward 2", "Evolution Pack", rom_addresses["Robert_Rematch_Reward_2"]),
    LocationData("Psychic Club Main Hall", "Murray Reward 1", "Laboratory Pack", rom_addresses["Murray_Reward_1"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Murray Reward 2", "Laboratory Pack", rom_addresses["Murray_Reward_2"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Beat Murray", "Beat Murray", event=True),
    LocationData("Psychic Club Main Hall", "Murray Rematch Reward 1", "Laboratory Pack", rom_addresses["Murray_Rematch_Reward_1"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Murray Rematch Reward 2", "Laboratory Pack", rom_addresses["Murray_Rematch_Reward_2"]), # Requires 4 medals

    LocationData("Rock Club Main Hall", "Ryan Reward 1", "Evolution Pack", rom_addresses["Ryan_Reward_1"]),
    LocationData("Rock Club Main Hall", "Ryan Reward 2", "Evolution Pack", rom_addresses["Ryan_Reward_2"]),
    LocationData("Rock Club Main Hall", "Beat Ryan", "Beat Ryan", event=True),
    LocationData("Rock Club Main Hall", "Ryan Rematch Reward 1", "Evolution Pack", rom_addresses["Ryan_Rematch_Reward_1"]),
    LocationData("Rock Club Main Hall", "Ryan Rematch Reward 2", "Evolution Pack", rom_addresses["Ryan_Rematch_Reward_2"]),
    LocationData("Rock Club Main Hall", "Andrew Reward 1", "Colosseum Pack", rom_addresses["Andrew_Reward_1"]),
    LocationData("Rock Club Main Hall", "Andrew Reward 2", "Colosseum Pack", rom_addresses["Andrew_Reward_2"]),
    LocationData("Rock Club Main Hall", "Beat Andrew", "Beat Andrew", event=True),
    LocationData("Rock Club Main Hall", "Andrew Rematch Reward 1", "Colosseum Pack", rom_addresses["Andrew_Rematch_Reward_1"]),
    LocationData("Rock Club Main Hall", "Andrew Rematch Reward 2", "Colosseum Pack", rom_addresses["Andrew_Rematch_Reward_2"]),
    LocationData("Rock Club Lounge", "Matthew Reward 1", "Mystery Pack", rom_addresses["Matthew_Reward_1"]),
    LocationData("Rock Club Lounge", "Matthew Reward 2", "Mystery Pack", rom_addresses["Matthew_Reward_2"]),
    LocationData("Rock Club Main Hall", "Beat Matthew", "Beat Matthew", event=True),
    LocationData("Rock Club Lounge", "Matthew Rematch Reward 1", "Mystery Pack", rom_addresses["Matthew_Rematch_Reward_1"]),
    LocationData("Rock Club Lounge", "Matthew Rematch Reward 2", "Mystery Pack", rom_addresses["Matthew_Rematch_Reward_2"]),
    LocationData("Rock Club Main Hall", "Gene Reward 1", "Mystery Pack", rom_addresses["Gene_Reward_1"]),
    LocationData("Rock Club Main Hall", "Gene Reward 2", "Mystery Pack", rom_addresses["Gene_Reward_2"]),
    LocationData("Rock Club Main Hall", "Beat Gene", "Beat Gene", event=True),
    LocationData("Rock Club Main Hall", "Gene Rematch Reward 1", "Mystery Pack", rom_addresses["Gene_Rematch_Reward_1"]),
    LocationData("Rock Club Main Hall", "Gene Rematch Reward 2", "Mystery Pack", rom_addresses["Gene_Rematch_Reward_2"]),

    LocationData("Fire Club Lounge", "Jessica Reward 1", "Colosseum Pack", rom_addresses["Jessica_Reward_1"]),
    LocationData("Fire Club Lounge", "Jessica Reward 2", "Colosseum Pack", rom_addresses["Jessica_Reward_2"]),
    LocationData("Fire Club Lounge", "Beat Jessica", "Beat Jessica", event=True),
    LocationData("Fighting Club Main Hall", "Jessica Rematch Reward 1", "Colosseum Pack", rom_addresses["Jessica_Rematch_Reward_1"]),
    LocationData("Fighting Club Main Hall", "Jessica Rematch Reward 2", "Colosseum Pack", rom_addresses["Jessica_Rematch_Reward_2"]),
    LocationData("Grass Club Lobby", "Michael Reward 1", "Colosseum Pack", rom_addresses["Michael_Reward_1"]),
    LocationData("Grass Club Lobby", "Michael Reward 2", "Colosseum Pack", rom_addresses["Michael_Reward_2"]),
    LocationData("Grass Club Lobby", "Beat Michael", "Beat Michael", event=True),
    LocationData("Fighting Club Main Hall", "Michael Rematch Reward 1", "Colosseum Pack", rom_addresses["Michael_Rematch_Reward_1"]),
    LocationData("Fighting Club Main Hall", "Michael Rematch Reward 2", "Colosseum Pack", rom_addresses["Michael_Rematch_Reward_2"]),
    LocationData("Rock Club Lounge", "Chris Reward 1", "Evolution Pack", rom_addresses["Chris_Reward_1"]),
    LocationData("Rock Club Lounge", "Chris Reward 2", "Evolution Pack", rom_addresses["Chris_Reward_2"]),
    LocationData("Rock Club Lounge", "Beat Chris", "Beat Chris", event=True),
    LocationData("Fighting Club Main Hall", "Chris Rematch Reward 1", "Evolution Pack", rom_addresses["Chris_Rematch_Reward_1"]),
    LocationData("Fighting Club Main Hall", "Chris Rematch Reward 2", "Evolution Pack", rom_addresses["Chris_Rematch_Reward_2"]),
    LocationData("Fighting Club Main Hall", "Mitch Reward 1", "Laboratory Pack", rom_addresses["Mitch_Reward_1"]),
    LocationData("Fighting Club Main Hall", "Mitch Reward 2", "Laboratory Pack", rom_addresses["Mitch_Reward_2"]),
    LocationData("Fighting Club Main Hall", "Beat Mitch", "Beat Mitch", event=True),
    LocationData("Fighting Club Main Hall", "Mitch Rematch Reward 1", "Laboratory Pack", rom_addresses["Mitch_Rematch_Reward_1"]),
    LocationData("Fighting Club Main Hall", "Mitch Rematch Reward 2", "Laboratory Pack", rom_addresses["Mitch_Rematch_Reward_2"]),

    LocationData("Grass Club Main Hall", "Grass Medal", "Grass Medal", rom_addresses["Grass_Medal"]),
    LocationData("Science Club Main Hall", "Science Medal", "Science Medal", rom_addresses["Science_Medal"]),
    LocationData("Water Club Main Hall", "Water Medal", "Water Medal", rom_addresses["Water_Medal"]),
    LocationData("Fire Club Main Hall", "Fire Medal", "Fire Medal", rom_addresses["Fire_Medal"]),
    LocationData("Lightning Club Main Hall", "Lightning Medal", "Lightning Medal", rom_addresses["Lightning_Medal"]),
    LocationData("Rock Club Main Hall", "Rock Medal", "Rock Medal", rom_addresses["Rock_Medal"]),
    LocationData("Psychic Club Main Hall", "Psychic Medal", "Psychic Medal", rom_addresses["Psychic_Medal"]),
    LocationData("Fighting Club Main Hall", "Fighting Medal", "Fighting Medal", rom_addresses["Fighting_Medal"]),

    LocationData("Fighting Club Lounge", "Imakuni Reward 1", "Evolution Pack", rom_addresses["Imakuni_Reward_1"]),
    LocationData("Science Club Lounge", "Imakuni Reward 2", "Laboratory Pack", rom_addresses["Imakuni_Reward_2"]),
    LocationData("Lightning Club Lounge", "Imakuni Rematch Reward 1", "Colosseum Pack", rom_addresses["Imakuni_Rematch_Reward_1"]),
    LocationData("Water Club Lounge", "Imakuni Rematch Reward 2", "Mystery Pack", rom_addresses["Imakuni_Rematch_Reward_2"]),

    LocationData("Rock Club Lounge", "Ronald Reward 1", "Promo Mewtwo 1 Pack", rom_addresses["Ronald_Reward_1"]), # 2 Medals
    LocationData("Fire Club Lounge", "Ronald Reward 2", "Promo Jigglypuff Pack", rom_addresses["Ronald_Reward_2"]), # 2 Medals
    LocationData("Grass Club Lounge", "Ronald Rematch Reward 1", "Promo Mew 1 Pack", rom_addresses["Ronald_Rematch_Reward_1"]), # 5 Medals
    LocationData("Psychic Club Lounge", "Ronald Rematch Reward 2", "Super Energy Retrieval Pack", rom_addresses["Ronald_Rematch_Reward_2"]), # 5 Medals

    LocationData("Pokemon Dome Hall of Honor", "Beat Courtney", "Beat Courtney", event=True),
    LocationData("Pokemon Dome Hall of Honor", "Beat Steve", "Beat Steve", event=True),
    LocationData("Pokemon Dome Hall of Honor", "Beat Jack", "Beat Jack", event=True),
    LocationData("Pokemon Dome Hall of Honor", "Beat Rod", "Beat Rod", event=True),
    LocationData("Pokemon Dome Hall of Honor", "Become Champion", "Become Champion", event=True),

    # Open the club main halls as an event
    LocationData("Water Club Lobby", "Open Water Club Door", "Water Club Door", event=True),
    LocationData("Fire Club Lobby", "Open Fire Club Door", "Fire Club Door", event=True),
    LocationData("Lightning Club Lobby", "Open Lightning Club Door", "Lightning Club Door", event=True),
    LocationData("Science Club Lobby", "Open Science Club Door", "Science Club Door", event=True),
    LocationData("Psychic Club Lobby", "Open Psychic Club Door", "Psychic Club Door", event=True),
    LocationData("Grass Club Lobby", "Open Grass Club Door", "Grass Club Door", event=True),
    LocationData("Rock Club Lobby", "Open Rock Club Door", "Rock Club Door", event=True),
    LocationData("Fighting Club Lobby", "Open Fighting Club Door", "Fighting Club Door", event=True),

    # Promo cards
    LocationData("Water Club Lounge", "Promo Arcanine Trade", "Promo Arcanine Pack", rom_addresses["Promo_Arcanine"]),
    LocationData("Grass Club Lounge", "Promo Pikachu Trade (Grass Club)", "Promo Pikachu 1 Pack", rom_addresses["Promo_Pikachu_1"]),
    LocationData("Fighting Club Lounge", "Promo Pikachu Trade (Fighting Club)", "Promo Pikachu 2 Pack", rom_addresses["Promo_Pikachu_2"]),
    LocationData("Ishihara's House", "Ishihara Trade 1", "Promo Flying Pikachu Pack", rom_addresses["Promo_Flying_Pikachu"]),
    LocationData("Ishihara's House", "Ishihara Trade 2", "Promo Surfing Pikachu 1 Pack", rom_addresses["Promo_Surfing_Pikachu_1"]),
    LocationData("Ishihara's House", "Ishihara Trade 3", "Promo Surfing Pikachu 2 Pack", rom_addresses["Promo_Surfing_Pikachu_2"]),
    LocationData("Lightning Club Lounge", "Promo Electabuzz Trade", "Promo Electabuzz Pack", rom_addresses["Promo_Electabuzz"]),
    LocationData("Fire Club Lounge", "Promo Slowpoke Trade", "Promo Slowpoke Pack", rom_addresses["Promo_Slowpoke"]),
    LocationData("Psychic Club Lounge", "Promo Mewtwo Gift", "Promo Mewtwo 2 Pack", rom_addresses["Promo_Mewtwo_2"]),

    # Email logic
    LocationData("Mason Laboratory Center Room", "Email 1", "Colosseum Pack", rom_addresses["Email_1"]),
    LocationData("Mason Laboratory Center Room", "Email 2", "Evolution Pack", rom_addresses["Email_2"]),
    LocationData("Mason Laboratory Center Room", "Email 3", "Mystery Pack", rom_addresses["Email_3"]),
    LocationData("Mason Laboratory Center Room", "Email 4", "Laboratory Pack", rom_addresses["Email_4"]),
    LocationData("Mason Laboratory Center Room", "Email 5", "Colosseum Pack", rom_addresses["Email_5"]),
    LocationData("Mason Laboratory Center Room", "Email 6", "Evolution Pack", rom_addresses["Email_6"]),
    LocationData("Mason Laboratory Center Room", "Email 7", "Mystery Pack", rom_addresses["Email_7"]),
    LocationData("Mason Laboratory Center Room", "Email 8", "Laboratory Pack", rom_addresses["Email_8"]),
    LocationData("Mason Laboratory Center Room", "Email 9", "Promo Articuno Pack", rom_addresses["Email_9"]),
    LocationData("Mason Laboratory Center Room", "Email 10", "Promo Zapdos Pack", rom_addresses["Email_10"]),
    LocationData("Mason Laboratory Center Room", "Email 11", "Promo Moltres Pack", rom_addresses["Email_11"]),
    LocationData("Mason Laboratory Center Room", "Email 12", "Promo Dragonite Pack", rom_addresses["Email_12"]),
    LocationData("Mason Laboratory Center Room", "Email 13", "Promo Imakuni Pack", rom_addresses["Email_13"]),
    LocationData("Mason Laboratory Center Room", "Email 14", "Promo Venusaur Pack", rom_addresses["Email_14"]),
    LocationData("Mason Laboratory Center Room", "Email 15", "Promo Mew 2 Pack", rom_addresses["Email_15"]),
]

class PokemonTCGLocation(Location):
    game = "Pokemon Trading Card Game"

    def __init__(self, player, name, address, rom_address):
        super(PokemonTCGLocation, self).__init__(
            player, name,
            address
        )
        self.rom_address = rom_address
