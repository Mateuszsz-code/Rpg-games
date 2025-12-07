from random import randint

def create_player():
    return [250, randint(25, 50), randint(15, 30),0]  
    # HP, Atak, leczenie, money

def show_player(player, player_name):
    print(f"\t{player_name}: hp: {player[0]} atak: {player[1]} leczenie: {player[2]} money: {player[3]}")
