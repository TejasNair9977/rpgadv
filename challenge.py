from turtle import st
from database import locations, keywords, items, stats, print_colored
from hunt import hunt

print_colored("This is a role playing adventure game,\
where you are an adventurer \
who has to kill the demon \nking \
in the throne room. You have to level up, \
upgrade your weapons, sell\nresources and \
keep fighting monsters until you\
 reach the demon king, and\ntry your \
best to defeat him, with magic or brawn.", style="info")


def town():
    inv = []
    index = 0
    area = locations[index]
    flag = True
    while flag == True:
        print("*" * 100)
        print(f"You are in the village near the {area},\
you can buy/sell items or hunt. What do you want to do?")
        print_colored("[buy/sell/increase-hp/inn/hunt/inv/stats/quit]", style="warning")
        choice = input_checker()
        if choice == "buy":
            while True:
                buy(inv)
                break
            continue
        elif choice == "sell":
            sell(inv)
            continue
        elif choice == "increase-hp":  # (increases hp with health potion)
            heal(inv)
            continue
        elif choice == "inn":  # (increases hp if your hp < 50)
            inn()
            continue
        elif choice == "hunt":
            index += 1
            area = locations[index]
            place = "area" + str(index)
            statlist = list(stats.values())
            place, area, inv, *newstats = hunt(place, area, inv, *statlist)
            j = 0
            for i in stats:
                stats[i] = newstats[j]
                j += 1
            index = int(place[4])
            if index == 6:
                print_colored("Congratulations! You finally beat the demon king and freed the country from his tyranny!", style="success")
                input("Press any key to exit")
                flag = False
                exit
            continue
        elif choice == "stats":
            for idx, i in enumerate(stats):
                if idx % 3 == 0:
                    print_colored(f"{i}: {stats[i]}", style="danger")
                elif idx % 3 == 1:
                    print_colored(f"{i}: {stats[i]}", style="success")
                else:
                    print_colored(f"{i}: {stats[i]}", style="info")
            continue
        elif choice == "inv":
            print("*" * 100)
            print_colored("You have: ", style="info")
            for i in inv:
                if isinstance(i, list):
                    print_colored(f"{i[0]} : {i[1]}", style="warning")
                    continue
                print_colored(i, style="warning")
            continue
        elif choice == "quit":
            flag = False
            exit
        else:
            print("Error: Wrong Choice!")
            continue


def input_checker(query=""):
    flag = True
    while flag == True:
        choice1 = input(query)
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
    print("*" * 100)
    
    print_colored(f'You currently have {stats["coins"]} and {inv}', style="info")
    print("You can buy/upgrade:")
    for i in items:
        print(items[i]["item"], "for", items[i]["cost"])
    while True:
        choice = input_checker("Your choice: ")
        if choice not in items:
            print("Please enter valid quantity!")
            continue
        try:
            quantity = int(input("Quantity: "))
            if quantity < 1:
                raise ValueError
        except ValueError:
            print("Please enter a valid option!")
            continue
        print("You chose to buy {} {}(s)".format(quantity, items[choice]["item"]))
        if stats["coins"] >= items[choice]["cost"]*quantity:
            stats["coins"] -= items[choice]["cost"]*quantity
            if items[choice]["item"] == "Greatsword":
                stats["strength"] += items[choice]["increase"]*quantity
                break
            elif items[choice]["item"] == "Magic Staff":
                stats["intel"] += items[choice]["increase"]*quantity
                break
            inv.extend([items[choice]["item"]]*quantity)
            print_colored("Purchase successful!", style="success")
        else:
            print_colored("You do not have enough money to buy this!", style="danger")
        break


def sell(inv):
    print("*" * 100)
    print("You currently have", stats["coins"], "and", inv)
    shop = True
    while shop:
        print("You can sell:-")
        for i in inv:
            if isinstance(i, list):
                print(i[0], ":", i[1])
        choice1 = input("What would you like to sell? ")
        choice1 = choice1.lower()
        if choice1 == "back":
            shop = False
            continue
        for i in inv:
            if isinstance(i, list):
                if i[0] == choice1:
                    print_colored(f"Found item worth {i[1]}, adding to coins.", style="success")
                    stats["coins"] += i[1]
                    inv.remove(i)
                    shop = False
                    break
        else:
            print_colored("Item not found, please try again", style="danger")

    return None


# Added a heal-up option to heal you up with your healing potion in you inv
def heal(inv):
    print("*" * 100)

    if "Health potion" in inv:
        inv.remove("Health potion")
        stats["health"] += items["health"]["increase"]
        health = stats["health"]
        print_colored(f'You gained {items["health"]["increase"]} HP and you now have {health} HP', style="success")
    else:
        print_colored("You do not have any health potions!", style="danger")


# Added an inn to heal you if you are less than 50 hp
def inn():
    print("*" * 100)
    if stats["health"] < 50:
        temp = stats["health"]
        stats["health"] = 50
        gained_hp = stats["health"] - temp
        print_colored(f'You rested and gained {gained_hp} HP', style="success")
    else:
        print_colored("You have rested", style="info")

# I wanted to make the inn also replenish mana, maybe later :)


town()
