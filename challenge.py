from database import locations, keywords, items, stats
from hunt import hunt
print("This is a role playing adventure game,\
where you are an adventurer \
who has to kill the demon \nking \
in the throne room. You have to level up, \
upgrade your weapons, sell\nresources and \
keep fighting monsters until you\
 reach the demon king, and\ntry your \
best to defeat him, with magic or brawn.")
def town(): 
    inv = []
    index = 0
    area = locations[index]
    flag = True
    while flag == True:
        print("*"*100)
        print(f"You are in the village near the {area},\
you can buy/sell items or hunt. What do you want to do?")
        print("[buy/sell/hunt/inv/stats/quit] ")
        choice = input_checker()
        if choice == "buy":
            while True:
                buy(inv)
                break
            continue
        elif choice == "sell":
            sell(inv)
            continue
        elif choice == "hunt":
            index+=1
            area = locations[index]
            place = "area"+str(index)
            statlist = list(stats.values())
            place, area, inv, *newstats=hunt(place ,area , inv, *statlist)
            j=0
            for i in stats:
                stats[i]=newstats[j]
                j+=1
            index = int(place[4])
            if index == 6:
                print("Congratulations! You finally beat the demon king and freed the country from his tyranny!")
                input("Press any key to exit")
                flag = False
                exit
            continue
        elif choice == "stats":
            for i in stats:
                print(i, ":", stats[i])
            continue
        elif choice == "inv":
            print("*"*100)
            print("You have: ")
            for i in inv:
                if isinstance(i, list):
                    print(i[0],":",i[1])
                    continue
                print(i)
            continue
        elif choice == "quit":
            flag = False
            exit
        else:
            print("Error: Wrong Choice!")
            continue


def input_checker():
    flag = True
    while flag == True:
        choice1 = input()
        choice1 = choice1.lower()
        clist = choice1.split()
        for word in clist:
            if word in keywords:
                choice1 = keywords[word]
                flag = False
                break
            else:
                print("Please enter a valid option")
                continue
    return choice1


def buy(inv):
    print("*"*100)
    print("You currently have",stats["coins"], "and",inv)
    print("You can buy/upgrade:")
    for i in items:
        print(items[i]["item"], "for",items[i]["cost"])
    while True:
        choice = input_checker()
        if choice not in items:
            print("Please enter a valid option!")
            continue
        print("You chose to buy a",items[choice]["item"])
        if stats["coins"] >= items[choice]["cost"]:
            stats["coins"] -= items[choice]["cost"]         
            if items[choice]["item"] == "Greatsword":
                stats["strength"]+=items[choice]["increase"]
                break
            elif items[choice]["item"] == "Magic Staff":
                stats["intel"]+=items[choice]["increase"]
                break
            inv.append(items[choice]["item"])   
        else:
            print("You do not have enough money to buy this!")
        break

def sell(inv):
    print("*"*100)
    print("You currently have",stats["coins"], "and",inv)
    shop = True
    while shop:
        print("You can sell:-")
        for i in inv:
            if isinstance(i, list):
                print(i[0],":",i[1])
        choice1 = input("What would you like to sell? ")
        choice1 = choice1.lower()
        if choice1 == "back":
            shop = False
            continue
        for i in inv:
            if isinstance(i, list):
                if i[0]==choice1:
                    print("Found item worth",i[1],", adding to coins.")
                    stats["coins"]+=i[1]
                    inv.remove(i)
                    shop = False
                    break
        else:
            print("Item not found, please try again")
    
    return None

town()
