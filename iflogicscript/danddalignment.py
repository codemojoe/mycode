#!/usr/bin/env python3

import random

#Attack Result

def main():

    #counter
    count = 0

    #conditional until 5
    while count < 5:
        
        count += 1
        
        #monster health
        monsterhealth = 3
        print("The monster's health is ", monsterhealth)

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
                print("Your attack missed.")
            
            else:
                monsterhealth -= 1
                print("Your attack landed. The monster's health is ", monsterhealth)

        else:
            print("Your attack landed, and the monster is finally dead.")

main()
