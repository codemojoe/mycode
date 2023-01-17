#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)

    #print(pokeapi["sprites"]["front_default"])

    for name in pokeapi["moves"]:
        print(name["move"]["name"])


    print(pokeapi["game_indices"].len)

    games = 0
    for name in pokeapi["game_indices"]:
        games += 1

    print(games)
main()

