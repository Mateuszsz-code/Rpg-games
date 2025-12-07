from random import randint


def simple_attack(player, enemy):
    enemy[0] -= player[1]
    player[0] -= enemy[1]
    print(f"Zadales {player[1]} obrazen!")
    
def fire_ball(player, enemy):
    if player[3] >= 100:
        player[0] -= enemy[1]
        enemy[0] -= randint(70,80)
        player[3] -= 100
        print(f"Zadales {randint(70,80)} obrazen")
    elif player[3] < 100:
        print("Nie masz wystarczajaco zlota na fire ball!")

def rocket(player, enemy):
    if player[3] >= 500:
        player[0] -= enemy[1]
        enemy[0] -= randint(150,200)
        player[3] -= 500
        print(f"Zadales {randint(150,200)} obrazen")
    elif player[3] < 500:
        print("Nie masz wystarczajaco zlota na rocket!")

def lighting(player, enemy):
    if player[3] >= 350:
        player[0] -= randint(10,15)
        enemy[1] -= randint(10,15)
        player[3] -= 150
        print(f"Zmniejszyles atak przeciwnika o {randint(10,15)}")
        print(f"Przeciwnik atakuje cie za {enemy[1]} obrazen")
        print(f"Zadales {player[1]} obrazen!")
    elif player[3] < 350:
        print("Nie masz wystarczajaco zlota na lighting!")

def earth_quake(player, enemy):
    if player[3] >= 400:
        player[0] -= enemy[1]
        enemy[0] -= randint(120,150)
        player[3] -= 400
        print(f"Zadales {randint(120,150)} obrazen")
    elif player[3] < 400:
        print("Nie masz wystarczajaco zlota na earth quake!")
