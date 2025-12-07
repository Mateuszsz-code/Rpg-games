from random import randint

def shop(player):
    print("Witamy w sklepie! Twoj bilans:", player[3], "zlotych")
    print("1. Zwieksz atak o 10-15 za 100 zl")
    print("2. Zwieksz leczenie o 5 za 100 zl")
    print("3. Ulecz do 250 HP za 50 zl")
    print("4. Dodaj 50 HP za 50 zl")
    print("5. cvxc  ")

    inp = input("co chcesz kupic: ")

    if inp == "1":
        if player[3] >= 100:
            player[1] += randint(10,15)
            player[3] -= 100
            print("Kupiono atak!")
        else:
            print("Za malo zlota!")

    elif inp == "2":
        if player[3] >= 100:
            player[2] += 5
            player[3] -= 100
        else:
            print("Za malo zlota!")

    elif inp == "3":
        if player[3] >= 50:
            player[0] = 250
            player[3] -= 50
        else:
            print("Za malo zlota!")

    elif inp == "4":
        if player[3] >= 50:
            player[0] += 50
            player[3] -= 50
        else:
            print("Za malo zlota!")
    
     
