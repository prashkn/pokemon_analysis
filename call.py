import requests

def make_call(type, query):
  response = requests.get(f'https://pokeapi.co/api/v2/{type}/{query}')
  return response.json()