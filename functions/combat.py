from random import randint
from . import statistics as s
from .atack import simple_attack, fire_ball, rocket, lighting, earth_quake
from .quests import complete_forest_beast, complete_cave_monster, complete_city_guardian, complete_world_monster_67

enchant_list = ["Fire", "Ice", "Lightning", "Earth", "Wind"]

def fight(player, enemy, enemy_name):
    if enemy_name == "Hades":
        if s.QUEST_FOREST_BEAST and s.QUEST_CAVE_MONSTER and s.QUEST_CITY_QUARDIAN and s.QUEST_WORLD_MONSTER_67:
            print("Brawo! Udalo ci sie ukonczyc wszystkie misje i mozesz zawalczyc z hadesem!")
        else:
            print("Aby zawalczyc z Hadesem musisz najpierw ukonczyc wszystkie misje!")
            return False

    print(f"Walka! Spotkales {enemy_name}!")

    while True:
        if player[0] < 0:
            print("Game over!")
            break

        if enemy[0] < 0:
            if enemy_name == "Hades":
                print(f"Brawo przeszedles gre bo pokonales Hadesa i zdobyles {enemy[2]} zlotych!")
                s.KILLED_ENEMYS += 1
                s.HADES_KILLED = True
                return False
            else:
                print(f"Brawo z pokonania bossa zdobyles {enemy[2]} zlotych!")
                if enemy_name == "Boss":
                    complete_forest_beast(player)
                elif enemy_name == "CaveBoss":
                    complete_cave_monster(player)
                elif enemy_name == "TownBoss":
                    complete_city_guardian(player)
                elif enemy_name == "Boss67":
                    complete_world_monster_67(player)
            player[3] += enemy[2]
            s.KILLED_ENEMYS += 1
            return True
        
        print(f"\n--- WALKA Z {enemy_name} ---")
        print(f"Player: {player}")
        print(f"{enemy_name}: {enemy}")
        print("a - atak  b - enchant  c - leczenie d - fire_ball e - rocket f - ucieczka g - lighting h - earth_quake")

        inp = input("co robisz: ")

        if inp == "a":
            simple_attack(player, enemy)

        elif inp == "b":
            e = enchant_list[randint(0,4)]
            print(f"Twoj atak zostanie wzmocniony o {e}!")
            player[1] += randint(5,10)
            player[0] -= enemy[1]

        elif inp == "c":
            player[0] += player[2]
            player[0] -= enemy[1]

        elif inp == "d":
            fire_ball(player, enemy)

        elif inp == "e":
            rocket(player, enemy)
        
        elif inp == "f":
            print("Uciekasz z walki! ale gubisz wszystkie pieniadze!")
            player[3] = 0
            break

        elif inp == "g":
            lighting(player, enemy)

        elif inp == "h":
            earth_quake(player, enemy)
