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
move_data = get_move_data(move_names)

#get enemy moves
enemy_move_data = get_random_moves(enemy_pokemon, 4)

print("Your moves have been set. " + enemy_pokemon["name"] + " moves have been set. Start the game.")

#keep track of stats
stats = {}
stats["health"] = 100

enemy_stats = {}
enemy_stats["health"] = 100

in_progress = stats["health"] > 0 and enemy_stats["health"] > 0
while in_progress:

    #confirm move
    confirm = ''
    while confirm != 'y':
        move_name = get_input("Choose your move", move_names)
        confirm = input("Confirm " + move_name + "? (y/n): ")
    
    user_move = move_data[move_name]

    #get enemy move
    m_data = random.choice(list(enemy_move_data.values()))

    
    print("You chose " + user_move["name"] + "!")
    print(enemy_pokemon["name"] + " chose " + m_data["name"] + "!")
    in_progress = False