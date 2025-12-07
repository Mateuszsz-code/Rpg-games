from random import randint, choice

def create_boss(name):
    boss = [150, randint(20,30), randint(50,150)] #hp , atak , zloto
    wolf = [100, randint(15,25), randint(30,100)] #hp , atak , zloto
    cave_boss = [225, randint(30,40), randint(100,300)] #hp , atak , zloto
    cave_boss67 = [275, randint(35,45), randint(150,400)] #hp , atak , zloto
    town_boss = [300, randint(40,50), randint(200,500)] #hp , atak , zloto
    town_boss67 = [325, randint(35,55), randint(250,550)] #hp , atak , zloto
    mango_mustard = [340, randint(50,55), randint(300,500)] #hp , atak , zloto
    boss67 = [350,randint(45,60),randint(300,700)] #hp , atak , zloto
    hades = [400, randint(50,70), randint(500,1000)] #hp , atak , zloto

    if name == "boss":
        forest_enemies = [boss, wolf]
        return choice(forest_enemies)
    
    elif name == "cave_boss":
        cave_enemies = [cave_boss, cave_boss67]
        return choice(cave_enemies)
    
    elif name == "town_boss":
        town_enemies = [town_boss, town_boss67]
        return choice(town_enemies)
    
    elif name == "boss67":
        boss67_enemies = [boss67, mango_mustard]
        return choice(boss67_enemies)
    
    elif name == "hades":
        return hades

