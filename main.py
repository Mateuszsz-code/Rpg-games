import time
import os
from functions.shop import shop
from functions.enemies import create_boss
from functions.player import create_player, show_player
from functions.combat import fight
from functions.quests import quests_menu
from functions import statistics as s
from random import randint

player_name = input("Podaj imie swojej postaci: ")
player = create_player()
#player[0] = hp 
while player[0] and not s.HADES_KILLED> 0:

    print("""
    a - idz do lasu
    b - idz do jaskini
    c - idz do miasta
    d - idz do sklepu
    e - idz do swiata 67
    f - idz do hadesu
    g - zakoncz gre
    m - misje
    """)

    show_player(player, player_name)
    inp = input("gdzie chcesz isc: ")

    if inp == "a":
        boss = create_boss('boss')
        fight(player, boss, "Boss")
        
    elif inp == "b":
        cave_boss = create_boss('cave_boss')
        fight(player, cave_boss, "CaveBoss")

    elif inp == "c":
        town_boss = create_boss('town_boss')
        fight(player, town_boss, "TownBoss")

    elif inp == "d":
        shop(player)
    
    elif inp == "e":
        boss67 = create_boss('boss67')
        fight(player, boss67, "Boss67")

    elif inp == "f":
        hades = create_boss('hades')
        fight(player, hades, "Hades")

    elif inp == "g":
        enemy_desc = " wrogow!"
        if s.KILLED_ENEMYS == 1:
            enemy_desc = " wroga!"
        print("Brawo ", player_name, "! Koniec gry! Wygrales", player[3], "zl! i  pokonales ", s.KILLED_ENEMYS, enemy_desc)
        break
    
    elif inp == "m":
        quests_menu()

    time.sleep(0.5)
