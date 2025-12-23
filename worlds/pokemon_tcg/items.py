from BaseClasses import ItemClassification


class ItemData:
    def __init__(self, item_id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if item_id is None else item_id + 172000000

# Soft limit of 22 cards per pack
# Hard cap of 128.  Unknown if soft limit can be bypassed currently
item_table = {
    "Colosseum Pack": ItemData(1, ItemClassification.progression, ["Pack"]),
    "Laboratory Pack": ItemData(2, ItemClassification.progression, ["Pack"]),
    "Mystery Pack": ItemData(3, ItemClassification.progression, ["Pack"]),
    "Evolution Pack": ItemData(4, ItemClassification.progression, ["Pack"]),
    "Promo Arcanine": ItemData(5, ItemClassification.progression, ["Pack"]),
    "Promo Moltres": ItemData(6, ItemClassification.progression, ["Pack"]),
    "Promo Articuno": ItemData(7, ItemClassification.progression, ["Pack"]),
    "Promo Pikachu 1": ItemData(8, ItemClassification.progression, ["Pack"]),
    "Promo Pikachu 2": ItemData(9, ItemClassification.progression, ["Pack"]),
    "Promo Flying Pikachu": ItemData(10, ItemClassification.progression, ["Pack"]),
    "Promo Surfing Pikachu 1": ItemData(11, ItemClassification.progression, ["Pack"]),
    "Promo Surfing Pikachu 2": ItemData(12, ItemClassification.progression, ["Pack"]),
    "Promo Electabuzz": ItemData(13, ItemClassification.progression, ["Pack"]),
    "Promo Zapdos": ItemData(14, ItemClassification.progression, ["Pack"]),
    "Promo Slowpoke": ItemData(15, ItemClassification.progression, ["Pack"]),
    "Promo Mewtwo 1": ItemData(16, ItemClassification.progression, ["Pack"]),
    "Promo Mewtwo 2": ItemData(17, ItemClassification.progression, ["Pack"]),
    "Promo Mew 1": ItemData(18, ItemClassification.progression, ["Pack"]),
    "Promo Jigglypuff": ItemData(19, ItemClassification.progression, ["Pack"]),
    "Promo Dragonite": ItemData(20, ItemClassification.progression, ["Pack"]),
    "Promo Imakuni": ItemData(21, ItemClassification.progression, ["Pack"]),
    "Promo Super Energy Retrieval": ItemData(22, ItemClassification.progression, ["Pack"]),
    "Promo Venusaur": ItemData(23, ItemClassification.progression, ["Pack"]),
    "Promo Mew 2": ItemData(24, ItemClassification.progression, ["Pack"]),

    "Aerodactyle Pack": ItemData(25, ItemClassification.progression, ["Fighting", "Pack"]),
    "Dugtrio Pack": ItemData(26, ItemClassification.progression, ["Fighting", "Pack"]),
    "Golem Pack": ItemData(27, ItemClassification.progression, ["Fighting", "Pack"]),
    "Hitmonchan Pack": ItemData(28, ItemClassification.progression, ["Fighting", "Pack"]),
    "Hitmonlee Pack": ItemData(29, ItemClassification.progression, ["Fighting", "Pack"]),
    "Kabutops Pack": ItemData(30, ItemClassification.progression, ["Fighting", "Pack"]),
    "Machamp Pack": ItemData(31, ItemClassification.progression, ["Fighting", "Pack"]),
    "Marowak 1 Pack": ItemData(32, ItemClassification.progression, ["Fighting", "Pack"]),
    "Marowak 2 Pack": ItemData(33, ItemClassification.progression, ["Fighting", "Pack"]),
    "Onix Pack": ItemData(34, ItemClassification.progression, ["Fighting", "Pack"]),
    "Primeape Pack": ItemData(35, ItemClassification.progression, ["Fighting", "Pack"]),
    "Rhydon Pack": ItemData(36, ItemClassification.progression, ["Fighting", "Pack"]),
    "Sandslash Pack": ItemData(37, ItemClassification.progression, ["Fighting", "Pack"]),

    "Alakazam Pack": ItemData(38, ItemClassification.progression, ["Psychic", "Pack"]),
    "Gengar 1 Pack": ItemData(39, ItemClassification.progression, ["Psychic", "Pack"]),
    "Gengar 2 Pack": ItemData(40, ItemClassification.progression, ["Psychic", "Pack"]),
    "Hypno Pack": ItemData(41, ItemClassification.progression, ["Psychic", "Pack"]),
    "Jynx Pack": ItemData(42, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 1 Pack": ItemData(43, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 2 Pack": ItemData(44, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mew 3 Pack": ItemData(45, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 1 Pack": ItemData(46, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 2 Pack": ItemData(47, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mewtwo 3 Pack": ItemData(48, ItemClassification.progression, ["Psychic", "Pack"]),
    "Mr Mime Pack": ItemData(49, ItemClassification.progression, ["Psychic", "Pack"]),

    "Arbok Pack": ItemData(50, ItemClassification.progression, ["Grass", "Pack"]),
    "Beedrill Pack": ItemData(51, ItemClassification.progression, ["Grass", "Pack"]),
    "Butterfree Pack": ItemData(52, ItemClassification.progression, ["Grass", "Pack"]),
    "Exeggutor Pack": ItemData(53, ItemClassification.progression, ["Grass", "Pack"]),
    "Golbat Pack": ItemData(54, ItemClassification.progression, ["Grass", "Pack"]),
    "Muk Pack": ItemData(55, ItemClassification.progression, ["Grass", "Pack"]),
    "Nidoking Pack": ItemData(56, ItemClassification.progression, ["Grass", "Pack"]),
    "Nidoqueen Pack": ItemData(57, ItemClassification.progression, ["Grass", "Pack"]),
    "Parasect Pack": ItemData(58, ItemClassification.progression, ["Grass", "Pack"]),
    "Pinsir Pack": ItemData(59, ItemClassification.progression, ["Grass", "Pack"]),
    "Scyther Pack": ItemData(60, ItemClassification.progression, ["Grass", "Pack"]),
    "Tangela 1 Pack": ItemData(61, ItemClassification.progression, ["Grass", "Pack"]),
    "Tangela 2 Pack": ItemData(62, ItemClassification.progression, ["Grass", "Pack"]),
    "Venomoth Pack": ItemData(63, ItemClassification.progression, ["Grass", "Pack"]),
    "Venusaur 1 Pack": ItemData(64, ItemClassification.progression, ["Grass", "Pack"]),
    "Venusaur 2 Pack": ItemData(65, ItemClassification.progression, ["Grass", "Pack"]),
    "Victreebel Pack": ItemData(66, ItemClassification.progression, ["Grass", "Pack"]),
    "Vileplume Pack": ItemData(67, ItemClassification.progression, ["Grass", "Pack"]),
    "Weezing Pack": ItemData(68, ItemClassification.progression, ["Grass", "Pack"]),

    "Arcanine 1 Pack": ItemData(69, ItemClassification.progression, ["Fire", "Pack"]),
    "Arcanine 2 Pack": ItemData(70, ItemClassification.progression, ["Fire", "Pack"]),
    "Charizard Pack": ItemData(71, ItemClassification.progression, ["Fire", "Pack"]),
    "Flareon 1 Pack": ItemData(72, ItemClassification.progression, ["Fire", "Pack"]),
    "Flareon 2 Pack": ItemData(73, ItemClassification.progression, ["Fire", "Pack"]),
    "Magmar 1 Pack": ItemData(74, ItemClassification.progression, ["Fire", "Pack"]),
    "Magmar 2 Pack": ItemData(75, ItemClassification.progression, ["Fire", "Pack"]),
    "Moltres 1 Pack": ItemData(76, ItemClassification.progression, ["Fire", "Pack"]),
    "Moltres 2 Pack": ItemData(77, ItemClassification.progression, ["Fire", "Pack"]),
    "Ninetales 1 Pack": ItemData(78, ItemClassification.progression, ["Fire", "Pack"]),
    "Ninetales 2 Pack": ItemData(79, ItemClassification.progression, ["Fire", "Pack"]),
    "Rapidash Pack": ItemData(80, ItemClassification.progression, ["Fire", "Pack"]),

    "Articuno 1 Pack": ItemData(81, ItemClassification.progression, ["Water", "Pack"]),
    "Articuno 2 Pack": ItemData(82, ItemClassification.progression, ["Water", "Pack"]),
    "Blastoise Pack": ItemData(83, ItemClassification.progression, ["Water", "Pack"]),
    "Cloyster Pack": ItemData(84, ItemClassification.progression, ["Water", "Pack"]),
    "Dewgong Pack": ItemData(85, ItemClassification.progression, ["Water", "Pack"]),
    "Golduck Pack": ItemData(86, ItemClassification.progression, ["Water", "Pack"]),
    "Gyrados Pack": ItemData(87, ItemClassification.progression, ["Water", "Pack"]),
    "Kingler Pack": ItemData(88, ItemClassification.progression, ["Water", "Pack"]),
    "Lapras Pack": ItemData(89, ItemClassification.progression, ["Water", "Pack"]),
    "Omastar Pack": ItemData(90, ItemClassification.progression, ["Water", "Pack"]),
    "Poliwrath Pack": ItemData(91, ItemClassification.progression, ["Water", "Pack"]),
    "Seadra Pack": ItemData(92, ItemClassification.progression, ["Water", "Pack"]),
    "Seaking Pack": ItemData(93, ItemClassification.progression, ["Water", "Pack"]),
    "Slowbrow Pack": ItemData(94, ItemClassification.progression, ["Water", "Pack"]),
    "Slowpoke Promo Pack": ItemData(95, ItemClassification.progression, ["Pack"]),
    "Starmie Pack": ItemData(96, ItemClassification.progression, ["Water", "Pack"]),
    "Tentacruel Pack": ItemData(97, ItemClassification.progression, ["Water", "Pack"]),
    "Vaporeon 1 Pack": ItemData(98, ItemClassification.progression, ["Water", "Pack"]),
    "Vaporeon 2 Pack": ItemData(99, ItemClassification.progression, ["Water", "Pack"]),

    "Chansey Pack": ItemData(100, ItemClassification.progression, ["Normal", "Pack"]),
    "Clefable Pack": ItemData(101, ItemClassification.progression, ["Normal", "Pack"]),
    "Ditto Pack": ItemData(102, ItemClassification.progression, ["Normal", "Pack"]),
    "Dodrio Pack": ItemData(103, ItemClassification.progression, ["Normal", "Pack"]),
    "Dragonite 1 Pack": ItemData(104, ItemClassification.progression, ["Normal", "Pack"]),
    "Dragonite 2 Pack": ItemData(105, ItemClassification.progression, ["Normal", "Pack"]),
    "Farfetch'd Pack": ItemData(106, ItemClassification.progression, ["Normal", "Pack"]),
    "Fearow Pack": ItemData(107, ItemClassification.progression, ["Normal", "Pack"]),
    "Jigglypuff Promo Pack": ItemData(108, ItemClassification.progression, ["Normal", "Pack"]),
    "Kangaskhan Pack": ItemData(109, ItemClassification.progression, ["Normal", "Pack"]),
    "Lickitung Pack": ItemData(110, ItemClassification.progression, ["Normal", "Pack"]),
    "Persian 1 Pack": ItemData(111, ItemClassification.progression, ["Normal", "Pack"]),
    "Persian 2 Pack": ItemData(112, ItemClassification.progression, ["Normal", "Pack"]),
    "Pidgeot 1 Pack": ItemData(113, ItemClassification.progression, ["Normal", "Pack"]),
    "Pidgeot 2 Pack": ItemData(114, ItemClassification.progression, ["Normal", "Pack"]),
    "Porygon Pack": ItemData(115, ItemClassification.progression, ["Normal", "Pack"]),
    "Raticate Pack": ItemData(116, ItemClassification.progression, ["Normal", "Pack"]),
    "Snorlax Pack": ItemData(117, ItemClassification.progression, ["Normal", "Pack"]),
    "Tauros Pack": ItemData(118, ItemClassification.progression, ["Normal", "Pack"]),
    "Wigglytuff 1 Pack": ItemData(119, ItemClassification.progression, ["Normal", "Pack"]),
    "Wigglytuff 2 Pack": ItemData(120, ItemClassification.progression, ["Normal", "Pack"]),

    "Electabuzz 1 Pack": ItemData(121, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electabuzz 2 Pack": ItemData(122, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electrode 1 Pack": ItemData(123, ItemClassification.progression, ["Lightning", "Pack"]),
    "Electrode 2 Pack": ItemData(124, ItemClassification.progression, ["Lightning", "Pack"]),
    "Flying Pikachu Pack": ItemData(125, ItemClassification.progression, ["Lightning", "Pack"]),
    "Jolteon 1 Pack": ItemData(126, ItemClassification.progression, ["Lightning", "Pack"]),
    "Jolteon 2 Pack": ItemData(127, ItemClassification.progression, ["Lightning", "Pack"]),
    "Magneton 1 Pack": ItemData(128, ItemClassification.progression, ["Lightning", "Pack"]),
    "Magneton 2 Pack": ItemData(129, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 1 Pack": ItemData(130, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 2 Pack": ItemData(131, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 3 Pack": ItemData(132, ItemClassification.progression, ["Lightning", "Pack"]),
    "Raichu 4 Pack": ItemData(133, ItemClassification.progression, ["Lightning", "Pack"]),
    "Surfing Pikachu 1 Pack": ItemData(134, ItemClassification.progression, ["Lightning", "Pack"]),
    "Surfing Pikachu 2 Pack": ItemData(135, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 1 Pack": ItemData(136, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 2 Pack": ItemData(137, ItemClassification.progression, ["Lightning", "Pack"]),
    "Zapdos 3 Pack": ItemData(138, ItemClassification.progression, ["Lightning", "Pack"]),

    "Clefairy Doll Pack": ItemData(139, ItemClassification.progression, ["Trainer", "Pack"]),
    "Defender Pack": ItemData(140, ItemClassification.progression, ["Trainer", "Pack"]),
    "Devolution Spray Pack": ItemData(141, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Removal Pack": ItemData(142, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Retrieval Pack": ItemData(143, ItemClassification.progression, ["Trainer", "Pack"]),
    "Energy Search Pack": ItemData(144, ItemClassification.progression, ["Trainer", "Pack"]),
    "Full Heal Pack": ItemData(145, ItemClassification.progression, ["Trainer", "Pack"]),
    "Gambler Pack": ItemData(146, ItemClassification.progression, ["Trainer", "Pack"]),
    "Imakuni? Pack": ItemData(147, ItemClassification.progression, ["Trainer", "Pack"]),
    "Imposter Professor Oak Pack": ItemData(148, ItemClassification.progression, ["Trainer", "Pack"]),
    "Item Finder Pack": ItemData(149, ItemClassification.progression, ["Trainer", "Pack"]),
    "Lass Pack": ItemData(150, ItemClassification.progression, ["Trainer", "Pack"]),
    "Maintenance Pack": ItemData(151, ItemClassification.progression, ["Trainer", "Pack"]),
    "Mr Fuji Pack": ItemData(152, ItemClassification.progression, ["Trainer", "Pack"]),
    "Poke Ball Pack": ItemData(153, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokedex Pack": ItemData(154, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Breeder Pack": ItemData(155, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Center Pack": ItemData(156, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Flute Pack": ItemData(157, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pokemon Trader Pack": ItemData(158, ItemClassification.progression, ["Trainer", "Pack"]),
    "Potion Pack": ItemData(159, ItemClassification.progression, ["Trainer", "Pack"]),
    "Recycle Pack": ItemData(160, ItemClassification.progression, ["Trainer", "Pack"]),
    "Revive Pack": ItemData(161, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Energy Retrieval Pack": ItemData(162, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Potion Pack": ItemData(163, ItemClassification.progression, ["Trainer", "Pack"]),
    "Switch Pack": ItemData(164, ItemClassification.progression, ["Trainer", "Pack"]),

    "Computer Search Pack": ItemData(165, ItemClassification.progression, ["Trainer", "Pack"]),
    "Gust of Wind Pack": ItemData(166, ItemClassification.progression, ["Trainer", "Pack"]),
    "Pluspower Pack": ItemData(167, ItemClassification.progression, ["Trainer", "Pack"]),

    "Bill Pack": ItemData(168, ItemClassification.progression, ["Trainer", "Pack"]),
    "Professor Oak Pack": ItemData(169, ItemClassification.progression, ["Trainer", "Pack"]),
    "Super Energy Removal Pack": ItemData(170, ItemClassification.progression, ["Trainer", "Pack"]),
    "Double Colorless Energy Pack": ItemData(171, ItemClassification.useful, ["Energy", "Pack"]),

    "Grass Medal": ItemData(172, ItemClassification.progression, ["Medal"]),
    "Lightning Medal": ItemData(173, ItemClassification.progression, ["Medal"]),
    "Fire Medal": ItemData(174, ItemClassification.progression, ["Medal"]),
    "Fighting Medal": ItemData(175, ItemClassification.progression, ["Medal"]),
    "Rock Medal": ItemData(176, ItemClassification.progression, ["Medal"]),
    "Science Medal": ItemData(177, ItemClassification.progression, ["Medal"]),
    "Psychic Medal": ItemData(178, ItemClassification.progression, ["Medal"]),
    "Water Medal": ItemData(179, ItemClassification.progression, ["Medal"]),

    "Energy Pack": ItemData(180, ItemClassification.filler, ["Energy", "Pack"]),

    "Beat Sam": ItemData(None, ItemClassification.progression, []),
    "Beat Aaron LF": ItemData(None, ItemClassification.progression, []),
    "Beat Aaron WF": ItemData(None, ItemClassification.progression, []),
    "Beat Aaron GP": ItemData(None, ItemClassification.progression, []),
    "Beat Heather": ItemData(None, ItemClassification.progression, []),
    "Beat Kristin": ItemData(None, ItemClassification.progression, []),
    "Beat Brittany": ItemData(None, ItemClassification.progression, []),
    "Beat Nikki": ItemData(None, ItemClassification.progression, []),
    "Beat Joseph": ItemData(None, ItemClassification.progression, []),
    "Beat David": ItemData(None, ItemClassification.progression, []),
    "Beat Erik": ItemData(None, ItemClassification.progression, []),
    "Beat Rick": ItemData(None, ItemClassification.progression, []),
    "Beat Jonathan": ItemData(None, ItemClassification.progression, []),
    "Beat Adam": ItemData(None, ItemClassification.progression, []),
    "Beat John": ItemData(None, ItemClassification.progression, []),
    "Beat Ken": ItemData(None, ItemClassification.progression, []),
    "Beat Joshua": ItemData(None, ItemClassification.progression, []),
    "Beat Amanda": ItemData(None, ItemClassification.progression, []),
    "Beat Sara": ItemData(None, ItemClassification.progression, []),
    "Beat Amy": ItemData(None, ItemClassification.progression, []),
    "Beat Nicholas": ItemData(None, ItemClassification.progression, []),
    "Beat Brandon": ItemData(None, ItemClassification.progression, []),
    "Beat Jennifer": ItemData(None, ItemClassification.progression, []),
    "Beat Isaac": ItemData(None, ItemClassification.progression, []),
    "Beat Daniel": ItemData(None, ItemClassification.progression, []),
    "Beat Stephanie": ItemData(None, ItemClassification.progression, []),
    "Beat Robert": ItemData(None, ItemClassification.progression, []),
    "Beat Murray": ItemData(None, ItemClassification.progression, []),
    "Beat Ryan": ItemData(None, ItemClassification.progression, []),
    "Beat Andrew": ItemData(None, ItemClassification.progression, []),
    "Beat Matthew": ItemData(None, ItemClassification.progression, []),
    "Beat Gene": ItemData(None, ItemClassification.progression, []),
    "Beat Jessica": ItemData(None, ItemClassification.progression, []),
    "Beat Michael": ItemData(None, ItemClassification.progression, []),
    "Beat Chris": ItemData(None, ItemClassification.progression, []),
    "Beat Mitch": ItemData(None, ItemClassification.progression, []),
    "Beat Courtney": ItemData(None, ItemClassification.progression, []),
    "Beat Steve": ItemData(None, ItemClassification.progression, []),
    "Beat Jack": ItemData(None, ItemClassification.progression, []),
    "Beat Rod": ItemData(None, ItemClassification.progression, []),
    "Become Champion": ItemData(None, ItemClassification.progression, []),

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
    "Vaporeon 2 Pack",],

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

medals = [
    "Water Medal",
    "Fighting Medal",
    "Rock Medal",
    "Lightning Medal",
    "Psychic Medal",
    "Science Medal",
    "Fire Medal",
    "Grass Medal"
]

doors = [
    "Water Club Door",
    "Fighting Club Door",
    "Rock Club Door",
    "Lightning Club Door",
    "Psychic Club Door",
    "Science Club Door",
    "Fire Club Door",
    "Grass Club Door"
]

masters_talkable = [
    "Water Club Talkable",
    "Fighting Club Talkable",
    "Rock Club Talkable",
    "Lightning Club Talkable",
    "Psychic Club Talkable",
    "Science Club Talkable",
    "Fire Club Talkable",
    "Grass Club Talkable"
]

pack_counts = {
    "Colosseum Pack": 10,
    "Mystery Pack": 10,
    "Laboratory Pack": 10,
    "Evolution Pack": 10,
    "Promo Arcanine": 1,
    "Promo Moltres": 1,
    "Promo Articuno": 1,
    "Promo Pikachu 1": 1,
    "Promo Pikachu 2": 1,
    "Promo Flying Pikachu": 1,
    "Promo Surfing Pikachu 1": 1,
    "Promo Surfing Pikachu 2": 1,
    "Promo Electabuzz": 1,
    "Promo Zapdos": 1,
    "Promo Slowpoke": 1,
    "Promo Mewtwo 1": 1,
    "Promo Mewtwo 2": 1,
    "Promo Mew 1": 1,
    "Promo Jigglypuff": 1,
    "Promo Dragonite": 1,
    "Promo Imakuni": 1,
    "Promo Super Energy Retrieval": 1,
    "Promo Venusaur": 1,
    "Promo Mew 2": 1,

    "Aerodactyle Pack": 1,
    "Dugtrio Pack": 1,
    "Golem Pack": 1,
    "Hitmonchan Pack": 1,
    "Hitmonlee Pack": 1,
    "Kabutops Pack": 1,
    "Machamp Pack": 1,
    "Marowak 1 Pack": 1,
    "Marowak 2 Pack": 1,
    "Onix Pack": 1,
    "Primeape Pack": 1,
    "Rhydon Pack": 1,
    "Sandslash Pack": 1,

    "Alakazam Pack": 1,
    "Gengar 1 Pack": 1,
    "Gengar 2 Pack": 1,
    "Hypno Pack": 1,
    "Jynx Pack": 1,
    "Mew 1 Pack": 1,
    "Mew 2 Pack": 1,
    "Mew 3 Pack": 1,
    "Mewtwo 1 Pack": 1,
    "Mewtwo 2 Pack": 1,
    "Mewtwo 3 Pack": 1,
    "Mr Mime Pack": 1,

    "Arbok Pack": 1,
    "Beedrill Pack": 1,
    "Butterfree Pack": 1,
    "Exeggutor Pack": 1,
    "Golbat Pack": 1,
    "Muk Pack": 1,
    "Nidoking Pack": 1,
    "Nidoqueen Pack": 1,
    "Parasect Pack": 1,
    "Pinsir Pack": 1,
    "Scyther Pack": 1,
    "Tangela 1 Pack": 1,
    "Tangela 2 Pack": 1,
    "Venomoth Pack": 1,
    "Venusaur 1 Pack": 1,
    "Venusaur 2 Pack": 1,
    "Victreebel Pack": 1,
    "Vileplume Pack": 1,
    "Weezing Pack": 1,

    "Arcanine 1 Pack": 1,
    "Arcanine 2 Pack": 1,
    "Charizard Pack": 1,
    "Flareon 1 Pack": 1,
    "Flareon 2 Pack": 1,
    "Magmar 1 Pack": 1,
    "Magmar 2 Pack": 1,
    "Moltres 1 Pack": 1,
    "Moltres 2 Pack": 1,
    "Ninetales 1 Pack": 1,
    "Ninetales 2 Pack": 1,
    "Rapidash Pack": 1,

    "Articuno 1 Pack": 1,
    "Articuno 2 Pack": 1,
    "Blastoise Pack": 1,
    "Cloyster Pack": 1,
    "Dewgong Pack": 1,
    "Golduck Pack": 1,
    "Gyrados Pack": 1,
    "Kingler Pack": 1,
    "Lapras Pack": 1,
    "Omastar Pack": 1,
    "Poliwrath Pack": 1,
    "Seadra Pack": 1,
    "Seaking Pack": 1,
    "Slowbrow Pack": 1,
    "Slowpoke Promo Pack": 1,
    "Starmie Pack": 1,
    "Tentacruel Pack": 1,
    "Vaporeon 1 Pack": 1,
    "Vaporeon 2 Pack": 1,

    "Chansey Pack": 1,
    "Clefable Pack": 1,
    "Ditto Pack": 1,
    "Dodrio Pack": 1,
    "Dragonite 1 Pack": 1,
    "Dragonite 2 Pack": 1,
    "Farfetch'd Pack": 1,
    "Fearow Pack": 1,
    "Jigglypuff Promo Pack": 1,
    "Kangaskhan Pack": 1,
    "Lickitung Pack": 1,
    "Persian 1 Pack": 1,
    "Persian 2 Pack": 1,
    "Pidgeot 1 Pack": 1,
    "Pidgeot 2 Pack": 1,
    "Porygon Pack": 1,
    "Raticate Pack": 1,
    "Snorlax Pack": 1,
    "Tauros Pack": 1,
    "Wigglytuff 1 Pack": 1,
    "Wigglytuff 2 Pack": 1,

    "Electabuzz 1 Pack": 1,
    "Electabuzz 2 Pack": 1,
    "Electrode 1 Pack": 1,
    "Electrode 2 Pack": 1,
    "Flying Pikachu Pack": 1,
    "Jolteon 1 Pack": 1,
    "Jolteon 2 Pack": 1,
    "Magneton 1 Pack": 1,
    "Magneton 2 Pack": 1,
    "Raichu 1 Pack": 1,
    "Raichu 2 Pack": 1,
    "Raichu 3 Pack": 1,
    "Raichu 4 Pack": 1,
    "Surfing Pikachu 1 Pack": 1,
    "Surfing Pikachu 2 Pack": 1,
    "Zapdos 1 Pack": 1,
    "Zapdos 2 Pack": 1,
    "Zapdos 3 Pack": 1,

    "Clefairy Doll Pack": 1,
    "Defender Pack": 1,
    "Devolution Spray Pack": 1,
    "Energy Removal Pack": 1,
    "Energy Retrieval Pack": 1,
    "Energy Search Pack": 1,
    "Full Heal Pack": 1,
    "Gambler Pack": 1,
    "Imakuni? Pack": 1,
    "Imposter Professor Oak Pack": 1,
    "Item Finder Pack": 1,
    "Lass Pack": 1,
    "Maintenance Pack": 1,
    "Mr Fuji Pack": 1,
    "Poke Ball Pack": 1,
    "Pokedex Pack": 1,
    "Pokemon Breeder Pack": 1,
    "Pokemon Center Pack": 1,
    "Pokemon Flute Pack": 1,
    "Pokemon Trader Pack": 1,
    "Potion Pack": 1,
    "Recycle Pack": 1,
    "Revive Pack": 1,
    "Super Energy Retrieval Pack": 1,
    "Super Potion Pack": 1,
    "Switch Pack": 1,

    "Computer Search Pack": 2,
    "Gust of Wind Pack": 2,
    "Pluspower Pack": 2,

    "Bill Pack": 4,
    "Professor Oak Pack": 4,
    "Super Energy Removal Pack": 4,
    "Double Colorless Energy Pack": 4,
}


item_groups = {}
for item, data in item_table.items():
    for group in data.groups:
        item_groups[group] = item_groups.get(group, []) + [item]
