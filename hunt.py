import random
from database import edata, eboosters, spells, items, locations


def hunt(place, area, inv,*stats):
    extraxp = 0
    print("*"*100)
    evariant = random.randint(1,12)
    variant = random.randint(-5,5)
    etype = eboosters[evariant]        
    health, coins, intel, strength, speed, level, xp = stats
    ename, ehealth, estrength, espeed = edata[place]["ename"],edata[place]["ehealth"], edata[place]["estrength\
"],edata[place]["espeed"]

    if etype["change"] == "espeed":
        espeed+=int(etype["by"])
    elif etype["change"] == "estrength":
        estrength+=int(etype["by"])
    elif etype["change"] == "ehealth":
        ehealth+=int(etype["by"])
    elif etype["change"] == "xpdrop":
        extraxp=int(etype["by"])
    print(f"You walk into the {area} and it wasnt long before you see a\
",etype["name"],ename)

    if speed>=espeed:
        print("You were ready for this fight, and started your attack")
    else:
        print("You werent ready for this fight, and the enemy attacked first")
        health -= estrength
        print("You lost",estrength,"HP")

    fight = True    
    playerturn = True
    enemyturn = False
    turn = 1
    ehp = ehealth
    poisoned = 0

    while fight:
        while playerturn:
            print("*"*100)
            print(f"Turn:{turn}")
            print("Your HP is:", health,"and the", ename,"has",ehp,"/", ehealth)
            print("You also currently have", intel,"mana")
            print("What do you want to do?")
            choice = input("[attack, magic, potion, run] ")
            variant = random.randint(-1/5*strength,1/5*strength)

            if choice =="attack":
                ehp-=strength+variant
                print("You attack, dealing", strength+variant,"points of damage.")
                playerturn = False
                enemyturn = True

            elif choice == "magic":
                print("What spell would you like to cast?")
                for i in spells:
                    print(i,"which costs",spells[i]["cost"],"mana and deals",spells[i]["effect"],"points of damage.")

                while True:
                    choice = input("[fireball, heal, thunderbolt/poison] ")
                    if choice == "fireball":
                        flag = spell_check(intel, choice)
                        if flag == False:
                            print("You do not have enough mana!")
                            continue
                        ehp-=spells[choice]["effect"]+variant
                        intel -= spells[choice]["cost"]
                        print("Fire bursts from your fingers, and engulfs your enemy, dealing\
",spells[choice]["effect"]+variant,"points of damage.")
                        playerturn = False
                        enemyturn = True
                        break

                    elif choice == "heal":
                        flag = spell_check(intel, choice)
                        if flag == False:
                            print("You do not have enough mana!")
                            continue
                        health+=spells[choice]["effect"]+variant
                        intel -= spells[choice]["cost"]
                        print("You get surrounded by a warm green glow, and your wounds heal, you gain\
",spells[choice]["effect"]+variant,"points of HP.")
                        playerturn = False
                        enemyturn = True
                        break

                    elif choice == "poison":
                        flag = spell_check(intel, choice)
                        if flag == False:
                            print("You do not have enough mana!")
                            continue
                        poisoned+=spells[choice]["effect"]
                        intel -= spells[choice]["cost"]
                        print("You release dark green gas from your hands, and your opponent gets poisoned for\
",poisoned,"points of HP per turn.")
                        playerturn = False
                        enemyturn = True
                        break

                    elif choice == "thunderbolt":
                        flag = spell_check(intel, choice)
                        if flag == False:
                            print("You do not have enough mana!")
                            continue
                        ehp -= spells[choice]["effect"]+variant
                        intel -= spells[choice]["cost"]
                        print("You raise your hand up to the sky and cast down lightning upon the enemy\
",spells[choice]["effect"]+variant,"points of HP.")
                        playerturn = False
                        enemyturn = True
                        break

                    elif choice == "back":
                        break

                    else:
                        print("Please enter a valid spell, or enter back")
                        
            elif choice == "potion":
                if not inv == []:
                    while True:
                        print(inv)
                        print("Which potion would you like to have?")
                        choice = input("[health, mana] ")
                        if choice == "health":
                            if "Health potion" in inv:
                                inv.remove("Health potion")
                                health+=items["health"]["increase"]
                                print("You gained",items["health"]["increase"],"HP and you now have",health,"HP")
                                playerturn = False
                                enemyturn = True
                                break
                            else:
                                print("You do not have any health potions!")
                                break
                        elif choice == "mana":
                            if "Mana potion" in inv:
                                inv.remove("Mana potion")
                                intel+=items["mana"]["increase"]
                                print("You gained",items["mana"]["increase"],"int and you now have",intel,"int")
                                playerturn = False
                                enemyturn = True
                                break
                            else:
                                print("You do not have any mana potions!")
                                break
                        else:
                            print("Please enter a valid choice")
                            break
                else:
                    print("You do not have any potions!")
                    continue
            elif choice == "run":
                place = place[:4]+str(int(place[4])-1)
                area = locations[int(place[4])]
                playerturn = False
                fight = False
            else:
                print("Please enter a valid choice")
            if not poisoned == 0:
                ehp-=poisoned
                print("Your opponent was also poisoned, dealing",poisoned,"points of damage")
        if ehp>0:
            while enemyturn:
                print("*"*100)
                if not edata[place]["regen"]==0 and not ehp == ehealth:
                    ehp += edata[place]["regen"]
                    print("The enemy regenerates",edata[place]["regen"],"HP")
                variant = random.randint(int(-1/5*estrength),int(1/5*estrength))
                health-=(estrength+variant)
                print("The",ename,"attacks, dealing",estrength+variant,"\
points of damage")
                enemyturn = False
                playerturn = True
                turn+=1
        else:
            print("*"*100)
            variant = random.randint(0,5)
            drop = [(etype["name"]+" "+edata[place]["drop"]),int(edata[place]["worth"]*eboosters[evariant]["dropprice"])]
            xp += (edata[place]["xpdrop"]+extraxp+variant)
            tolevel = 10*level
            if xp>=tolevel:
                xp-=tolevel
                print("You have gained a level!\n\
+30 HP\n+5 Strength\n+50 Intelligence\n+1 Speed")
                strength+=5
                health+=30
                intel+=50
                speed+=1
                level+=1
            inv.append(drop)
            print("You won this fight! You gain",str(edata[place]["xpdrop"]+extraxp+variant),"XP")
            print("You also got a",drop[0],"worth",drop[1], "coins")
            fight = False
        if not health >0:
            print("*"*100)
            print("You have died!")
            input("Press enter to exit")
            exit()
    stats = (health, coins, intel, strength, speed, level, xp)
    return place, area, inv,*stats

def spell_check(intel, choice):
    if intel>=spells[choice]["cost"]:
        flag = True
    else:
        flag = False
    return flag

