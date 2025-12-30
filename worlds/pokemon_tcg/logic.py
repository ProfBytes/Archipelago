from .items import packs, medals, masters_talkable
from .data import card_to_pack, pack_to_card

def has_type(state, world, player, type, number):
    return (len([item for item in packs[type] if state.has(item, player)]) + starting_deck_has_type(type) >= number) or \
        (world.options.pack_type.value == 'vanilla' and has_enough_packs(state, world, player, number*number))

def has_enough_packs(state, world, player, number):
    return number <= (state.count("Colosseum Pack") + state.count("Mystery Pack") +
                      state.count("Laboratory Pack") + state.count("Evolution Pack"))

def starting_deck_has_type(state, world, player, type):
    if world.options.starting_deck_type_1 == type or world.options.starting_deck_type_2 == type or world.options.starting_deck_type_3 == type:
        return 2
    return 0

def medal_count(state, world, player):
    return len([item for item in medals if state.has(item, player)])

def card_count(state, world, player):
    #TODO FIX
    return 540 + sum(value for key, value in pack_to_card if state.has(key, player))

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
    return good_trainer_count(state, world, player) >= 4

def grand_master_logic(state, world, player):
    return good_trainer_count(state, world, player) >= 10

def ronald_logic(state, world, player):
    return good_trainer_count(state, world, player) >= 2

def good_trainer_count(state, world, player):
    total = state.count("Computer Search Pack", player)
    total += state.count("Gust of Wind Pack", player)
    total += state.count("Pluspower Pack", player)

    total += state.count("Bill Pack", player)
    total += state.count("Professor Oak Pack", player)
    total += state.count("Super Energy Removal Pack", player)
    total += state.count("Double Colorless Energy Pack", player)
    return total

def has_card(state, world, player, card):
    if card == "Fire Energy":
        return True
    if world.options.pack_type.value == "Evoline":
        packs = card_to_pack[card]
        return any([pack == "Starter Deck" or state.has(pack) for pack in packs])
    else:
        return False

def has_all_cards(state, world, player, card_list):
    for card in card_list:
        if not has_card(state, world, player, card):
            return False
    return True

def has_item(state, world, player, item):
    if item == "Nothing":
        return True
    if item in medals:
        return state.has(item, player)
    return has_card(state, world, player, item)