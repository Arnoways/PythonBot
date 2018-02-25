from rpggame import rpgshopitem as rpgsi, rpgtrainingitem as rpgti

element_none = 1
element_lightning = 2
element_air = -2
element_dark = 3
element_holy = -3
element_ice = 4
element_fire = -4
elementnames = {
    element_none : "Normal", 
    element_lightning : "Lightning", 
    element_air : "Air", 
    element_dark : "Dark", 
    element_holy : "Holy", 
    element_ice : "Ice", 
    element_fire : "Fire"
    }

weaponelems = ['Plain', 'Thunder', 'Aerial', 'Dark', 'Divine', 'Frozen', 'Flaming']

shopitems = {
    "health" : rpgsi.RPGShopItem("health", 100, {"health" : ("+", 25)}), 
    "damage" : rpgsi.RPGShopItem("damage", 250, {"damage" : ("+", 1)}),
    "critical" : rpgsi.RPGShopItem("critical", 4000, {"critical" : ("+", 1)})
    }

trainingitems = {
    "maxhealth" : rpgsi.RPGShopItem("maxhealth", 0.25, {"maxhealth" : ("+", 1)}), 
    "weaponskill" : rpgsi.RPGShopItem("weaponskill", 10, {"weaponskill" : ("+", 1)})
    }

weapons = [
    'Axe', 
    'Boomerang', 'Bow', 
    'Club', 'Crossbow', 
    'Dual Daggers', 'Dagger', 
    'Glaive', 'Greatsword', 
    'Hammer', 'Halberd', 
    'Katana', 
    'Mace', 'Magic', 
    'Pike', 
    'Rapier', 
    'Spear', 'Slingshot', 'Scourge', 'Scythe', 'Sorcery', 'Staff', 'Sword', 
    'Twin Glaives'
    ]

armors = [
    'Brigandine', 
    'Chainmail', 'Cuirass', 
    'Dō', 
    'Keikō', 'Kusari Katabira', 
    'Lamellar Armor', 'Laminar Armor', 
    'Plate Armor', 'Plated Mail', 
    'Robes', 
    'Scale Armor', 
    'Tankō'
    ]

weaponprefixes = [
    'Cursed', 
    'Possesed', 
    'Rusty', 
    'Old', 
    'Used', 
    'Antic', 
    'Ancient', 
    'Common', 
    'Forgotten', 
    'New', 
    'Rare', 
    'Epic', 
    'Legendary'
    ]

weaponsuffixes = [
    'stolen from a kid', 
    'that fell off the tumbrel', 
    'made from Dafaq\'s tears', 
    'bought from the local dealer', 
    'gifted by the Emperor', 
    'as long as Nya\'s Dildo', 
    'blessed by Kappa', 
    'of Dankness', 
    'of Love', 
    'of Power',
    'of Doom',
    'of Power of Doom of Apoc..',
    'found under a rock', 
    'crafted by your mom', 
    'found in a happy meal',
    'that also tells time',
    'that protects your virginity',
    'bought for 2$ in wallmart',
    'scavenged on a weeb\'s corpse',
    'used to clean dragon teeth',
    'that can talk but not to you'
    ]

names = {
    "role" : [
        "Assassin", 
        "Sorcerer", 
        "Barbarian", 
        "Knight"
        ]
    }

