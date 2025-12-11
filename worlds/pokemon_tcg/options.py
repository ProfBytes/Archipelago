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
    """"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 0

class StartingDeck2(Choice):
    """"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 1

class StartingDeck3(Choice):
    """"""
    display_name = "Pack Types"
    option_fire = 0
    option_grass = 1
    option_water = 2
    option_lightning = 3
    option_psychic = 4
    option_fighting = 5
    default = 2


@dataclass
class PokemonTCGOptions(PerGameCommonOptions):
    accessibility: ItemsAccessibility
    pack_type: PackType
    medal_sanity: MedalSanity
    starting_deck_1: StartingDeck1
    starting_deck_2: StartingDeck2
    starting_deck_3: StartingDeck3