from . import statistics as s

quest_forest_beast_desc = "Pokonaj Bestię z Lasu, która terroryzuje okolicę."
quest_forest_beast_reward = 50  # złota

quest_city_guardian_desc = "Obroń miasto pokonując jego Strażnika."
quest_city_guardian_reward = 75  # złota

quest_cave_monster_desc = "Wejdź do mrocznej jaskini i pokonaj potwora."
quest_cave_monster_reward = 100  # złota

quest_67_world_monster_desc = "Wejdź do świata 67 i pokonaj potwora."
quest_67_world_monster_reward = 125

def quests_menu():
    print("\n=== MISJE ===")
    if s.QUEST_FOREST_BEAST:
        desc1 = " [v]"
    else:
        desc1 = " [x]"
    print("1. Bestia z Lasu" + desc1)
    if s.QUEST_CITY_QUARDIAN:
        desc2 = " [v]"
    else:
        desc2 = " [x]"
    print("2. Strażnik Miasta" + desc2)
    if s.QUEST_CAVE_MONSTER:
        desc3 = " [v]"
    else:
        desc3 = " [x]"
    print("3. Potwór w Jaskini" + desc3)
    if s.QUEST_WORLD_MONSTER_67:
        desc4 = " [v]"
    else:
        desc4 = " [x]"
    print("4. Potwór Świata 67" + desc4)
    print("0. Powrót")

    choice = input("Wybierz misję, aby zobaczyć szczegóły: ")

    if choice == "1":
        show_quest_forest_beast()
    elif choice == "2":
        show_quest_city_guardian()
    elif choice == "3":
        show_quest_cave_monster()
    elif choice == "4":
        show_quest_world_monster_67()


def show_quest_forest_beast():
    print("\n--- BESTIA Z LASU ---")
    print(quest_forest_beast_desc)
    print("Nagroda:", quest_forest_beast_reward, "złota")

def show_quest_city_guardian():
    print("\n--- STRAŻNIK MIASTA ---")
    print(quest_city_guardian_desc)
    print("Nagroda:", quest_city_guardian_reward, "złota")

def show_quest_cave_monster():
    print("\n--- POTWÓR W JASKINI ---")
    print(quest_cave_monster_desc)
    print("Nagroda:", quest_cave_monster_reward, "specjalny przedmiot")

def show_quest_world_monster_67():
    print("\n--- POTWÓR ŚWIATA 67 ---")
    print(quest_67_world_monster_desc)
    print("Nagroda:", quest_67_world_monster_reward, "specjalny przedmiot")

def complete_forest_beast(player):
    if not s.QUEST_FOREST_BEAST:
        s.QUEST_FOREST_BEAST = True
        player[3] += quest_forest_beast_reward
        print("\nUkończono misję: Bestia z Lasu!")
        print("+", quest_forest_beast_reward, "złota")

def complete_city_guardian(player):
    if not s.QUEST_CITY_QUARDIAN:
        s.QUEST_CITY_QUARDIAN = True
        player[3] += quest_city_guardian_reward
        print("\nUkończono misję: Strażnik Miasta!")
        print("+", quest_city_guardian_reward, "złota")

def complete_cave_monster(player):
    if not s.QUEST_CAVE_MONSTER:
        s.QUEST_CAVE_MONSTER = True
        player[3] += quest_cave_monster_reward
        print("\nUkończono misję: Potwór w Jaskini!")

def complete_world_monster_67(player):
    if not s.QUEST_WORLD_MONSTER_67:
        s.QUEST_WORLD_MONSTER_67 = True
        player[3] += quest_67_world_monster_reward
        print("\nUkończono misję: Potwór Świata 67!")
