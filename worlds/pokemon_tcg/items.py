from BaseClasses import ItemClassification
from .poke_data import pokemon_data


class ItemData:
    def __init__(self, item_id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if item_id is None else item_id + 172000000

# Soft limit of 22 cards per pack
# Hard cap of 128.  Unknown if soft limit can be bypassed currently
item_table = {
    "Colosseum Pack": ItemData(35, ItemClassification.progression, ["Pack"]),
    "Laboratory Pack": ItemData(35, ItemClassification.progression, ["Pack"]),
    "Mystery Pack": ItemData(35, ItemClassification.progression, ["Pack"]),
    "Evolution Pack": ItemData(35, ItemClassification.progression, ["Pack"]),
    "Promo Arcanine": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Moltres": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Articuno": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Pikachu 1": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Pikachu 2": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Flying Pikachu": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Surfing Pikachu 1": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Surfing Pikachu 2": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Electabuzz": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Zapdos": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Slowpoke": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Mewtwo 1": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Mewtwo 2": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Mew 1": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Jigglypuff": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Dragonite": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Imakuni": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Super Energy Retrieval": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Venusaur": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Promo Mew 2": ItemData(1, ItemClassification.progression, ["Pack"]),

    "Aerodactyle Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Dugtrio Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Golem Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Hitmonchan Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Hitmonlee Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Kabutops Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Machamp Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Marowak 1 Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Marowak 2 Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Onix Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Primeape Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Rhydon Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),
    "Sandslash Pack": ItemData(1, ItemClassification.progression, ["Fighting", "Pack"]),

    "Alakazam Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Gengar 1 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Gengar 2 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Hypno Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Jynx Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 1 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 2 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 3 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 1 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 2 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 3 Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mr Mime Pack": ItemData(1, ItemClassification.progression, ["Psychic", "Pack"]),

    "Arbok Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Beedrill Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Butterfree Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Exeggutor Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Golbat Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Muk Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Nidoking Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Nidoqueen Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Parasect Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Pinsir Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Scyther Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Tangela 1 Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Tangela 2 Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Venomoth Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Venusaur 1 Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Venusaur 2 Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Victreebel Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Vileplume Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),
    "Weezing Pack": ItemData(1, ItemClassification.progression, ["Grass", "Pack"]),

    "Arcanine 1 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Arcanine 2 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Charizard Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Flareon 1 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Flareon 2 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Magmar 1 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Magmar 2 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Moltres 1 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Moltres 2 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Ninetales 1 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Ninetales 2 Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),
    "Rapidash Pack": ItemData(1, ItemClassification.progression, ["Fire", "Pack"]),

    "Articuno 1 Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Articuno 2 Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Blastoise Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Cloyster Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Dewgong Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Golduck Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Gyrados Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Kingler Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Lapras Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Omastar Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Poliwrath Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Seadra Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Seaking Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Slowbrow Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Slowpoke Promo Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Starmie Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Tentacruel Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Vaporeon 1 Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),
    "Vaporeon 2 Pack": ItemData(1, ItemClassification.progression, ["Water", "Pack"]),

    "Chansey Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Clefable Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Ditto Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Dodrio Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Dragonite 1 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Dragonite 2 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Farfetch'd Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Fearow Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Jigglypuff Promo Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Kangaskhan Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Lickitung Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Persian 1 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Persian 2 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Pidgeot 1 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Pidgeot 2 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Porygon Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Raticate Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Snorlax Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Tauros Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Wigglytuff 1 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),
    "Wigglytuff 2 Pack": ItemData(1, ItemClassification.progression, ["Normal", "Pack"]),

    "Electabuzz 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electabuzz 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electrode 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electrode 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Flying Pikachu Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Jolteon 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Jolteon 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Magneton 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Magneton 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 3 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 4 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Surfing Pikachu 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Surfing Pikachu 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 1 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 2 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 3 Pack": ItemData(1, ItemClassification.progression, ["Lightning", "Pack"]),

    "Clefairy Doll Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Defender Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Devolution Spray Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Removal Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Retrieval Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Search Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Full Heal Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Gambler Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Imakuni? Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Imposter Professor Oak Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Item Finder Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Lass Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Maintenance Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Mr Fuji Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Poke Ball Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokedex Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Breeder Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Center Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Flute Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Trader Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Potion Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Recycle Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Revive Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Energy Retrieval Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Potion Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),
    "Switch Pack": ItemData(1, ItemClassification.progression, ["Trainer", "Pack"]),

    "Computer Search Pack": ItemData(2, ItemClassification.progression, ["Trainer", "Pack"]),
    "Gust of Wind Pack": ItemData(2, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pluspower Pack": ItemData(2, ItemClassification.progression, ["Trainer", "Pack"]),

    "Bill Pack": ItemData(4, ItemClassification.progression, ["Trainer", "Pack"]),
    "Professor Oak Pack": ItemData(4, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Energy Removal Pack": ItemData(4, ItemClassification.progression, ["Trainer", "Pack"]),
    "Double Colorless Energy Pack": ItemData(4, ItemClassification.useful, ["Energy", "Pack"]),

    "Energy Pack": ItemData(1, ItemClassification.filler, ["Energy", "Pack"]),

    # Colosseum packs
    # Nidoran♂, Nidorino
    # Tangela
    # Scyther
    # Pinsir
    # Charmander, Charmeleon
    # Growlithe, Arcanine
    # Ponyta
    # Magmar
    # Seel, Dewgong
    # Goldeen, Seaking
    # Staryu
    # Magikarp, Gyrados
    # Pikachu, Raichu
    # Magnemite, Magneton
    # Electabuzz
    # Zapdos
    # Diglett, Dugtrio
    # Machop
    # Hitmonchan
    # Abra, Kadabra
    # Rattata, Raticate
    # Jigglypuff, Wigglytuff
    # Meowth
    # Chansey
    # Kangaskhan
    # Snorlax
    # Trainers: Professor Oak, Bill, Switch, Poke Ball, Scoop Up, Computer Search, Plus Power, Defender, Item Finder, Potion, Full Heal, Revive

    # Evolution packs

    # Bulbasaur, Ivysaur, Venusaur
    # Caterpie, Metapod, Butterfree
    # Weedle, Kakuna, Beedrill
    # Nidoking
    # Bellsprout, Weepinbell, Victreebel
    # Charizard
    # Rapidash
    # Flareon
    # Squirtle, Wartortle, Blastoise
    # Krabby, Kingler
    # Starmie
    # Vaporeon
    # Jolteon
    # Sandshrew, Sandslash
    # Machoke, Machamp
    # Geodude, Graveler, Golem
    # Cubone, Marowak
    # Gastly, Haunter, Gengar
    # Jynx
    # Pidgey, Pidgeotto, Pidgeot
    # Jigglypuff
    # Eevee
    # Trainers: Pokemon Trader, Pokemon Breeder, Clefairy Doll, Energy Retrieval, Energy Search, Gust of Wind, Super Potion, Pokemon Flute

    # Mystery Packs

    # Nidoran♀, Nidorina, Nidoqueen
    # Oddish, Gloom, Vileplume
    # Paras, Parasect
    # Exeggcute, Exeggutor
    # Vulpix, Ninetales
    # Flareon
    # Moltres
    # Shellder, Cloyster
    # Lapras
    # Vaporeon
    # Omanyte, Omastar
    # Articuno
    # Pikachu, Raichu
    # Voltorb, Electrode
    # Jolteon
    # Zapdos
    # Mankey, Primeape
    # Rhyhorn, Rhydon
    # Kabuto, Kabutops
    # Aerodactyl
    # Alakazam
    # Drowzee
    # Mew
    # Clefairy
    # Meowth, Persian
    # Farfetch'd
    # Lickitung
    # Tauros
    # Dratini, Dragonair, Dragonite
    # Trainers: Mr. Fuji, Mysterious Fossil, Energy Removal, Pokemon Center, Double Colorless Energy

    # Laboratory cards

    # Ekands, Arbok
    # Zubat, Golbat
    # Venonat, Venomoth
    # Grimer, Muk
    # Koffing, Weezing
    # Tangela
    # Ninetales
    # Magmar
    # Psyduck, Golduck
    # Poliwag, Poliwhirl, Poliwrath
    # Tentacool, Tentacruel
    # Horsea, Seadra
    # Magnemite, Magneton
    # Electrode
    # Onix
    # Marowak
    # Hitmonlee
    # Slowpoke, Slowbro
    # Gastly, Haunter
    # Hypno
    # Mr. Mime
    # Mewtwo
    # Pidgeot
    # Spearow, Fearow
    # Clefable
    # Doduo, Dodrio
    # Ditto
    # Porygon
    # Trainers: Impostor Professor Oak, Lass, Super Energy Removal, Pokedex, Devolution Spray, Maintenance, Gambler, Recycle

    # Promo cards
    # Arcanine
    # Moltres
    # Articuno
    # Pikachu
    # Pikachu
    # Flying Pikachu
    # Surfing Pikachu
    # Surfing Pikachu
    # Electabuzz
    # Zapdos
    # Slowpoke
    # Mewtwo
    # Mewtwo
    # Mew
    # Jigglypuff
    # Dragonite
    # Imakuni?
    # Super Energy Retrieval
    # Venusaur
    # Mew

    # "Master Ball": ItemData(1, ItemClassification.useful, ["Consumables", "Poke Balls"]),
    # "Ultra Ball": ItemData(2, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    # "Great Ball": ItemData(3, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    # "Poke Ball": ItemData(4, ItemClassification.filler, ["Consumables", "Poke Balls"]),
    # "Town Map": ItemData(5, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    # "Bicycle": ItemData(6, ItemClassification.progression, ["Unique", "Key Items"]),
    # # "Flippers": ItemData(7, ItemClassification.progression),
    # # "Safari Ball": ItemData(8, ItemClassification.filler),
    # "Pokedex": ItemData(9, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Moon Stone": ItemData(10, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    # "Antidote": ItemData(11, ItemClassification.filler, ["Consumables"]),
    # "Burn Heal": ItemData(12, ItemClassification.filler, ["Consumables"]),
    # "Ice Heal": ItemData(13, ItemClassification.filler, ["Consumables"]),
    # "Awakening": ItemData(14, ItemClassification.filler, ["Consumables"]),
    # "Paralyze Heal": ItemData(15, ItemClassification.filler, ["Consumables"]),
    # "Full Restore": ItemData(16, ItemClassification.filler, ["Consumables"]),
    # "Max Potion": ItemData(17, ItemClassification.filler, ["Consumables"]),
    # "Hyper Potion": ItemData(18, ItemClassification.filler, ["Consumables"]),
    # "Super Potion": ItemData(19, ItemClassification.filler, ["Consumables"]),
    # "Potion": ItemData(20, ItemClassification.filler, ["Consumables"]),
    # "Boulder Badge": ItemData(21, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Cascade Badge": ItemData(22, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Thunder Badge": ItemData(23, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Rainbow Badge": ItemData(24, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Soul Badge": ItemData(25, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Marsh Badge": ItemData(26, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Volcano Badge": ItemData(27, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Earth Badge": ItemData(28, ItemClassification.progression, ["Unique", "Key Items", "Badges"]),
    # "Escape Rope": ItemData(29, ItemClassification.filler, ["Consumables"]),
    # "Repel": ItemData(30, ItemClassification.filler, ["Consumables"]),
    # "Old Amber": ItemData(31, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    # "Fire Stone": ItemData(32, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    # "Thunder Stone": ItemData(33, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    # "Water Stone": ItemData(34, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    # "HP Up": ItemData(35, ItemClassification.filler, ["Consumables", "Vitamins"]),
    # "Protein": ItemData(36, ItemClassification.filler, ["Consumables", "Vitamins"]),
    # "Iron": ItemData(37, ItemClassification.filler, ["Consumables", "Vitamins"]),
    # "Carbos": ItemData(38, ItemClassification.filler, ["Consumables", "Vitamins"]),
    # "Calcium": ItemData(39, ItemClassification.filler, ["Consumables", "Vitamins"]),
    # "Rare Candy": ItemData(40, ItemClassification.filler, ["Consumables"]),
    # "Dome Fossil": ItemData(41, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    # "Helix Fossil": ItemData(42, ItemClassification.progression_skip_balancing, ["Unique", "Fossils", "Key Items"]),
    # "Secret Key": ItemData(43, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Bike Voucher": ItemData(45, ItemClassification.progression, ["Unique", "Key Items"]),
    # "X Accuracy": ItemData(46, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "Leaf Stone": ItemData(47, ItemClassification.progression_skip_balancing, ["Unique", "Evolution Stones", "Key Items"]),
    # "Card Key": ItemData(48, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Nugget": ItemData(49, ItemClassification.filler, []),
    # #"Laptop": ItemData(50, ItemClassification.useful, ["Unique"]),
    # "Poke Doll": ItemData(51, ItemClassification.filler, ["Consumables"]),
    # "Full Heal": ItemData(52, ItemClassification.filler, ["Consumables"]),
    # "Revive": ItemData(53, ItemClassification.filler, ["Consumables"]),
    # "Max Revive": ItemData(54, ItemClassification.filler, ["Consumables"]),
    # "Guard Spec": ItemData(55, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "Super Repel": ItemData(56, ItemClassification.filler, ["Consumables"]),
    # "Max Repel": ItemData(57, ItemClassification.filler, ["Consumables"]),
    # "Dire Hit": ItemData(58, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "10 Coins": ItemData(59, ItemClassification.filler, ["Coins"]),
    # "Fresh Water": ItemData(60, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    # "Soda Pop": ItemData(61, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    # "Lemonade": ItemData(62, ItemClassification.filler, ["Consumables", "Vending Machine Drinks"]),
    # "S.S. Ticket": ItemData(63, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Gold Teeth": ItemData(64, ItemClassification.progression, ["Unique", "Key Items"]),
    # "X Attack": ItemData(65, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "X Defend": ItemData(66, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "X Speed": ItemData(67, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "X Special": ItemData(68, ItemClassification.filler, ["Consumables", "Battle Items"]),
    # "Coin Case": ItemData(69, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Oak's Parcel": ItemData(70, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Item Finder": ItemData(71, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Silph Scope": ItemData(72, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Poke Flute": ItemData(73, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Lift Key": ItemData(74, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Exp. All": ItemData(75, ItemClassification.progression_skip_balancing, ["Unique", "Key Items"]),
    # "Old Rod": ItemData(76, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    # "Good Rod": ItemData(77, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    # "Super Rod": ItemData(78, ItemClassification.progression_skip_balancing, ["Unique", "Key Items", "Rods"]),
    # "PP Up": ItemData(79, ItemClassification.filler, ["Consumables"]),
    # "Ether": ItemData(80, ItemClassification.filler, ["Consumables"]),
    # "Max Ether": ItemData(81, ItemClassification.filler, ["Consumables"]),
    # "Elixir": ItemData(82, ItemClassification.filler, ["Consumables"]),
    # "Max Elixir": ItemData(83, ItemClassification.filler, ["Consumables"]),
    # "Tea": ItemData(84, ItemClassification.progression, ["Unique", "Key Items"]),
    # # "Master Sword": ItemData(85, ItemClassification.progression),
    # # "Flute": ItemData(86, ItemClassification.progression),
    # # "Titan's Mitt": ItemData(87, ItemClassification.progression),
    # # "Lamp": ItemData(88, ItemClassification.progression),
    # "Plant Key": ItemData(89, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Mansion Key": ItemData(90, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Hideout Key": ItemData(91, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Safari Pass": ItemData(93, ItemClassification.progression, ["Unique", "Key Items"]),
    # "Poison Trap": ItemData(94, ItemClassification.trap, ["Traps"]),
    # "Paralyze Trap": ItemData(95, ItemClassification.trap, ["Traps"]),
    # "Ice Trap": ItemData(96, ItemClassification.trap, ["Traps"]),
    # "Fire Trap": ItemData(97, ItemClassification.trap, ["Traps"]),
    # "20 Coins": ItemData(98, ItemClassification.filler, ["Coins"]),
    # "100 Coins": ItemData(99, ItemClassification.filler, ["Coins"]),
    # "Card Key 2F": ItemData(100, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 3F": ItemData(101, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 4F": ItemData(102, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 5F": ItemData(103, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 6F": ItemData(104, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 7F": ItemData(105, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 8F": ItemData(106, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 9F": ItemData(107, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 10F": ItemData(108, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Card Key 11F": ItemData(109, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Progressive Card Key": ItemData(110, ItemClassification.progression, ["Unique", "Key Items", "Card Keys"]),
    # "Sleep Trap": ItemData(111, ItemClassification.trap, ["Traps"]),
    # "HM01 Cut": ItemData(196, ItemClassification.progression, ["Unique", "HMs", "HM01", "Key Items"]),
    # "HM02 Fly": ItemData(197, ItemClassification.progression, ["Unique", "HMs", "HM02", "Key Items"]),
    # "HM03 Surf": ItemData(198, ItemClassification.progression, ["Unique", "HMs", "HM03", "Key Items"]),
    # "HM04 Strength": ItemData(199, ItemClassification.progression, ["Unique", "HMs", "HM04", "Key Items"]),
    # "HM05 Flash": ItemData(200, ItemClassification.progression, ["Unique", "HMs", "HM05", "Key Items"]),
    # "TM01 Mega Punch": ItemData(201, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM02 Razor Wind": ItemData(202, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM03 Swords Dance": ItemData(203, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM04 Whirlwind": ItemData(204, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM05 Mega Kick": ItemData(205, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM06 Toxic": ItemData(206, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM07 Horn Drill": ItemData(207, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM08 Body Slam": ItemData(208, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM09 Take Down": ItemData(209, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM10 Double Edge": ItemData(210, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM11 Bubble Beam": ItemData(211, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM12 Water Gun": ItemData(212, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM13 Ice Beam": ItemData(213, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM14 Blizzard": ItemData(214, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM15 Hyper Beam": ItemData(215, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM16 Pay Day": ItemData(216, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM17 Submission": ItemData(217, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM18 Counter": ItemData(218, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM19 Seismic Toss": ItemData(219, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM20 Rage": ItemData(220, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM21 Mega Drain": ItemData(221, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM22 Solar Beam": ItemData(222, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM23 Dragon Rage": ItemData(223, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM24 Thunderbolt": ItemData(224, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM25 Thunder": ItemData(225, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM26 Earthquake": ItemData(226, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM27 Fissure": ItemData(227, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM28 Dig": ItemData(228, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM29 Psychic": ItemData(229, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM30 Teleport": ItemData(230, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM31 Mimic": ItemData(231, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM32 Double Team": ItemData(232, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM33 Reflect": ItemData(233, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM34 Bide": ItemData(234, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM35 Metronome": ItemData(235, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM36 Self-Destruct": ItemData(236, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM37 Egg Bomb": ItemData(237, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM38 Fire Blast": ItemData(238, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM39 Swift": ItemData(239, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM40 Skull Bash": ItemData(240, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM41 Soft-Boiled": ItemData(241, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM42 Dream Eater": ItemData(242, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM43 Sky Attack": ItemData(243, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM44 Rest": ItemData(244, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM45 Thunder Wave": ItemData(245, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM46 Psywave": ItemData(246, ItemClassification.filler, ["Unique", "TMs"]),
    # "TM47 Explosion": ItemData(247, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM48 Fighting Slide": ItemData(248, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM49 Tri Attack": ItemData(249, ItemClassification.useful, ["Unique", "TMs"]),
    # "TM50 Substitute": ItemData(250, ItemClassification.useful, ["Unique", "TMs"]),
    #
    # "Game Corner": ItemData(None, ItemClassification.progression, []),
    # "Cinnabar Island": ItemData(None, ItemClassification.progression, []),
    # "Buy Poke Doll": ItemData(None, ItemClassification.progression, []),
    # "Vending Machine Drinks": ItemData(None, ItemClassification.progression, []),
    # "Help Bill": ItemData(None, ItemClassification.progression, []),
    # "Defeat BFighting": ItemData(None, ItemClassification.progression, []),
    # "Defeat Misty": ItemData(None, ItemClassification.progression, []),
    # "Defeat Lt. Surge": ItemData(None, ItemClassification.progression, []),
    # "Defeat Erika": ItemData(None, ItemClassification.progression, []),
    # "Defeat Koga": ItemData(None, ItemClassification.progression, []),
    # "Defeat Blaine": ItemData(None, ItemClassification.progression, []),
    # "Defeat Sabrina": ItemData(None, ItemClassification.progression, []),
    # "Defeat Viridian Gym Giovanni": ItemData(None, ItemClassification.progression, []),
    # "Seafoam Exit Boulder": ItemData(None, ItemClassification.progression, []),
    # "Seafoam Boss Boulders": ItemData(None, ItemClassification.progression, []),
    # "Victory Road Boulder": ItemData(None, ItemClassification.progression, []),
    # "Fuji Saved": ItemData(None, ItemClassification.progression, []),
    # "Silph Co Liberated": ItemData(None, ItemClassification.progression, []),
    # "Become Champion": ItemData(None, ItemClassification.progression, []),
    # "Mt Moon Fossils": ItemData(None, ItemClassification.progression, []),
    # "Cinnabar Lab": ItemData(None, ItemClassification.progression, []),
    #
    # "Trainer Parties": ItemData(None, ItemClassification.filler, [])
}

packs = {
    "Fighting": ["Aerodactyle Pack",
    "Dugtrio Pack",
    "Golem Pack",
    "Hitmonchan Pack",
    "Hitmonlee Pack",
    "Kabutops Pack",
    "Machamp Pack",
    "Marowak 1 Pack",
    "Marowak 2 Pack",
    "Onix Pack",
    "Primeape Pack",
    "Rhydon Pack",
    "Sandslash Pack"],

    "Psychic": ["Alakazam Pack",
    "Gengar 1 Pack",
    "Gengar 2 Pack",
    "Hypno Pack",
    "Jynx Pack",
    "Mew 1 Pack",
    "Mew 2 Pack",
    "Mew 3 Pack",
    "Mewtwo 1 Pack",
    "Mewtwo 2 Pack",
    "Mewtwo 3 Pack",
    "Mr Mime Pack"],

    "Grass": ["Arbok Pack",
    "Beedrill Pack",
    "Butterfree Pack",
    "Exeggutor Pack",
    "Golbat Pack",
    "Muk Pack",
    "Nidoking Pack",
    "Nidoqueen Pack",
    "Parasect Pack",
    "Pinsir Pack",
    "Scyther Pack",
    "Tangela 1 Pack",
    "Tangela 2 Pack",
    "Venomoth Pack",
    "Venusaur 1 Pack",
    "Venusaur 2 Pack",
    "Victreebel Pack",
    "Vileplume Pack",
    "Weezing Pack"],

    "Fire": ["Arcanine 1 Pack",
    "Arcanine 2 Pack",
    "Charizard Pack",
    "Flareon 1 Pack",
    "Flareon 2 Pack",
    "Magmar 1 Pack",
    "Magmar 2 Pack",
    "Moltres 1 Pack",
    "Moltres 2 Pack",
    "Ninetales 1 Pack",
    "Ninetales 2 Pack",
    "Rapidash Pack"],

    "Water": ["Articuno 1 Pack",
    "Articuno 2 Pack",
    "Blastoise Pack",
    "Cloyster Pack",
    "Dewgong Pack",
    "Golduck Pack",
    "Gyrados Pack",
    "Kingler Pack",
    "Lapras Pack",
    "Omastar Pack",
    "Poliwrath Pack",
    "Seadra Pack",
    "Seaking Pack",
    "Slowbrow Pack",
    "Slowpoke Promo Pack",
    "Starmie Pack",
    "Tentacruel Pack",
    "Vaporeon 1 Pack",
    "Vaporeon 2 Pack",]

    "Normal": ["Chansey Pack",
    "Clefable Pack",
    "Ditto Pack",
    "Dodrio Pack",
    "Dragonite 1 Pack",
    "Dragonite 2 Pack",
    "Farfetch'd Pack",
    "Fearow Pack",
    "Jigglypuff Promo Pack",
    "Kangaskhan Pack",
    "Lickitung Pack",
    "Persian 1 Pack",
    "Persian 2 Pack",
    "Pidgeot 1 Pack",
    "Pidgeot 2 Pack",
    "Porygon Pack",
    "Raticate Pack",
    "Snorlax Pack",
    "Tauros Pack",
    "Wigglytuff 1 Pack",
    "Wigglytuff 2 Pack"],

    "Lightning": ["Electabuzz 1 Pack",
    "Electabuzz 2 Pack",
    "Electrode 1 Pack",
    "Electrode 2 Pack",
    "Flying Pikachu Pack",
    "Jolteon 1 Pack",
    "Jolteon 2 Pack",
    "Magneton 1 Pack",
    "Magneton 2 Pack",
    "Raichu 1 Pack",
    "Raichu 2 Pack",
    "Raichu 3 Pack",
    "Raichu 4 Pack",
    "Surfing Pikachu 1 Pack",
    "Surfing Pikachu 2 Pack",
    "Zapdos 1 Pack",
    "Zapdos 2 Pack",
    "Zapdos 3 Pack"],

    "Trainer": ["Clefairy Doll Pack",
    "Defender Pack",
    "Devolution Spray Pack",
    "Energy Removal Pack",
    "Energy Retrieval Pack",
    "Energy Search Pack",
    "Full Heal Pack",
    "Gambler Pack",
    "Imakuni? Pack",
    "Imposter Professor Oak Pack",
    "Item Finder Pack",
    "Lass Pack",
    "Maintenance Pack",
    "Mr Fuji Pack",
    "Poke Ball Pack",
    "Pokedex Pack",
    "Pokemon Breeder Pack",
    "Pokemon Center Pack",
    "Pokemon Flute Pack",
    "Pokemon Trader Pack",
    "Potion Pack",
    "Recycle Pack",
    "Revive Pack",
    "Super Energy Retrieval Pack",
    "Super Potion Pack",
    "Switch Pack",

    "Computer Search Pack",
    "Gust of Wind Pack",
    "Pluspower Pack",

    "Bill Pack",
    "Professor Oak Pack",
    "Super Energy Removal Pack",
    "Double Colorless Energy Pack"],
}

medals = {
    "Water Medal",
    "Fighting Medal",
    "Rock Medal",
    "Lightning Medal",
    "Psychic Medal",
    "Science Medal",
    "Fire Medal",
    "Grass Medal"
}

doors = {
    "Water Club Door",
    "Fighting Club Door",
    "Rock Club Door",
    "Lightning Club Door",
    "Psychic Club Door",
    "Science Club Door",
    "Fire Club Door",
    "Grass Club Door"
}

masters_talkable = {
    "Water Club Talkable",
    "Fighting Club Talkable",
    "Rock Club Talkable",
    "Lightning Club Talkable",
    "Psychic Club Talkable",
    "Science Club Talkable",
    "Fire Club Talkable",
    "Grass Club Talkable"
}

pack_counts = {
    "Colosseum Pack": 10,
    "Mystery Pack": 10,
    "Laboratory Pack": 10,
    "Evolution Pack": 10,
    "Promo Arcanine": 4,
    "Promo Moltres": 4,
    "Promo Articuno": 4,
    "Promo Pikachu 1": 4,
    "Promo Pikachu 2": 4,
    "Promo Flying Pikachu": 4,
    "Promo Surfing Pikachu 1": 4,
    "Promo Surfing Pikachu 2": 4,
    "Promo Electabuzz": 4,
    "Promo Zapdos": 4,
    "Promo Slowpoke": 4,
    "Promo Mewtwo 1": 4,
    "Promo Mewtwo 2": 4,
    "Promo Mew 1": 4,
    "Promo Jigglypuff": 4,
    "Promo Dragonite": 4,
    "Promo Imakuni": 4,
    "Promo Super Energy Retrieval": 4,
    "Promo Venusaur": 4,
    "Promo Mew 2": 4,

    "Aerodactyle Pack": 4,
    "Dugtrio Pack": 4,
    "Golem Pack": 4,
    "Hitmonchan Pack": 4,
    "Hitmonlee Pack": 4,
    "Kabutops Pack": 4,
    "Machamp Pack": 4,
    "Marowak 1 Pack": 4,
    "Marowak 2 Pack": 4,
    "Onix Pack": 4,
    "Primeape Pack": 4,
    "Rhydon Pack": 4,
    "Sandslash Pack": 4,

    "Alakazam Pack": 4,
    "Gengar 1 Pack": 4,
    "Gengar 2 Pack": 4,
    "Hypno Pack": 4,
    "Jynx Pack": 4,
    "Mew 1 Pack": 4,
    "Mew 2 Pack": 4,
    "Mew 3 Pack": 4,
    "Mewtwo 1 Pack": 4,
    "Mewtwo 2 Pack": 4,
    "Mewtwo 3 Pack": 4,
    "Mr Mime Pack": 4,

    "Arbok Pack": 4,
    "Beedrill Pack": 4,
    "Butterfree Pack": 4,
    "Exeggutor Pack": 4,
    "Golbat Pack": 4,
    "Muk Pack": 4,
    "Nidoking Pack": 4,
    "Nidoqueen Pack": 4,
    "Parasect Pack": 4,
    "Pinsir Pack": 4,
    "Scyther Pack": 4,
    "Tangela 1 Pack": 4,
    "Tangela 2 Pack": 4,
    "Venomoth Pack": 4,
    "Venusaur 1 Pack": 4,
    "Venusaur 2 Pack": 4,
    "Victreebel Pack": 4,
    "Vileplume Pack": 4,
    "Weezing Pack": 4,

    "Arcanine 1 Pack": 4,
    "Arcanine 2 Pack": 4,
    "Charizard Pack": 4,
    "Flareon 1 Pack": 4,
    "Flareon 2 Pack": 4,
    "Magmar 1 Pack": 4,
    "Magmar 2 Pack": 4,
    "Moltres 1 Pack": 4,
    "Moltres 2 Pack": 4,
    "Ninetales 1 Pack": 4,
    "Ninetales 2 Pack": 4,
    "Rapidash Pack": 4,

    "Articuno 1 Pack": 4,
    "Articuno 2 Pack": 4,
    "Blastoise Pack": 4,
    "Cloyster Pack": 4,
    "Dewgong Pack": 4,
    "Golduck Pack": 4,
    "Gyrados Pack": 4,
    "Kingler Pack": 4,
    "Lapras Pack": 4,
    "Omastar Pack": 4,
    "Poliwrath Pack": 4,
    "Seadra Pack": 4,
    "Seaking Pack": 4,
    "Slowbrow Pack": 4,
    "Slowpoke Promo Pack": 4,
    "Starmie Pack": 4,
    "Tentacruel Pack": 4,
    "Vaporeon 1 Pack": 4,
    "Vaporeon 2 Pack": 4,

    "Chansey Pack": 4,
    "Clefable Pack": 4,
    "Ditto Pack": 4,
    "Dodrio Pack": 4,
    "Dragonite 1 Pack": 4,
    "Dragonite 2 Pack": 4,
    "Farfetch'd Pack": 4,
    "Fearow Pack": 4,
    "Jigglypuff Promo Pack": 4,
    "Kangaskhan Pack": 4,
    "Lickitung Pack": 4,
    "Persian 1 Pack": 4,
    "Persian 2 Pack": 4,
    "Pidgeot 1 Pack": 4,
    "Pidgeot 2 Pack": 4,
    "Porygon Pack": 4,
    "Raticate Pack": 4,
    "Snorlax Pack": 4,
    "Tauros Pack": 4,
    "Wigglytuff 1 Pack": 4,
    "Wigglytuff 2 Pack": 4,

    "Electabuzz 1 Pack": 4,
    "Electabuzz 2 Pack": 4,
    "Electrode 1 Pack": 4,
    "Electrode 2 Pack": 4,
    "Flying Pikachu Pack": 4,
    "Jolteon 1 Pack": 4,
    "Jolteon 2 Pack": 4,
    "Magneton 1 Pack": 4,
    "Magneton 2 Pack": 4,
    "Raichu 1 Pack": 4,
    "Raichu 2 Pack": 4,
    "Raichu 3 Pack": 4,
    "Raichu 4 Pack": 4,
    "Surfing Pikachu 1 Pack": 4,
    "Surfing Pikachu 2 Pack": 4,
    "Zapdos 1 Pack": 4,
    "Zapdos 2 Pack": 4,
    "Zapdos 3 Pack": 4,

    "Clefairy Doll Pack": 4,
    "Defender Pack": 4,
    "Devolution Spray Pack": 4,
    "Energy Removal Pack": 4,
    "Energy Retrieval Pack": 4,
    "Energy Search Pack": 4,
    "Full Heal Pack": 4,
    "Gambler Pack": 4,
    "Imakuni? Pack": 4,
    "Imposter Professor Oak Pack": 4,
    "Item Finder Pack": 4,
    "Lass Pack": 4,
    "Maintenance Pack": 4,
    "Mr Fuji Pack": 4,
    "Poke Ball Pack": 4,
    "Pokedex Pack": 4,
    "Pokemon Breeder Pack": 4,
    "Pokemon Center Pack": 4,
    "Pokemon Flute Pack": 4,
    "Pokemon Trader Pack": 4,
    "Potion Pack": 4,
    "Recycle Pack": 4,
    "Revive Pack": 4,
    "Super Energy Retrieval Pack": 4,
    "Super Potion Pack": 4,
    "Switch Pack": 4,

    "Computer Search Pack": 2,
    "Gust of Wind Pack": 2,
    "Pluspower Pack": 2,

    "Bill Pack": 1,
    "Professor Oak Pack": 1,
    "Super Energy Removal Pack": 1,
    "Double Colorless Energy Pack": 1,
}

item_table.update({f"TM{str(i).zfill(2)}": ItemData(i + 456, ItemClassification.filler, ["Unique", "TMs"])
                   for i in range(1, 51)})

item_table.update(
    {pokemon: ItemData(None, ItemClassification.progression, []) for pokemon in pokemon_data.keys()}
)
item_table.update(
    {f"Missable {pokemon}": ItemData(None, ItemClassification.useful, []) for pokemon in pokemon_data.keys()}
)
item_table.update(
    {f"Static {pokemon}": ItemData(None, ItemClassification.progression, []) for pokemon in pokemon_data.keys()}
)


item_groups = {}
for item, data in item_table.items():
    for group in data.groups:
        item_groups[group] = item_groups.get(group, []) + [item]
