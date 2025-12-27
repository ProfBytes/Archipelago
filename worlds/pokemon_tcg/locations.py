
from BaseClasses import Location
from .rom_addresses import rom_addresses
loc_id_start = 172000000


def always_on(world, player):
    return True


class LocationData:
    def __init__(self, region, name, original_item, rom_address=None, ram_address=None, bit_mask=0xff, event=False, type="Item",
                 inclusion=always_on, level=None, level_address=None):
        self.region = region
        self.name = region if name == "" else region.split("-")[0] + " - " + name if name != "Trainer Parties" else region + " - Trainer Parties"
        self.original_item = original_item
        self.rom_address = rom_address
        self.ram_address = ram_address
        self.bit_mask = bit_mask
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


location_data = [
    LocationData("Mason Laboratory Center Room", "Sam Reward 1", "Energy Pack", rom_addresses["Sam Reward 1"]),
    LocationData("Mason Laboratory Center Room", "Sam Reward 2", "Energy Pack", rom_addresses["Sam Reward 2"]),
    LocationData("Mason Laboratory Center Room", "Beat Sam", "Beat Sam", event=True),
    LocationData("Mason Laboratory Center Room", "Sam Rematch Reward 1", "Energy Pack", rom_addresses["Sam Rematch Reward 1"]),
    LocationData("Mason Laboratory Center Room", "Sam Rematch Reward 2", "Energy Pack", rom_addresses["Sam Rematch Reward 2"]),
    LocationData("Mason Laboratory Center Room", "Aaron Reward 1", "Energy Pack", rom_addresses["Aaron Reward 1"]),
    LocationData("Mason Laboratory Center Room", "Aaron Reward 2", "Energy Pack", rom_addresses["Aaron Reward 2"]),
    LocationData("Mason Laboratory Center Room", "Beat Aaron", "Beat Aaron", event=True),
    LocationData("Mason Laboratory Center Room", "Aaron Rematch Reward 1", "Energy Pack", rom_addresses["Aaron Rematch Reward 1"]),
    LocationData("Mason Laboratory Center Room", "Aaron Rematch Reward 2", "Energy Pack", rom_addresses["Aaron Rematch Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 1", "Energy Pack", rom_addresses["Aaron LF Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron LF Reward 2", "Energy Pack", rom_addresses["Aaron LF Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Beat Aaron LF", "Beat Aaron LF", event=True),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch LF Reward 1", "Energy Pack", rom_addresses["Aaron Rematch LF Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch LF Reward 2", "Energy Pack", rom_addresses["Aaron Rematch LF Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 1", "Energy Pack", rom_addresses["Aaron WF Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron WF Reward 2", "Energy Pack", rom_addresses["Aaron WF Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Beat Aaron WF", "Beat Aaron WF", event=True),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch WF Reward 1", "Energy Pack", rom_addresses["Aaron Rematch WF Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch WF Reward 2", "Energy Pack", rom_addresses["Aaron Rematch WF Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 1", "Energy Pack", rom_addresses["Aaron GP Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron GP Reward 2", "Energy Pack", rom_addresses["Aaron GP Reward 2"]),
#    LocationData("Mason Laboratory Center Room", "Beat Aaron GP", "Beat Aaron GP", event=True),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch GP Reward 1", "Energy Pack", rom_addresses["Aaron Rematch GP Reward 1"]),
#    LocationData("Mason Laboratory Center Room", "Aaron Rematch GP Reward 2", "Energy Pack", rom_addresses["Aaron Rematch GP Reward 2"]),

    LocationData("Grass Club Main Hall", "Heather Reward 1", "Colosseum Pack", rom_addresses["Heather Reward 1"]),
    LocationData("Grass Club Main Hall", "Heather Reward 2", "Colosseum Pack", rom_addresses["Heather Reward 2"]),
    LocationData("Grass Club Main Hall", "Beat Heather", "Beat Heather", event=True),
    LocationData("Grass Club Main Hall", "Heather Rematch Reward 1", "Colosseum Pack", rom_addresses["Heather Rematch Reward 1"]),
    LocationData("Grass Club Main Hall", "Heather Rematch Reward 2", "Colosseum Pack", rom_addresses["Heather Rematch Reward 2"]),
    LocationData("Grass Club Main Hall", "Kristin Reward 1", "Evolution Pack", rom_addresses["Kristin Reward 1"]),
    LocationData("Grass Club Main Hall", "Kristin Reward 2", "Evolution Pack", rom_addresses["Kristin Reward 2"]),
    LocationData("Grass Club Main Hall", "Beat Kristin", "Beat Kristin", event=True),
    LocationData("Grass Club Main Hall", "Kristin Rematch Reward 1", "Evolution Pack", rom_addresses["Kristin Rematch Reward 1"]),
    LocationData("Grass Club Main Hall", "Kristin Rematch Reward 2", "Evolution Pack", rom_addresses["Kristin Rematch Reward 2"]),
    LocationData("Grass Club Lounge", "Brittany Reward 1", "Mystery Pack", rom_addresses["Brittany Reward 1"]),
    LocationData("Grass Club Lounge", "Brittany Reward 2", "Mystery Pack", rom_addresses["Brittany Reward 2"]),
    LocationData("Grass Club Lounge", "Beat Brittany", "Beat Brittany", event=True),
    LocationData("Grass Club Lounge", "Brittany Rematch Reward 1", "Mystery Pack", rom_addresses["Brittany Rematch Reward 1"]),
    LocationData("Grass Club Lounge", "Brittany Rematch Reward 2", "Mystery Pack", rom_addresses["Brittany Rematch Reward 2"]),
    LocationData("Grass Club Main Hall", "Nikki Reward 1", "Laboratory Pack", rom_addresses["Nikki Reward 1"]),
    LocationData("Grass Club Main Hall", "Nikki Reward 2", "Laboratory Pack", rom_addresses["Nikki Reward 2"]),
    LocationData("Grass Club Main Hall", "Beat Nikki", "Beat Nikki", event=True),
    LocationData("Grass Club Main Hall", "Nikki Rematch Reward 1", "Laboratory Pack", rom_addresses["Nikki Rematch Reward 1"]),
    LocationData("Grass Club Main Hall", "Nikki Rematch Reward 2", "Laboratory Pack", rom_addresses["Nikki Rematch Reward 2"]),

    LocationData("Science Club Main Hall", "Joseph Reward 1", "Laboratory Pack", rom_addresses["Joseph Reward 1"]),
    LocationData("Science Club Main Hall", "Joseph Reward 2", "Laboratory Pack", rom_addresses["Joseph Reward 2"]),
    LocationData("Science Club Main Hall", "Beat Joseph", "Beat Joseph", event=True),
    LocationData("Science Club Main Hall", "Joseph Rematch Reward 1", "Laboratory Pack", rom_addresses["Joseph Rematch Reward 1"]),
    LocationData("Science Club Main Hall", "Joseph Rematch Reward 2", "Laboratory Pack", rom_addresses["Joseph Rematch Reward 2"]),
    LocationData("Science Club Main Hall", "David Reward 1", "Mystery Pack", rom_addresses["David Reward 1"]),
    LocationData("Science Club Main Hall", "David Reward 2", "Mystery Pack", rom_addresses["David Reward 2"]),
    LocationData("Science Club Main Hall", "Beat David", "Beat David", event=True),
    LocationData("Science Club Main Hall", "David Rematch Reward 1", "Mystery Pack", rom_addresses["David Rematch Reward 1"]),
    LocationData("Science Club Main Hall", "David Rematch Reward 2", "Mystery Pack", rom_addresses["David Rematch Reward 2"]),
    LocationData("Science Club Main Hall", "Erik Reward 1", "Evolution Pack", rom_addresses["Erik Reward 1"]),
    LocationData("Science Club Main Hall", "Erik Reward 2", "Evolution Pack", rom_addresses["Erik Reward 2"]),
    LocationData("Science Club Main Hall", "Beat Erik", "Beat Erik", event=True),
    LocationData("Science Club Main Hall", "Erik Rematch Reward 1", "Evolution Pack", rom_addresses["Erik Rematch Reward 1"]),
    LocationData("Science Club Main Hall", "Erik Rematch Reward 2", "Evolution Pack", rom_addresses["Erik Rematch Reward 2"]),
    LocationData("Science Club Main Hall", "Rick Reward 1", "Laboratory Pack", rom_addresses["Rick Reward 1"]),
    LocationData("Science Club Main Hall", "Rick Reward 2", "Laboratory Pack", rom_addresses["Rick Reward 2"]),
    LocationData("Science Club Main Hall", "Beat Rick", "Beat Rick", event=True),
    LocationData("Science Club Main Hall", "Rick Rematch Reward 1", "Laboratory Pack",  rom_addresses["Rick Rematch Reward 1"]),
    LocationData("Science Club Main Hall", "Rick Rematch Reward 2", "Laboratory Pack",  rom_addresses["Rick Rematch Reward 2"]),

    LocationData("Fire Club Main Hall", "Jonathan Reward 1", "Colosseum Pack", rom_addresses["Jonathan Reward 1"]),
    LocationData("Fire Club Main Hall", "Jonathan Reward 2", "Colosseum Pack", rom_addresses["Jonathan Reward 2"]),
    LocationData("Fire Club Main Hall", "Beat Jonathan", "Beat Jonathan", event=True),
    LocationData("Fire Club Main Hall", "Jonathan Rematch Reward 1", "Colosseum Pack", rom_addresses["Jonathan Rematch Reward 1"]),
    LocationData("Fire Club Main Hall", "Jonathan Rematch Reward 2", "Colosseum Pack", rom_addresses["Jonathan Rematch Reward 2"]),
    LocationData("Fire Club Main Hall", "Adam Reward 1", "Colosseum Pack", rom_addresses["Adam Reward 1"]),
    LocationData("Fire Club Main Hall", "Adam Reward 2", "Colosseum Pack", rom_addresses["Adam Reward 2"]),
    LocationData("Fire Club Main Hall", "Beat Adam", "Beat Adam", event=True),
    LocationData("Fire Club Main Hall", "Adam Rematch Reward 1", "Colosseum Pack", rom_addresses["Adam Rematch Reward 1"]),
    LocationData("Fire Club Main Hall", "Adam Rematch Reward 2", "Colosseum Pack", rom_addresses["Adam Rematch Reward 2"]),
    LocationData("Fire Club Main Hall", "John Reward 1", "Evolution Pack", rom_addresses["John Reward 1"]),
    LocationData("Fire Club Main Hall", "John Reward 2", "Evolution Pack", rom_addresses["John Reward 2"]),
    LocationData("Fire Club Main Hall", "Beat John", "Beat John", event=True),
    LocationData("Fire Club Main Hall", "John Rematch Reward 1", "Evolution Pack", rom_addresses["John Rematch Reward 1"]),
    LocationData("Fire Club Main Hall", "John Rematch Reward 2", "Evolution Pack", rom_addresses["John Rematch Reward 2"]),
    LocationData("Fire Club Main Hall", "Ken Reward 1", "Mystery Pack", rom_addresses["Ken Reward 1"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Ken Reward 2", "Mystery Pack", rom_addresses["Ken Reward 2"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Beat Ken", "Beat Ken", event=True),
    LocationData("Fire Club Main Hall", "Ken Rematch Reward 1", "Mystery Pack", rom_addresses["Ken Rematch Reward 1"]), # Needs 300 cards
    LocationData("Fire Club Main Hall", "Ken Rematch Reward 2", "Mystery Pack", rom_addresses["Ken Rematch Reward 2"]), # Needs 300 cards

    LocationData("Water Club Main Hall", "Joshua Reward 1", "Mystery Pack", rom_addresses["Joshua Reward 1"]),
    LocationData("Water Club Main Hall", "Joshua Reward 2", "Mystery Pack", rom_addresses["Joshua Reward 2"]),
    LocationData("Water Club Main Hall", "Beat Joshua", "Beat Joshua", event=True),
    LocationData("Water Club Main Hall", "Joshua Rematch Reward 1", "Mystery Pack", rom_addresses["Joshua Rematch Reward 1"]),
    LocationData("Water Club Main Hall", "Joshua Rematch Reward 2", "Mystery Pack", rom_addresses["Joshua Rematch Reward 2"]),
    LocationData("Water Club Main Hall", "Amanda Reward 1", "Mystery Pack", rom_addresses["Amanda Reward 1"]),
    LocationData("Water Club Main Hall", "Amanda Reward 2", "Mystery Pack", rom_addresses["Amanda Reward 2"]),
    LocationData("Water Club Main Hall", "Beat Amanda", "Beat Amanda", event=True),
    LocationData("Water Club Main Hall", "Amanda Rematch Reward 1", "Mystery Pack", rom_addresses["Amanda Rematch Reward 1"]),
    LocationData("Water Club Main Hall", "Amanda Rematch Reward 2", "Mystery Pack", rom_addresses["Amanda Rematch Reward 2"]),
    LocationData("Water Club Main Hall", "Sara Reward 1", "Colosseum Pack", rom_addresses["Sara Reward 1"]),
    LocationData("Water Club Main Hall", "Sara Reward 2", "Colosseum Pack", rom_addresses["Sara Reward 2"]),
    LocationData("Water Club Main Hall", "Beat Sara", "Beat Sara", event=True),
    LocationData("Water Club Main Hall", "Sara Rematch Reward 1", "Colosseum Pack", rom_addresses["Sara Rematch Reward 1"]),
    LocationData("Water Club Main Hall", "Sara Rematch Reward 2", "Colosseum Pack", rom_addresses["Sara Rematch Reward 2"]),
    LocationData("Water Club Main Hall", "Amy Reward 1", "Laboratory Pack", rom_addresses["Amy Reward 1"]),
    LocationData("Water Club Main Hall", "Amy Reward 2", "Laboratory Pack", rom_addresses["Amy Reward 2"]),
    LocationData("Water Club Main Hall", "Beat Amy", "Beat Amy", event=True),
    LocationData("Water Club Main Hall", "Amy Rematch Reward 1", "Laboratory Pack", rom_addresses["Amy Rematch Reward 1"]),
    LocationData("Water Club Main Hall", "Amy Rematch Reward 2", "Laboratory Pack", rom_addresses["Amy Rematch Reward 2"]),

    LocationData("Lightning Club Main Hall", "Nicholas Reward 1", "Colosseum Pack", rom_addresses["Nicholas Reward 1"]),
    LocationData("Lightning Club Main Hall", "Nicholas Reward 2", "Colosseum Pack", rom_addresses["Nicholas Reward 2"]),
    LocationData("Lightning Club Main Hall", "Beat Nicholas", "Beat Nicholas", event=True),
    LocationData("Lightning Club Main Hall", "Nicholas Rematch Reward 1", "Colosseum Pack", rom_addresses["Nicholas Rematch Reward 1"]),
    LocationData("Lightning Club Main Hall", "Nicholas Rematch Reward 2", "Colosseum Pack", rom_addresses["Nicholas Rematch Reward 2"]),
    LocationData("Lightning Club Main Hall", "Brandon Reward 1", "Colosseum Pack", rom_addresses["Brandon Reward 1"]),
    LocationData("Lightning Club Main Hall", "Brandon Reward 2", "Colosseum Pack", rom_addresses["Brandon Reward 2"]),
    LocationData("Lightning Club Main Hall", "Beat Brandon", "Beat Brandon", event=True),
    LocationData("Lightning Club Main Hall", "Brandon Rematch Reward 1", "Colosseum Pack", rom_addresses["Brandon Rematch Reward 1"]),
    LocationData("Lightning Club Main Hall", "Brandon Rematch Reward 2", "Colosseum Pack", rom_addresses["Brandon Rematch Reward 2"]),
    LocationData("Lightning Club Main Hall", "Jennifer Reward 1", "Mystery Pack", rom_addresses["Jennifer Reward 1"]),
    LocationData("Lightning Club Main Hall", "Jennifer Reward 2", "Mystery Pack", rom_addresses["Jennifer Reward 2"]),
    LocationData("Lightning Club Main Hall", "Beat Jennifer", "Beat Jennifer", event=True),
    LocationData("Lightning Club Main Hall", "Jennifer Rematch Reward 1", "Mystery Pack", rom_addresses["Jennifer Rematch Reward 1"]),
    LocationData("Lightning Club Main Hall", "Jennifer Rematch Reward 2", "Mystery Pack", rom_addresses["Jennifer Rematch Reward 2"]),
    LocationData("Lightning Club Main Hall", "Isaac Reward 1", "Mystery Pack", rom_addresses["Isaac Reward 1"]),
    LocationData("Lightning Club Main Hall", "Isaac Reward 2", "Mystery Pack", rom_addresses["Isaac Reward 2"]),
    LocationData("Lightning Club Main Hall", "Beat Isaac", "Beat Isaac", event=True),
    LocationData("Lightning Club Main Hall", "Isaac Rematch Reward 1", "Mystery Pack", rom_addresses["Isaac Rematch Reward 1"]),
    LocationData("Lightning Club Main Hall", "Isaac Rematch Reward 2", "Mystery Pack", rom_addresses["Isaac Rematch Reward 2"]),

    LocationData("Psychic Club Main Hall", "Daniel Reward 1", "Evolution Pack", rom_addresses["Daniel Reward 1"]),
    LocationData("Psychic Club Main Hall", "Daniel Reward 2", "Evolution Pack", rom_addresses["Daniel Reward 2"]),
    LocationData("Psychic Club Main Hall", "Beat Daniel", "Beat Daniel", event=True),
    LocationData("Psychic Club Main Hall", "Daniel Rematch Reward 1", "Evolution Pack", rom_addresses["Daniel Rematch Reward 1"]),
    LocationData("Psychic Club Main Hall", "Daniel Rematch Reward 2", "Evolution Pack", rom_addresses["Daniel Rematch Reward 2"]),
    LocationData("Psychic Club Main Hall", "Stephanie Reward 1", "Laboratory Pack", rom_addresses["Stephanie Reward 1"]),
    LocationData("Psychic Club Main Hall", "Stephanie Reward 2", "Laboratory Pack", rom_addresses["Stephanie Reward 2"]),
    LocationData("Psychic Club Main Hall", "Beat Stephanie", "Beat Stephanie", event=True),
    LocationData("Psychic Club Main Hall", "Stephanie Rematch Reward 1", "Laboratory Pack", rom_addresses["Stephanie Rematch Reward 1"]),
    LocationData("Psychic Club Main Hall", "Stephanie Rematch Reward 2", "Laboratory Pack", rom_addresses["Stephanie Rematch Reward 2"]),
    LocationData("Psychic Club Lounge", "Robert Reward 1", "Evolution Pack", rom_addresses["Robert Reward 1"]),
    LocationData("Psychic Club Lounge", "Robert Reward 2", "Evolution Pack", rom_addresses["Robert Reward 2"]),
    LocationData("Psychic Club Lounge", "Beat Robert", "Beat Robert", event=True),
    LocationData("Psychic Club Lounge", "Robert Rematch Reward 1", "Evolution Pack", rom_addresses["Robert Rematch Reward 1"]),
    LocationData("Psychic Club Lounge", "Robert Rematch Reward 2", "Evolution Pack", rom_addresses["Robert Rematch Reward 2"]),
    LocationData("Psychic Club Main Hall", "Murray Reward 1", "Laboratory Pack", rom_addresses["Murray Reward 1"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Murray Reward 2", "Laboratory Pack", rom_addresses["Murray Reward 2"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Beat Murray", "Beat Murray", event=True),
    LocationData("Psychic Club Main Hall", "Murray Rematch Reward 1", "Laboratory Pack", rom_addresses["Murray Rematch Reward 1"]), # Requires 4 medals
    LocationData("Psychic Club Main Hall", "Murray Rematch Reward 2", "Laboratory Pack", rom_addresses["Murray Rematch Reward 2"]), # Requires 4 medals

    LocationData("Rock Club Main Hall", "Ryan Reward 1", "Evolution Pack", rom_addresses["Ryan Reward 1"]),
    LocationData("Rock Club Main Hall", "Ryan Reward 2", "Evolution Pack", rom_addresses["Ryan Reward 2"]),
    LocationData("Rock Club Main Hall", "Beat Ryan", "Beat Ryan", event=True),
    LocationData("Rock Club Main Hall", "Ryan Rematch Reward 1", "Evolution Pack", rom_addresses["Ryan Rematch Reward 1"]),
    LocationData("Rock Club Main Hall", "Ryan Rematch Reward 2", "Evolution Pack", rom_addresses["Ryan Rematch Reward 2"]),
    LocationData("Rock Club Main Hall", "Andrew Reward 1", "Colosseum Pack", rom_addresses["Andrew Reward 1"]),
    LocationData("Rock Club Main Hall", "Andrew Reward 2", "Colosseum Pack", rom_addresses["Andrew Reward 2"]),
    LocationData("Rock Club Main Hall", "Beat Andrew", "Beat Andrew", event=True),
    LocationData("Rock Club Main Hall", "Andrew Rematch Reward 1", "Colosseum Pack", rom_addresses["Andrew Rematch Reward 1"]),
    LocationData("Rock Club Main Hall", "Andrew Rematch Reward 2", "Colosseum Pack", rom_addresses["Andrew Rematch Reward 2"]),
    LocationData("Rock Club Lounge", "Matthew Reward 1", "Mystery Pack", rom_addresses["Matthew Reward 1"]),
    LocationData("Rock Club Lounge", "Matthew Reward 2", "Mystery Pack", rom_addresses["Matthew Reward 2"]),
    LocationData("Rock Club Main Hall", "Beat Matthew", "Beat Matthew", event=True),
    LocationData("Rock Club Lounge", "Matthew Rematch Reward 1", "Mystery Pack", rom_addresses["Matthew Rematch Reward 1"]),
    LocationData("Rock Club Lounge", "Matthew Rematch Reward 2", "Mystery Pack", rom_addresses["Matthew Rematch Reward 2"]),
    LocationData("Rock Club Main Hall", "Gene Reward 1", "Mystery Pack", rom_addresses["Gene Reward 1"]),
    LocationData("Rock Club Main Hall", "Gene Reward 2", "Mystery Pack", rom_addresses["Gene Reward 2"]),
    LocationData("Rock Club Main Hall", "Beat Gene", "Beat Gene", event=True),
    LocationData("Rock Club Main Hall", "Gene Rematch Reward 1", "Mystery Pack", rom_addresses["Gene Rematch Reward 1"]),
    LocationData("Rock Club Main Hall", "Gene Rematch Reward 2", "Mystery Pack", rom_addresses["Gene Rematch Reward 2"]),

    LocationData("Fire Club Lounge", "Jessica Reward 1", "Colosseum Pack", rom_addresses["Jessica Reward 1"]),
    LocationData("Fire Club Lounge", "Jessica Reward 2", "Colosseum Pack", rom_addresses["Jessica Reward 2"]),
    LocationData("Fire Club Lounge", "Beat Jessica", "Beat Jessica", event=True),
    LocationData("Fighting Club Main Hall", "Jessica Rematch Reward 1", "Colosseum Pack", rom_addresses["Jessica Rematch Reward 1"]),
    LocationData("Fighting Club Main Hall", "Jessica Rematch Reward 2", "Colosseum Pack", rom_addresses["Jessica Rematch Reward 2"]),
    LocationData("Grass Club Lobby", "Michael Reward 1", "Colosseum Pack", rom_addresses["Michael Reward 1"]),
    LocationData("Grass Club Lobby", "Michael Reward 2", "Colosseum Pack", rom_addresses["Michael Reward 2"]),
    LocationData("Grass Club Lobby", "Beat Michael", "Beat Michael", event=True),
    LocationData("Fighting Club Main Hall", "Michael Rematch Reward 1", "Colosseum Pack", rom_addresses["Michael Rematch Reward 1"]),
    LocationData("Fighting Club Main Hall", "Michael Rematch Reward 2", "Colosseum Pack", rom_addresses["Michael Rematch Reward 2"]),
    LocationData("Rock Club Lounge", "Chris Reward 1", "Evolution Pack", rom_addresses["Chris Reward 1"]),
    LocationData("Rock Club Lounge", "Chris Reward 2", "Evolution Pack", rom_addresses["Chris Reward 2"]),
    LocationData("Rock Club Lounge", "Beat Chris", "Beat Chris", event=True),
    LocationData("Fighting Club Main Hall", "Chris Rematch Reward 1", "Evolution Pack", rom_addresses["Chris Rematch Reward 1"]),
    LocationData("Fighting Club Main Hall", "Chris Rematch Reward 2", "Evolution Pack", rom_addresses["Chris Rematch Reward 2"]),
    LocationData("Fighting Club Main Hall", "Mitch Reward 1", "Laboratory Pack", rom_addresses["Mitch Reward 1"]),
    LocationData("Fighting Club Main Hall", "Mitch Reward 2", "Laboratory Pack", rom_addresses["Mitch Reward 2"]),
    LocationData("Fighting Club Main Hall", "Beat Mitch", "Beat Mitch", event=True),
    LocationData("Fighting Club Main Hall", "Mitch Rematch Reward 1", "Laboratory Pack", rom_addresses["Mitch Rematch Reward 1"]),
    LocationData("Fighting Club Main Hall", "Mitch Rematch Reward 2", "Laboratory Pack", rom_addresses["Mitch Rematch Reward 2"]),

    LocationData("Grass Club Main Hall", "Grass Medal", "Grass Medal", rom_addresses["Grass Medal"]),
    LocationData("Science Club Main Hall", "Science Medal", "Science Medal", rom_addresses["Science Medal"]),
    LocationData("Water Club Main Hall", "Water Medal", "Water Medal", rom_addresses["Water Medal"]),
    LocationData("Fire Club Main Hall", "Fire Medal", "Fire Medal", rom_addresses["Fire Medal"]),
    LocationData("Lightning Club Main Hall", "Lightning Medal", "Lightning Medal", rom_addresses["Lightning Medal"]),
    LocationData("Rock Club Main Hall", "Rock Medal", "Rock Medal", rom_addresses["Rock Medal"]),
    LocationData("Psychic Club Main Hall", "Psychic Medal", "Psychic Medal", rom_addresses["Psychic Medal"]),
    LocationData("Fighting Club Main Hall", "Fighting Medal", "Fighting Medal", rom_addresses["Fighting Medal"]),

    LocationData("Fighting Club Lounge", "Imakuni Reward 1", "Evolution Pack", rom_addresses["Imakuni Reward 1"]),
    LocationData("Science Club Lounge", "Imakuni Reward 2", "Laboratory Pack", rom_addresses["Imakuni Reward 2"]),
    LocationData("Lightning Club Lounge", "Imakuni Rematch Reward 1", "Colosseum Pack", rom_addresses["Imakuni Rematch Reward 1"]),
    LocationData("Water Club Lounge", "Imakuni Rematch Reward 2", "Mystery Pack", rom_addresses["Imakuni Rematch Reward 2"]),

    LocationData("Rock Club Lounge", "Ronald Reward 1", "Promo Mewtwo 1", rom_addresses["Ronald Reward 1"]), # 2 Medals
    LocationData("Fire Club Lounge", "Ronald Reward 2", "Promo Jigglypuff", rom_addresses["Ronald Reward 2"]), # 2 Medals
    LocationData("Grass Club Lounge", "Ronald Rematch Reward 1", "Promo Mew 1", rom_addresses["Ronald Rematch Reward 1"]), # 5 Medals
    LocationData("Psychic Club Lounge", "Ronald Rematch Reward 2", "Super Energy Retrieval Pack", rom_addresses["Ronald Rematch Reward 2"]), # 5 Medals

    LocationData("Pokemon Dome Main Hall", "Beat Courtney", "Beat Courtney", event=True),
    LocationData("Pokemon Dome Main Hall", "Beat Steve", "Beat Steve", event=True),
    LocationData("Pokemon Dome Main Hall", "Beat Jack", "Beat Jack", event=True),
    LocationData("Pokemon Dome Main Hall", "Beat Rod", "Beat Rod", event=True),
    LocationData("Pokemon Dome Main Hall", "Become Champion", "Become Champion", event=True),

    # Open the club main halls as an event
    LocationData("Water Club Lobby", "Open Water Club Door", "Water Club Door", event=True),
    LocationData("Fire Club Lobby", "Open Fire Club Door", "Fire Club Door", event=True),
    LocationData("Lightning Club Lobby", "Open Lightning Club Door", "Lightning Club Door", event=True),
    LocationData("Science Club Lobby", "Open Science Club Door", "Science Club Door", event=True),
    LocationData("Psychic Club Lobby", "Open Psychic Club Door", "Psychic Club Door", event=True),
    LocationData("Grass Club Lobby", "Open Grass Club Door", "Grass Club Door", event=True),
    LocationData("Rock Club Lobby", "Open Rock Club Door", "Rock Club Door", event=True),
    LocationData("Fighting Club Lobby", "Open Fighting Club Door", "Fighting Club Door", event=True),

    # Email logic
    LocationData("Mason Laboratory Center Room", "Email 1", "Colosseum Pack", rom_addresses["Email 1"]),
    LocationData("Mason Laboratory Center Room", "Email 2", "Evolution Pack", rom_addresses["Email 2"]),
    LocationData("Mason Laboratory Center Room", "Email 3", "Mystery Pack", rom_addresses["Email 3"]),
    LocationData("Mason Laboratory Center Room", "Email 4", "Laboratory Pack", rom_addresses["Email 4"]),
    LocationData("Mason Laboratory Center Room", "Email 5", "Colosseum Pack", rom_addresses["Email 5"]),
    LocationData("Mason Laboratory Center Room", "Email 6", "Evolution Pack", rom_addresses["Email 6"]),
    LocationData("Mason Laboratory Center Room", "Email 7", "Mystery Pack", rom_addresses["Email 7"]),
    LocationData("Mason Laboratory Center Room", "Email 8", "Laboratory Pack", rom_addresses["Email 8"]),
    LocationData("Mason Laboratory Center Room", "Email 9", "Promo Articuno", rom_addresses["Email 9"]),
    LocationData("Mason Laboratory Center Room", "Email 10", "Promo Zapdos", rom_addresses["Email 10"]),
    LocationData("Mason Laboratory Center Room", "Email 11", "Promo Moltres", rom_addresses["Email 11"]),
    LocationData("Mason Laboratory Center Room", "Email 12", "Promo Dragonite", rom_addresses["Email 12"]),
    LocationData("Mason Laboratory Center Room", "Email 13", "Promo Imakuni", rom_addresses["Email 13"]),
    LocationData("Mason Laboratory Center Room", "Email 14", "Promo Venusaur", rom_addresses["Email 14"]),
    LocationData("Mason Laboratory Center Room", "Email 15", "Promo Mew 2", rom_addresses["Email 15"]),

    # Promo cards
    LocationData("Psychic Club Lounge", "Promo Mewtwo Gift", "Promo Mewtwo 2", rom_addresses["Promo Mewtwo 2"]),
    LocationData("Fighting Club Lounge", "Promo Pikachu Trade (Fighting Club)", "Promo Pikachu 2", rom_addresses["Promo Pikachu 2"]),
    LocationData("Fire Club Lounge", "Promo Slowpoke Trade", "Promo Slowpoke", rom_addresses["Promo Slowpoke"]),
    LocationData("Lightning Club Lounge", "Promo Electabuzz Trade", "Promo Electabuzz", rom_addresses["Promo Electabuzz"]),
    LocationData("Water Club Lounge", "Promo Arcanine Trade", "Promo Arcanine", rom_addresses["Promo Arcanine"]),

    LocationData("Grass Club Lounge", "Lass Trade 1", "Energy Pack", rom_addresses["Lass Trade 1"]),
    LocationData("Grass Club Lounge", "Lass Trade 2", "Promo Pikachu 1", rom_addresses["Lass Trade 2"]),
    LocationData("Grass Club Lounge", "Lass Trade 3", "Energy Pack", rom_addresses["Lass Trade 3"]),
    LocationData("Ishihara's House", "Ishihara Trade 1", "Promo Flying Pikachu", rom_addresses["Promo Flying Pikachu"]),
    LocationData("Ishihara's House", "Ishihara Trade 2", "Promo Surfing Pikachu 1", rom_addresses["Promo Surfing Pikachu 1"]),
    LocationData("Ishihara's House", "Ishihara Trade 3", "Promo Surfing Pikachu 2", rom_addresses["Promo Surfing Pikachu 2"]),
]

class PokemonTCGLocation(Location):
    game = "Pokemon Trading Card Game"

    def __init__(self, player, name, address, rom_address):
        super(PokemonTCGLocation, self).__init__(
            player, name,
            address
        )
        self.rom_address = rom_address
