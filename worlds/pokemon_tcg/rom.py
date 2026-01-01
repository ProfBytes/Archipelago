import os
import pkgutil
import typing

import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from .data import card_ids, medal_ids, pack_to_card, card_list
from .options import PackType
from .rom_addresses import rom_addresses

class PokemonTCGProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon Trading Card Game"
    hash = "219b2cc64e5a052003015d4bd4c622cd"
    patch_file_ending = ".apptcg"
    result_file_ending = ".gbc"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        from . import PokemonTCGWorld
        with open(PokemonTCGWorld.settings.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes


char_map = {
    "\0": 0x00,  # String terminator
    "<": 0x05,
    ">": 0x20,
    "?": 0x3F,
    "!": 0x21,
    "&": 0x26,
    ",": 0x2C,
    ".": 0x2E,
    "'": 0x27,
    ";": 0x3B,
    "(": 0x28,
    ")": 0x29,
    "é": 0x60,
    "\n": 0x0A,
    " ": 0x20,

    "A": 0x41,
    "B": 0x42,
    "C": 0x43,
    "D": 0x44,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 0x53,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 0x57,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,

    "a": 0x61,
    "b": 0x62,
    "c": 0x63,
    "d": 0x64,
    "e": 0x65,
    "f": 0x66,
    "g": 0x67,
    "h": 0x68,
    "i": 0x69,
    "j": 0x6A,
    "k": 0x6B,
    "l": 0x6C,
    "m": 0x6D,
    "n": 0x6E,
    "o": 0x6F,
    "p": 0x70,
    "q": 0x71,
    "r": 0x72,
    "s": 0x73,
    "t": 0x74,
    "u": 0x75,
    "v": 0x76,
    "w": 0x77,
    "x": 0x78,
    "y": 0x79,
    "z": 0x7A,

    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
}

def encode_text(text: str, length: int=0, whitespace=True, force=False, safety=False):
    encoded_text = bytearray()
    for char in text:
        if char in char_map:
            encoded_text.append(char_map[char])
        else:
            encoded_text.append(char_map["é"])
    if length > 0:
        encoded_text = encoded_text[:length]
    while whitespace and len(encoded_text) < length:
        encoded_text.append(char_map[" " if whitespace is True else whitespace])
    return encoded_text

def get_card_bytes(card_dict: dict):
    bytes = []
    for key, value in card_dict.items():
        for i in range(value):
            bytes.append(card_ids[key])
    return bytes

def get_pack_bytes(card_dict: dict):
    bytes = []
    for key, value in card_dict.items():
        for i in range(value):
            bytes.append(card_ids[key])
    while len(bytes) < 60:
        bytes.append(0xff)
    return bytes

def get_deck_bytes(card_dict: dict):
    bytes = []
    for key, value in card_dict.items():
        bytes.append(value)
        bytes.append(card_ids[key])
    return bytes

def door_string(item: str):
    string = "a " + item
    return encode_text(string, 28)

def door_bytes(item: str):
    if item in card_ids:
        return card_ids[item]
    else:
        return medal_ids[item]

def door_requirement(item: str):
    if item in card_ids:
        return 0x01
    else:
        return 0x00


def make_item_string(item: str, player: str):
    full_string = "Sent {item} to {player}."
    while len(full_string) < 62:
        full_string = full_string + " "
    return encode_text("{full_string[:32]}\n{full_string[32:62]]}\0", 64)


def generate_output(world: "PokemonTCGWorld", output_directory: str):
    patch_type = PokemonTCGProcedurePatch
    patch = patch_type(player=world.player, player_name=world.player_name)
    patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, f"base_patch.bsdiff4"))

    def write_bytes(address: int, data: typing.Sequence[int] | int):
        if isinstance(data, int):
            data = bytes([data])
        else:
            data = bytes(data)

        patch.write_token(APTokenTypes.WRITE, address, data)

    deck_bytes = get_deck_bytes(world.options.starter_deck.value)
    deck_bytes.extend([0x00, 0xae, 0x0b])
    write_bytes(rom_addresses["Starter Deck"], deck_bytes)
    write_bytes(rom_addresses["Door Setting"], [1])
    write_bytes(rom_addresses["Door Strings Start"], door_string(world.options.fighting_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 28, door_string(world.options.rock_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 56, door_string(world.options.water_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 84, door_string(world.options.lightning_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 112, door_string(world.options.grass_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 140, door_string(world.options.psychic_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 168, door_string(world.options.science_club_unlock.value))
    write_bytes(rom_addresses["Door Strings Start"] + 196, door_string(world.options.fire_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"], door_requirement(world.options.fighting_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 1, door_requirement(world.options.rock_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 2, door_requirement(world.options.water_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 3, door_requirement(world.options.lightning_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 4, door_requirement(world.options.grass_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 5, door_requirement(world.options.psychic_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 6, door_requirement(world.options.science_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 7, door_requirement(world.options.fire_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 8, door_bytes(world.options.fighting_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 9, door_bytes(world.options.rock_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 10, door_bytes(world.options.water_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 11, door_bytes(world.options.lightning_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 12, door_bytes(world.options.grass_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 13, door_bytes(world.options.psychic_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 14, door_bytes(world.options.science_club_unlock.value))
    write_bytes(rom_addresses["Door Requirements Start"] + 15, door_bytes(world.options.fire_club_unlock.value))

    #"Reward Table": 0x6836a,  # 2 bytes per trainer for first and second matches.  Need more details to fill out

    for location in world.multiworld.get_locations(world.player):
        if location.is_event:
            continue
        trimmed = location.name.split(" - ")[1]
        write_bytes(rom_addresses[trimmed], 0xff)
        write_bytes(rom_addresses[trimmed] + 15332, make_item_string(location.item, location.player))
        write_bytes(rom_addresses[trimmed] + 178, location.item.classification)

    # if not world.options.medal_sanity:
    #     write_bytes(rom_addresses["Grass Medal"], 0xf0)
    #     write_bytes(rom_addresses["Science Medal"], 0xf1)
    #     write_bytes(rom_addresses["Fire Medal"], 0xf2)
    #     write_bytes(rom_addresses["Water Medal"], 0xf3)
    #     write_bytes(rom_addresses["Lightning Medal"], 0xf4)
    #     write_bytes(rom_addresses["Psychic Medal"], 0xf5)
    #     write_bytes(rom_addresses["Rock Medal"], 0xf6)
    #     write_bytes(rom_addresses["Fighting Medal"], 0xf7)

    if world.options.pack_type == PackType.option_evoline:
        index = 0
        for pack_name, pack_contents in pack_to_card.items():
            write_bytes(rom_addresses["Booster Table"] + index*60, get_pack_bytes(pack_contents))
            index = index + 1
        while index < 238:
            write_bytes(rom_addresses["Booster Table"] + index*60, get_pack_bytes({}))
            index = index + 1

    rom_name = bytearray(f"AP{Utils.__version__.replace('.', '')[0:3]}_{world.player}_{world.multiworld.seed:11}\0",
                         "utf8")[:21]
    rom_name.extend([0] * (21 - len(rom_name)))
    write_bytes(rom_addresses["ROM Name"], rom_name)
    write_bytes(rom_addresses["Seed Name"], world.multiworld.seed_name.encode())
    write_bytes(rom_addresses["Slot Name"], world.multiworld.player_name[world.player].encode())

    patch.write_file("token_data.bin", patch.get_token_binary())
    out_file_name = world.multiworld.get_out_file_name_base(world.player)
    patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
