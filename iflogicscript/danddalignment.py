#!/usr/bin/env python3

import random

def main():

    #counter
    counter = 0
    
    #get user input for type of monster to fight, each have health values
    print("Goblin: 3 health \n")
    print("Orc: 5 health \n")
    monstertype = input("What kind of monster would you like to fight? \n")
    if monstertype.lower() == "goblin":
        monsterhealth = 3
    elif monstertype.lower() == "orc":
        monsterhealth = 5
    else:
        print("Something went wrong.")
    
    #default to true until attack is halted by user or monster dies
    while True:    
        try:
            #characterhealth
            characterhealth = 5

            #roll 2 die with random
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            total = die1 + die2
            print("Your dice roll total: ", total)

            #attack success threshold
            minimum = random.randint(1,12)
            print("Your miminum roll must be:", minimum, "to land.")
            
            #condition if attack misses and monster has health
            if minimum > total and monsterhealth > 0:
                print("Your attack missed. The monster attacks you back.")
                characterhealth -= 1
                print("Your health is ", characterhealth)
                attack = input("Would you like to continue your attack? True or False \n")
                if attack == "False":
                    break

            #condition if attack lands
            elif minimum < total and monsterhealth > 0:
                monsterhealth -= 1
                print("Your attack landed. The monster's health is ", monsterhealth)
                attack = input("Would you like to continue your attack? True or False \n")
                if attack == "False":
                    break

            #monster health is finally 0
            elif monsterhealth == 0:
                print("You killed the monster.")
                break

        except Exception as err:
            print("Something went wrong.")

if __name__ == "__main__":
    main()
