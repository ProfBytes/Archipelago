from dataclasses import dataclass
from Options import (PerGameCommonOptions, Toggle, Choice, Range, NamedRange, FreeText, TextChoice, DeathLink,
                     ItemsAccessibility)


class MedalSanity(Toggle):
    """Shuffle gym badges into the general item pool. If turned off, badges will be shuffled across the 8 gyms."""
    display_name = "Medalsanity"
    default = 0


class PackType(Choice):
    """"""
    display_name = "Pack Types"
    option_vanilla = 0
    option_evoline = 1
    default = 1

class StartingDeck1(Choice):
    """Select the primary type for your starting deck.
    Selecting the same type multiple times will randomize the secondary or tertiary type"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 0

class StartingDeck2(Choice):
    """Select the secondary type for your starting deck.
    Selecting the same type multiple times will randomize the secondary or tertiary type"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 1

class StartingDeck3(Choice):
    """Select the tertiary type for your starting deck.
    Selecting the same type multiple times will randomize the secondary or tertiary type"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 2

class GrandMasterMedalCount(Range):
    """How many medals do you need to open the Grand Master fights"""
    display_name = "Grand Master Medal Count"
    range_start = 0
    range_end = 8
    default = 8

class OpenDoors(Range):
    """How many of the Club doors start unlocked"""
    display_name = "Open Club Door Count"
    range_start = 0
    range_end = 8
    default = 0

class WaterClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class FireClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class GrassClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class LightningClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class RockClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class FightingClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class PsychicClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class ScienceClubUnlock(FreeText):
    """"""
    visibility = Visibility.all & ~Visibility.simple_ui
    default = "random"

class SpecialDeck(FreeText):
    """"""
    visibility = Visibility.none
    default = "Nothing to see here"

class StarterDeck(OptionDict):
    """"""
    visibility = Visibility.none
    default = "Nothing to see here"

@dataclass
class PokemonTCGOptions(PerGameCommonOptions):
    accessibility: ItemsAccessibility
    pack_type: PackType
    medal_sanity: MedalSanity
    starting_deck_1: StartingDeck1
    starting_deck_2: StartingDeck2
    starting_deck_3: StartingDeck3
    water_club_unlock: WaterClubUnlock
    fire_club_unlock: FireClubUnlock
    grass_club_unlock: GrassClubUnlock
    rock_club_unlock: RockClubUnlock
    lightning_club_unlock: LightningClubUnlock
    fighting_club_unlock: FightingClubUnlock
    psychic_club_unlock: PsychicClubUnlock
    science_club_unlock: ScienceClubUnlock
    grand_master_medal_count: GrandMasterMedalCount
    open_doors: OpenDoors
    special_deck: SpecialDeck
    starter_deck: StarterDeck