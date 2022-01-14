#this is the players base stats, and it increases the more you play the game.

stats = {"health" : 50,
        "coins" :50,
        "intel": 100,
        "strength": 10,
        "speed" : 5,
        "level":1,
        "xp":0}

#edata stands for enemy data and it stores the enemies you can encounter in your hunts, along with their
#stats like their health, strength and speed. 

edata={"area1":
        {"ename":"Wolf",
        "ehealth":40,
        "estrength":10,
        "espeed":5,
        "xpdrop":5,
        "eintel":10,
        "regen":0,
        "drop":"wolf skin",
        "worth":100},

        "area2":
        {"ename":"Goblin",
        "ehealth":70,
        "estrength":15,
        "espeed":8,
        "xpdrop":7,
        "eintel":20,
        "regen":4,
        "drop":"goblin ear",
        "worth":150},

        "area3":
        {"ename":"Orc",
        "ehealth":100,
        "estrength":15,
        "espeed":6,
        "xpdrop":10,
        "eintel":40,
        "regen":0,
        "drop":"orc tooth",
        "worth":250},

        "area4":
        {"ename":"Giant",
        "ehealth":200,
        "estrength":20,
        "espeed":7,
        "xpdrop":20,
        "eintel":70,
        "regen":1,
        "drop":"giant eye",
        "worth":500},

        "area5":
        {"ename":"Dragon",
        "ehealth":300,
        "estrength":30,
        "espeed":7,
        "eintel":200,
        "xpdrop":130,
        "regen":2,
        "drop":"dragon scale",
        "worth":750},

        "area6":
        {"ename":"Demon King",
        "ehealth":500,
        "estrength":50,
        "eintel":200,
        "espeed":10,
        "xpdrop":100,
        "regen":3,
        "drop":"demon crown",
        "worth":1000}}

eboosters = {1:{"name":"strong",
                "change":"estrength",
                "by":7,
                "dropprice":1.5},
            2:{"name":"extravagant",
                "change":"worth",
                "by":1,
                "dropprice":5},
            3:{"name":"nimble",
                "change":"espeed",
                "by":2,
                "dropprice":1.5},
            4:{"name":"experienced",
                "change":"xpdrop",
                "by":10,
                "dropprice":1},
            5:{"name":"tanky",
                "change":"ehealth",
                "by":50,
                "dropprice":2},
            6:{"name":"deadly",
                "change":"estrength",
                "by":10,
                "dropprice":3},
            7:{"name":"monstrous",
                "change":"estrength",
                "by":20,
                "dropprice":4},
            8:{"name":"godly",
                "change":"ehealth",
                "by":150,
                "dropprice":5},
            9:{"name":"weak",
                "change":"estrength",
                "by":-9,
                "dropprice":0.5},
            10:{"name":"slow",
                "change":"espeed",
                "by":-2,
                "dropprice":0.5},
            11:{"name":"young",
                "change":"ehealth",
                "by":-19,
                "dropprice":0.8},
            12:{"name":"dimwit",
                "change":"eintel",
                "by":-9,
                "dropprice":0.8}
            }

spells =  {"heal":
            {"effect":50,
            "cost":30},
          "fireball":
            {"effect":50,
            "cost":70},
          "thunderbolt":
            {"effect":150,
            "cost":150},
          "poison":
            {"effect":30,
            "cost":100}}
          

#items stores the items you can buy in the shop, along with the price, and the quantity
#you have and what each item does


items = {"health":
        {"item":"Health potion",
        "cost":50,
        "increase":70},

        "mana":
        {"item":"Mana potion",
        "cost":50,
        "increase":100},

        "sword":
        {"item":"Greatsword",
        "cost":100,
        "increase":15},

        "magic":
        {"item":"Magic Staff",
        "cost":150,
        "increase":300},
        }


#keywords stores values that the user might type instead of the main commands. for example, if the user types supplies instead of buy,
#the program will know that the user wants to buy something, and wont cause any error
keywords = {"supplies":"buy",
            "buy":"buy",
            "sell":"sell",
            "hunt":"hunt",
            "resources":"sell",
            "start":"hunt",
            "magic":"magic",
            "staff":"magic",
            "magic staff":"magic",
            "sword":"sword",
            "greatsword":"sword",
            "mana potion":"mana",
            "health potion":"health",
            "mana":"mana",
            "health":"health",
            "inventory":"inv",
            "inv":"inv",
            "stats":"stats",
            "exit":"quit",
            "quit":"quit",
            "leave":"quit",
            "equip":"equip",
            "enchant":"enchant",
            "shop":"buy"}

#this list stores all the locations you can reach in your hunts

locations = ["town",  "woods", "goblin camps", "badlands", "entrance", "castle", "throneroom"]
