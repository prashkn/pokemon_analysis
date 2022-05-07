from call import *
from command import *
import climage

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

    if user_move["accuracy"] == None:
        user_move["accuracy"] = -1
    if m_data["accuracy"] == None:
        m_data["accuracy"] = -1

    user_move_hit = random.randint(0, 100) <= user_move["accuracy"]
    enemy_move_hit = random.randint(0, 100) <= m_data["accuracy"]

    if user_move["power"] == None:
        user_move["power"] = 0
    if m_data["power"] == None:
        m_data["power"] = 0
    
    if user_move["priority"] > m_data["priority"]:
        move_hits, message = does_move_hit(user_move)
        print(message)

        if move_hits:
            enemy_stats["health"] = enemy_stats["health"] - user_move["power"]

        if enemy_stats["health"] > 0:
            move_hits, message = does_move_hit(m_data)
            print(message)

            if move_hits:
                stats["health"] = stats["health"] - m_data["power"]
    else:
        move_hits, message = does_move_hit(m_data)
        print(message)

        if move_hits:
            stats["health"] = stats["health"] - m_data["power"]
        
        if stats["health"] > 0:
            move_hits, message = does_move_hit(user_move)
            print(message)

            if move_hits:
                enemy_stats["health"] = enemy_stats["health"] - user_move["power"]

    in_progress = stats["health"] > 0 and enemy_stats["health"] > 0

print("game over")