import inquirer
import random
from call import *

#loads pokemon into dictionary
def load_pokemon(count):
    data = {}
    for i in range(1, count + 1):
        dp = make_call("pokemon", str(i))
        data[dp["name"]] = dp
    return data

#lists out options for the user to pick and returns user input
def get_input(prompt, choices_arr):
    questions = [
        inquirer.List('query', message=prompt, choices=choices_arr,),
    ]
    return inquirer.prompt(questions)['query']

#get users pokemon
def get_pokemon(data):
    names = []
    for i in data.keys():
        names.append(i)
    print(names)
    ui = input("Choose your pokemon: ")
    while ui not in names:
        ui = input("Invalid pokemon. Choose your pokemon: ")
    confirm = input("You chose " + ui + ". Confirm choice? (y/n): ")
    while confirm != "y":
        ui = input("Choose your pokemon: ")
        while ui not in names:
            ui = input("Invalid pokemon. Choose your pokemon: ")
        confirm = input("You chose " + ui + ". Confirm choice? (y/n): ")
    return data[ui]

def get_enemy_pokemon(data):
    number = random.randint(1, len(data) + 1)
    for pokemon in data.keys():
        if (data[pokemon]["id"] == number):
            return data[pokemon]