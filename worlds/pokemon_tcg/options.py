from dataclasses import dataclass
from Options import (PerGameCommonOptions, Toggle, Choice, Range, FreeText, ItemsAccessibility, Visibility, OptionSet)


class MedalSanity(Toggle):
    """Shuffle gym badges into the general item pool. If turned off, badges will be shuffled across the 8 gyms."""
    display_name = "Medalsanity"
    default = 0


class PackType(Choice):
    """"""
    display_name = "Pack Types"
    option_vanilla = 0
    option_evoline = 1
    option_decks = 2
    option_mixed = 3
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


class StarterDeck(FreeText):
    """"""
    visibility = Visibility.none
    default = "Nothing to see here"


class PsychicClubTrade(FreeText):
    """"""
    visibility = Visibility.none
    default = "Psychic Medal"


class FireClubTrade(Range):
    """"""
    visibility = Visibility.none
    range_start = 0
    range_end = 8
    default = 3


class FightingClubTrade(OptionSet):
    """"""
    visibility = Visibility.none
    default = ["Rapidash", "Omastar", "Graveler", "Parasect", "Weezing"]


class LightningClubTrade(FreeText):
    """"""
    visibility = Visibility.none
    default = "Electabuzz Lv35"


class WaterClubTrade(FreeText):
    """"""
    visibility = Visibility.none
    default = "Lapras"


class GrassClubTrade1(FreeText):
    """"""
    visibility = Visibility.none
    default = "Oddish"


class GrassClubTrade2(FreeText):
    """"""
    visibility = Visibility.none
    default = "Clefairy"


class GrassClubTrade3(FreeText):
    """"""
    visibility = Visibility.none
    default = "Charizard"


class IshiharaTrade1(FreeText):
    """"""
    visibility = Visibility.none
    default = "Clefable"


class IshiharaTrade2(FreeText):
    """"""
    visibility = Visibility.none
    default = "Ditto"


class IshiharaTrade3(FreeText):
    """"""
    visibility = Visibility.none
    default = "Chansey"

class PackSeed(Range):
    """Seed for generating random packs"""
    display_name = "Pack generator seed"
    range_start = 0
    range_end = 1000000000
    default = "random"


@dataclass
class PokemonTCGOptions(PerGameCommonOptions):
    accessibility: ItemsAccessibility
    pack_type: PackType
    medal_sanity: MedalSanity
    starting_deck_1: StartingDeck1
    starting_deck_2: StartingDeck2
    starting_deck_3: StartingDeck3
    pack_seed: PackSeed
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
    psychic_club_trade: PsychicClubTrade
    fighting_club_trade: FightingClubTrade
    fire_club_trade: FireClubTrade
    lightning_club_trade: LightningClubTrade
    water_club_trade: WaterClubTrade
    grass_club_trade_1: GrassClubTrade1
    grass_club_trade_2: GrassClubTrade2
    grass_club_trade_3: GrassClubTrade3
    ishihara_trade_1: IshiharaTrade1
    ishihara_trade_2: IshiharaTrade2
    ishihara_trade_3: IshiharaTrade3
