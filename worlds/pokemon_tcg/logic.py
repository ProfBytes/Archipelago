from items import packs, medals, pack_counts, doors, masters_talkable
from data import evoline

def has_type(state, world, player, type, number):
    return (len([item for item in packs[type] if state.has(item, player)]) + starting_deck_has_type(type) >= number) or \
        (world.options.pack_types.value == 'vanilla' and has_enough_packs(state, world, player, number*number))

def has_enough_packs(state, world, player, number):
    return number <= (state.count("Colosseum Pack") + state.count("Mystery Pack") +
                      state.count("Laboratory Pack") + state.count("Evolution Pack"))

def starting_deck_has_type(state, world, player, type):
    if world.options.starting_deck_type_1 == type or world.options.starting_deck_type_2 == type or world.options.starting_deck_type_3 == type:
        return 1
    return 0

def medal_count(state, world, player):
    return len([item for item in medals if state.has(item, player)])

def card_count(state, world, player):
    return 540 + sum(value for key, value in pack_counts if state.has(key, player))

def masters_talkable_count(state, world, player):
    return len([event for event in masters_talkable if state.has(event, player)])

def email_count(state, world, player):
    emails_available = 1
    emails_available += (medal_count(state, world, player) + 1) // 4
    emails_available += masters_talkable_count(state, world, player)

    if state.has("Defeat Rod"):
        emails_available += 4
    return emails_available

def club_leader_logic(state, world, player):
    return good_trainer_count() >= 4

def grand_master_logic(state, world, player):
    return good_trainer_count() >= 10

def ronald_logic(state, world, player):
    return good_trainer_count() >= 2

def good_trainer_count(state, world, player):
    total = state.count("Computer Search Pack")
    total += state.count("Gust of Wind Pack")
    total += state.count("Pluspower Pack")

    total += state.count("Bill Pack")
    total += state.count("Professor Oak Pack")
    total += state.count("Super Energy Removal Pack")
    total += state.count("Double Colorless Energy Pack")
    return total

def has_card(state, world, player, card):
    if world.options.pack_types == "Evoline":
        packs = evoline[card]
        return any([pack == "Starter Deck" or state.has(pack) for pack in packs])
    else:
        return False