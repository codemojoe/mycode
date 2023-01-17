#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import random

# dictionary of player

# player = {
#    'health': 5,
#   'inventory': [],
#  'skills': {
#     'strength': False,
#       'dexterity': False,
#       'intelligence': False
#    }
# }

# player class
class Player:
    def __init__(self):
        self.inventory = [],
        self.health = 5,
        self.skills = [{"strength": 5}, {"dexteriy": 5}, {"intelligence": 5}]

# room class
class Room:
    def __init__(self):
        # start the player in the Hall
        self.currentRoom = 'Hall',
        self.rooms = {
            'Hall': {
                'south': 'Kitchen',
                'east': 'Dining Room',
                'north': 'Weapons Room',
                'item': 'key'
            },
            'Kitchen': {
                'north': 'Hall',
                'item': {'monster': {'health': 5},
                         'food': 'apple'}
            },
            'Dining Room': {
                'west': 'Hall',
                'south': 'Garden',
                'item': 'potion'
            },
            'Garden': {
                'north': 'Dining Room'
            },
            'Weapons Room': {
                'south': 'Hall',
                'item': 'silver sword'
            },
            'Dungeon': {
                'north': 'Kitchen',
                'item': {'locked': True,
                         'chest': 'gold coins'}
            }
        }

# game class to create game object
class Game:
    # def __init__(self):

    def showInstructions(self):
        """Show the game instructions when called"""
        # print a main menu and the commands
        print('''
        RPG Game
        ========
        Commands:
        go [direction]
        get [item]
        ========
        To Win:
        Get to the Garden with a key
        and potion to win! Avoid the
        monsters! 
        ''')

    def showStatus(self, room, player):
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print('You are in the ', room.currentRoom)
        # print what the player is carrying
        print('Inventory:', player.inventory)
        # check if there's an item in the room, if so print it
        if "item" in room.currentRoom:
            print('You see a ' + room.currentRoom['item'])
        print("---------------------------")


# an inventory, which is initially empty
# inventory = []

def main():
    game = Game()
    player = Player()
    room = Room()

    game.showInstructions()
    # breaking this while loop means the game is over
    while True:
        game.showStatus(room, player)

        # the player MUST type something in
        # otherwise input will keep asking
        move = ''
        while move == '':
            move = input('>')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]
        move = move.lower().split(" ", 1)

        # if they type 'go' first
        if move[0] == 'go':
            # check that they are allowed wherever they want to go
            if move[1] in room.currentRoom:
                # set the current room to the new room
                room.currentRoom = room.currentRoom[move[1]]
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')

        # if they type 'get' first
        if move[0] == 'get':
            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "item" in room.currentRoom and move[1] in room.currentRoom['item']:
                # add the item to their inventory
                player[1].append(move[1])
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item key:value pair from the room's dictionary
                del room.currentRoom['item']
            # if there's no item in the room or the item doesn't match
            else:
                # tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
        if 'item' in room.currentRoom and 'monster' in room.currentRoom['item'] and 'silver sword' not in player.inventory:
            print('A monster has got you... GAME OVER!')
            break
        if 'item' in room.currentRoom and 'monster' in room.currentRoom['item'] and 'silver sword' in player.inventory:
            attack_minimum = random.randint(1, 6)
            user_roll = random.randint(1, 6)
            print('Minimum roll to attack successfully: ', attack_minimum)
            print('Your roll: ', user_roll)
            if attack_minimum <= user_roll:
                print('A monster appears before you, but you slay it as it approaches.')

            else:
                print(
                    'A monster appears before you, but before you could act, it attacks...')

            # Define how a player can win
        if room.currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory or 'cookie':
            print(
                'You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break


if __name__ == "__main__":
    main()

