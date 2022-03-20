from call import *
from command import *

data = load_pokemon(20)

print("Pokemon Battle CLI")

#get both pokemon
user_pokemon = get_pokemon(data)
enemy_pokemon = get_enemy_pokemon(data)

#get user moves
print("Your " + user_pokemon["name"] + " is up against " + enemy_pokemon["name"] + "! Time to choose your moves.")
confirm = ""
while confirm != "y":
    move_names = choose_moves(user_pokemon, 4)
    confirm = input("Confirm moves? " + str(move_names) + ". (y/n): ")