monsters = [
    ("Boar", element_none, "https://vignette.wikia.nocookie.net/swordartonlineroleplay/images/4/4a/Frenzy_Boar.png/revision/latest?cb=20121115182555"),
    ("Black Wolf", element_none, "https://s-media-cache-ak0.pinimg.com/originals/40/80/39/40803940ed534c4b396a43a270e66e57.jpg"), 
    ("Desert Raider", element_none, "https://i.pinimg.com/736x/71/ca/fb/71cafb5cb719b0336547694db1038d3d--fantasy-warrior-character-ideas.jpg"),
    ("Drunk Dwarf", element_none, "https://fc06.deviantart.net/fs70/f/2011/234/c/b/party_dwarf_by_capprotti-d47g5pt.jpg"),
    ("Elven Ranger", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/7/75/Warhammer_Wood_Elf.png/revision/latest?cb=20130519024532"),
    ("Greatsword Champion", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/8/85/Capture22233232.png/revision/latest?cb=20140206193843"),
    ("Gretchin", element_none, "http://wh40k.lexicanum.com/mediawiki/images/thumb/e/eb/SM_Gretchin.png/250px-SM_Gretchin.png"),
    ("Giant Spider", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/3/3f/Warhammer_Giant_Spiders.png/revision/latest?cb=20170809014204"),
    ("Hungry Spirit", element_none, "https://vignette.wikia.nocookie.net/studio-ghibli/images/f/f1/Pngghost.png/revision/latest?cb=20160424134002"),
    ("Runaway Warbeast", element_none, "http://wh40k.lexicanum.com/mediawiki/images/thumb/6/6e/Cruorian_War_Beast.jpg/300px-Cruorian_War_Beast.jpg"),
    ("Malicious Chopper", element_none, "https://vignette.wikia.nocookie.net/villains/images/c/c9/Barry-0.png/revision/latest?cb=20150810173740"),
    ("Nya's Little Brother", element_none, "http://wh40k.lexicanum.com/mediawiki/images/thumb/a/a0/ChaosSpawn2.jpg/225px-ChaosSpawn2.jpg"),
    ("Savage Armored Goblin", element_none, "https://i.pinimg.com/736x/24/23/e1/2423e1955cf7e40b20d40bedbe16a392--warhammer-fantasy-warhammer-k.jpg"),
    ("Stalking Elven Archer", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/0/0c/Warhammer_Wood_Elves_Waystalker.jpg/revision/latest?cb=20160909032654"),
    ("Something Disguised as a Tree", element_none, "http://statici.behindthevoiceactors.com/behindthevoiceactors/_img/chars/treebeard-the-lord-of-the-rings-the-two-towers-68.6.jpg"),
    ("Sepulchural Stalker", element_none, "https://s-media-cache-ak0.pinimg.com/originals/f5/6d/2d/f56d2d38d427d25a610ac7e4365f1bcf.jpg"),
    ("Tomb King Chosen", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/d/da/Warhammer_Tomb_Kings_Settra.png/revision/latest?cb=20160911222902"),
    ("Wounded Troll", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/2/20/Trolls_-_Stone_Troll_%28Old_Art%29.jpg/revision/latest?cb=20160708133949"),
                      
    ("Elemental Shaman", element_lightning, "https://i.pinimg.com/736x/f8/5c/f6/f85cf681c7465967fedfe89bfb6caf0d--the-wizard-lightning.jpg"),
    ("Doomsayer", element_lightning, "https://2dbdd5116ffa30a49aa8-c03f075f8191fb4e60e74b907071aee8.ssl.cf1.rackcdn.com/3065298_1421697249.5094_funddescription.jpg"),
    ("Thunder Knight", element_lightning, "https://s-media-cache-ak0.pinimg.com/originals/78/de/77/78de777c2411214e0b61eb22ba25c985.jpg"), 
    ("Scissor Knight", element_lightning, "https://i.pinimg.com/736x/41/32/b7/4132b7423da75a1d5f9bed5d467072d2--kill-la-kill-anime-art.jpg"),
    ("Storm Elemental", element_lightning, "https://i.pinimg.com/736x/87/c7/8e/87c78eb9801fb248f91844881259e0ac--guild-wars--medieval-fantasy.jpg"),
                      
    ("A Birdperson", element_air, "https://vignette.wikia.nocookie.net/rickandmorty/images/9/9d/BirdpersonTransparent.png/revision/latest?cb=20161223222905"),
    ("Angry Griffin", element_air, "http://www.dododex.com/media/creature/griffin.png"),
    ("Awakened Being", element_air, "https://vignette.wikia.nocookie.net/claymore/images/2/20/PriscillaAwakened.gif/revision/latest?cb=20080815194603"),
    ("Fallen Friend", element_air, "https://pm1.narvii.com/6351/867f04184d535dedf5d2062f7c7cac46f94776bd_hq.jpg"),
    ("Little Witch", element_air, "https://pre00.deviantart.net/c2bd/th/pre/i/2017/103/f/6/shiny_arc_by_moonflower20000-db5qf30.jpg"),
    ("Little Loli Dragon", element_air, "https://vignette.wikia.nocookie.net/vsbattles/images/d/d4/Blue_Eyes.png/revision/latest?cb=20160201020306"),
    ("Enraged Spiritual Guide", element_air, "https://bravenewmoe.files.wordpress.com/2013/08/monogatari20second20season20-200520-20large2018.jpg"),
    ("Single Air Bender", element_air, "https://orig08.deviantart.net/f3a9/f/2016/119/4/f/aang_about_web_by_dynamo1212-da0ox4c.jpg"),
   
    ("Angry Goblin", element_dark, "https://vignette.wikia.nocookie.net/warhammerfb/images/b/b4/Goblin_Warrior.png/revision/latest?cb=20160508093347"),
    ("Hekatonkheires", element_dark, "https://vignette.wikia.nocookie.net/akamegakill/images/6/64/Coro.png/revision/latest?cb=20140803220237"),
    ("Khone Juggernaut", element_dark, "https://vignette.wikia.nocookie.net/warhammer40k/images/5/56/Juggernaut_of_Khorne.png/revision/latest?cb=20151215222741"),
    ("Lone Chaos Marauder", element_dark, "https://vignette.wikia.nocookie.net/warhammerfb/images/7/7f/Chaos_Marauder.png/revision/latest?cb=20151106043446"),
    ("Mutated Monkey", element_dark, "https://orig00.deviantart.net/07df/f/2013/119/d/5/rainy_devil_cosplay___bakemonogatari_by_kohimebashiri-d63k393.jpg"),
    ("Skaven Assassin in Training", element_dark, "https://us.v-cdn.net/5022456/uploads/editor/tr/lllm5fvwginz.jpg"), 
    
    ("Awoken Spirit", element_holy, "https://vignette.wikia.nocookie.net/warhammerfb/images/4/41/WAR_CA_00806_07.jpg/revision/latest/scale-to-width-down/251?cb=20171119134426"),
    ("Elven Slave", element_holy, "http://whfb.lexicanum.com/mediawiki/images/thumb/4/44/DEW.JPG/293px-DEW.JPG"),
    ("Elven Wanderer", element_holy, "https://vignette.wikia.nocookie.net/warhammerfb/images/2/26/Warhammer_Aenarion.png/revision/latest?cb=20161029054605"),
    ("Justice", element_holy, "http://www.1zoom.me/big2/39/207534-SweetAngel.jpg"),
    ("Saint of a Lost Faith", element_holy, "https://img00.deviantart.net/7081/i/2013/103/4/f/saint_celestine__warhammer_40_000__by_phallseanghell-d61lry2.jpg"),
    ("Tired Pilgrim", element_holy, "https://vignette.wikia.nocookie.net/warhammerfb/images/2/2d/Warhammer_Human_Nagash.jpg/revision/latest?cb=20170422040305"),
    ("Wandering Angel", element_holy, "https://i.pinimg.com/736x/42/92/59/429259b04d9825ec546cda7ae11095f4--fantasy-art-angels-fallen-angels.jpg"),
    
    ("Lava Crocodile", element_fire, "https://vignette.wikia.nocookie.net/creaturequest/images/4/4f/246_LavaCrocodile.png/revision/latest?cb=20170316003052"),
    ("Lava Salamander", element_fire, "http://4.bp.blogspot.com/-UEZJNqRarg0/T_H4FbsjPwI/AAAAAAAABK0/GxEgvp3qcqk/s1600/Fire_Lizard_by_bcook972001.jpeg"),
    ("Magma Slime", element_fire, "https://d1u5p3l4wpay3k.cloudfront.net/minecraft_gamepedia/thumb/c/c8/Magma_Cube_Jumping.png/150px-Magma_Cube_Jumping.png?version=745959687f245bc782a68f16eead18cc"),
    ("Molten Troll", element_fire, "https://img00.deviantart.net/79de/i/2014/039/1/c/lava_monster__cherufe__by_jubjubjedi-d56j69f.jpg"),
    ("Wild Cursed Campfire", element_fire, "http://www.rachelhtmendell.com/wp-content/uploads/2017/07/fire-2197606_1920.jpg"),
                      
    ("Crystal Lizard", element_ice, "http://darksouls3.wiki.fextralife.com/file/Dark-Souls-3/ravenous_liz.jpg"),
    ("Evolved Fish", element_ice, "https://s-media-cache-ak0.pinimg.com/originals/4d/0f/8d/4d0f8d96222ee1840c2c388dc8997aea.jpg"),
    ("Frost Sorcerer Apprentice", element_ice, "https://i.pinimg.com/736x/e4/23/c3/e423c34e957a90ecf14e8dcacccaa92b.jpg"),
    ("Frozen Golem", element_ice, "https://i.pinimg.com/236x/a6/2d/f3/a62df3326559cb9ed161df2c6817fdb5--ice-magic-golem.jpg"),
    ("Lizardman with Magic Frost Weapon", element_ice, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRxmqhxYgUX30N8lidVmhS93NUaQjB-_ILTfNEqNKKUrEr-hr7Xg"),
    ("Northern Dwarf", element_ice, "https://vignette.wikia.nocookie.net/warhammerfb/images/5/55/Grombrindal%2C_The_White_Dwarf.jpg/revision/latest?cb=20161231045405"),
    ("Snow Giant", element_ice, "https://orig00.deviantart.net/6cbb/f/2012/233/e/d/frost_giant_by_catherine_oc-d5bvjz1.jpg"),
    ("Cursed Ice Princess", element_ice, "https://cdna.artstation.com/p/assets/images/images/001/758/500/large/rafael-teruel-ice-queen-by-rafater-2.jpg?1452293194")
    ]

bosses = [
    ("Ogre Bruiser", element_none, "https://vignette.wikia.nocookie.net/warhammerfb/images/2/2d/Warhammer_Ogre_Bruiser.png/revision/latest?cb=20170111040334"),
    ("Barbarian Chieftain", element_none, "https://s-media-cache-ak0.pinimg.com/originals/49/76/90/497690027055ec7531ab471f99d57426.jpg"),
    
    ("Lord of Change", element_air, "https://spikeybits.com/wp-content/uploads/2014/11/fateweaver.jpg"),
    ("Valkia the Bloody", element_air, "https://s-media-cache-ak0.pinimg.com/originals/33/ac/2a/33ac2abb16e80727180259f8b05beb61.jpg"),

    ("Biribiri Herself", element_lightning, "https://i.imgur.com/2AhCKgV.png"),
    ("Dragon Ogre Shaggoth", element_lightning, "https://vignette.wikia.nocookie.net/warhammerfb/images/0/0b/Kolek.png/revision/latest?cb=20160623213433"),
    ("Thunder Demi-god", element_lightning, "https://1d4chan.org/images/thumb/f/f8/SigThor.jpg/850px-SigThor.jpg"),
    
    ("Black Ork Boss", element_dark, "https://vignette.wikia.nocookie.net/warhammerfb/images/d/d2/Untitled3232.jpg/revision/latest?cb=20131002023457"),
    ("Demon Prince", element_dark, "https://spikeybits.com/wp-content/uploads/2017/03/Demon-Prince.jpg"),
    ("Unknown Mutation", element_dark, "https://i.pinimg.com/736x/60/34/88/603488c24a5a10662ad451738afe2cec--warhammer-fantasy-warhammer-k.jpg"),
    ("Vampire Count", element_dark, "https://vignette.wikia.nocookie.net/warhammerfb/images/7/74/Mannfred_von_Carstein.PNG/revision/latest?cb=20150724201838"),
    
    ("Spear of the Holy Church", element_holy, "http://www.postavy.cz/foto/halflight-spear-of-the-church-foto.jpg"),
    ("Young Dragon", element_holy, "https://cdnb.artstation.com/p/assets/images/images/005/275/043/large/john-stone-holy-dragon-by-john-stone-art-db2ox97.jpg?1489830207"),
    
    ("Chaos Demon of Khorne", element_fire, "https://vignette.wikia.nocookie.net/warhammer40k/images/1/17/Bloodthirster_by_columbussage-d47j02l.jpg/revision/latest?cb=20120117042500"),
    ("Pyrese Dragon", element_fire, "https://vignette.wikia.nocookie.net/risingdawn/images/c/c1/Pyrese.jpg/revision/latest?cb=20131222230556"),

    ("Mammoth", element_ice, "https://i.ytimg.com/vi/ilr_CRV9MQ4/maxresdefault.jpg"),
    ("Yeti", element_ice, "https://img00.deviantart.net/b76e/i/2006/316/5/a/yeti_by_andreauderzo.jpg")
    ]

adventureSecrets = [
    ("you saw something shiny when you followed a bird", "Money", 100),
    ("a strange creature you saved gave you his thanks", "Money", 100),
    ("you cought a thief for a nearby shopowner", "Money", 150),
    ("you killed a running skaven thief", "Money", 150),
    ("you found a treasure chest", "Money", 200),
    ("you found a naked guy in a cave and stole his ring", "Money", 200),
    ("you sold some junk at a salesman near the road", "Money", 250),

    ("an old lady shared a meal with you", "Health", 100),
    ("you got lost and rested at a small lake", "Health", 200),

    ("you found a nest of little griffins and made the wise decision to run", "Exp", 100),
    ("you sparred with an old friend", "Exp", 100),
    ("you listened to another adventurer's tales", "Exp", 150),
    ("you got through the scary part of nearby woods", "Exp", 150),
    ("you talked to some strange travellers", "Exp", 200),
    ("you saw big creatures fighting in the distance and learned some moves", "Exp", 250),

    ("you fell off the road and climbed back up", "Weaponskill", 1),

    ("a blacksmith in a small village tought you some tricks", "Damage", 2),
                    
    ("you got distracted by nature", "A good feeling", 1)
    ]