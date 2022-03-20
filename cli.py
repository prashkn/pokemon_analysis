from call import *
from command import *

data = load_pokemon(127)

print("Pokemon Battle CLI")

user_pokemon = get_pokemon(data)
enemy_pokemon = get_enemy_pokemon(data)

print(user_pokemon["name"])
print(enemy_pokemon["name"])