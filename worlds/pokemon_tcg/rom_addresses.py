rom_addresses = {
    "Starter Deck": 0x309a0,
    "Door Setting": 0x03ff6,
    "Door Strings Start": 0x64bde, #Must be 28 bytes, all in a row
    "Door Requirements Start": 0x6835a, #first 8 bytes is type (0 = medal, 1 = card), next 8 are the ID
    "Reward Table": 0x6836a, #2 bytes per trainer for first and second matches.  Need more details to fill out
    "AP Item Table": 0x6841c, # 2 bytes per trainer.  Order is trainer first, empty slots, trainer second, empty, medal replacement, mail, trade
    "AP Item Type": 0x684ce, # 2 bytes per trainer.  +1 for filler, +2 for prog, +4 for useful, +8 for trap, $ff for no item
    "AP Reward Text Table": 0x6c000, # 64 bytes.  32 bytes for first line, new character, 30 bytes for second line, string terminator character
    "Booster Table": 0x7c012, # 238 slots each holding 60 cards.
}
