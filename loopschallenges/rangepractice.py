#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

atbottle = int(input("What number bottle would you like to count?\n"))
atbottle = 99 - atbottle

if atbottle > 100:
    print("Invalid input, cannot go over 100 bottles")
    atbottle = int(input("What number bottle would you like to start with?"))

for bottle in range(99, atbottle, -1):
    if bottle > 1:
        print(f'{bottle} bottles of beer on the wall!')
        print(f'{bottle} bottles of beer on the wall! {bottle} bottles of beer! You take one down, pass it around!' )
    else:
        print(f'{bottle} bottle of beer on the wall!')
        print(f'{bottle} bottle of beer on the wall! {bottle} bottle of beer! You take one down, pass it around!' )
