#!/usr/bin/env python3

import random

#Attack Result

def main():

    #counter
    counter = 0

    #conditional until 5
    while counter < 5:
        #monsterhealth
        monsterhealth = 3
        
        counter += 1
        print("The monster's health is ", monsterhealth)

        #characterhealth
        characterhealth = 5

        #roll 2 dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)

        #add total
        total = die1 + die2
        print("Your dice roll total: ",total)

        #attack success threshold
        minimum = random.randint(1,12)
        print("Your miminum attack total must be: ", minimum)
        
        if monsterhealth > 0:
            if minimum > total:
                print("Your attack missed. The monster attacks you back.")
                characterhealth -= 1
                print("Your health is ", characterhealth)
            else:
                monsterhealth -= 1
                print("Your attack landed. The monster's health is ", monsterhealth)

        else:
            print("Your attack landed, and the monster is finally dead.")

main()
