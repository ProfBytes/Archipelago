import random

from .items import packs, medals, masters_talkable
from .data import card_to_pack, pack_to_card, common_count, uncommon_count, rare_count, pack_contents, offsets
from .card_points import card_points, pokemon_lookup

def get_card_list(state, world, player):
    cards = world.options.starter_deck
    seed = world.options.pack_seed
    for pack in pack_to_card:
        for card, count in pack:
            if not card in cards:
                cards[card] = count
            else:
                cards[card] += count
    for pack in ["Colosseum Pack", "Laboratory Pack", "Mystery Pack", "Evolution Pack"]:
        count = state.count(pack, player)
        offset = offsets[pack]
        common_list = pack_contents[pack]["common"].copy()
        uncommon_list = pack_contents[pack]["uncommon"].copy()
        rare_list = pack_contents[pack]["rare"].copy()
        random.shuffle(common_list, random.seed(seed + offset))
        random.shuffle(uncommon_list, random.seed(seed + offset + 17))
        random.shuffle(rare_list, random.seed(seed + offset + 68))
        for i in range(0, min(count * common_count, len(common_list))):
            if not common_list[i] in cards:
                cards[common_list[i]] = 1
            else:
                cards[common_list[i]] += 1
        for i in range(0, min(count  * uncommon_count, len(uncommon_list))):
            if not uncommon_list[i] in cards:
                cards[uncommon_list[i]] = 1
            else:
                cards[uncommon_list[i]] += 1
        for i in range(0, min(count  * rare_count, len(rare_list))):
            if not rare_list[i] in cards:
                cards[rare_list[i]] = 1
            else:
                cards[rare_list[i]] += 1
    return cards

def has_type(state, world, player, type, number):
    cards = get_card_list(state, world, player)
    value = 0

    for pokemon in pokemon_lookup:
        values = {}
        total = 0
        for card in pokemon:
            values[card] = {
                "count": cards[card],
                "points": card_points[card]["value"]
            }
            total += cards[card]
        while total > 4:
            lowest_card = pokemon[0]
            lowest_value = values[lowest_card]["points"]
            lowest_count = values[lowest_card]["count"]
            for card in pokemon:
                if lowest_count == 0 or lowest_value > values[lowest_card]["points"]:
                    lowest_card = card
                    lowest_value = values[lowest_card]["points"]
                    lowest_count = values[lowest_card]["count"]
            to_remove = min(total-4, values[lowest_card]["count"])
            values[lowest_card]["count"] -= to_remove
            total -= to_remove

        for card, dict in values:
            cards[card] = dict["count"]

    for card, count in cards:
        max_valid = 4
        if card_points[card]["type"] == type:
            prevolutions = card_points[card]["pokemon"]
            for pokemon in prevolutions:
                if pokemon == "Not":
                    continue
                cards = pokemon_lookup[pokemon]
                total = 0
                for card_name in cards:
                    total += cards[card_name]
                if len(cards) == 0:
                    total = 4
                max_valid = min(max_valid, total)
            value += card_points[card]["value"] * min(count, max_valid)
    return value >= number


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

    if state.has("Beat Rod", player):
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
    cards = get_card_list(state, world, player)
    return card in cards

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