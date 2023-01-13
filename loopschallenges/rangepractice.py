#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

for bottle in range(99, 0, -1):
    if bottle > 1:
        print(f'{bottle} bottles of beer on the wall!')
        print(f'{bottle} bottles of beer on the wall! {bottle} bottles of beer! You take one down, pass it around!' )
    else:
        print(f'{bottle} bottle of beer on the wall!')
        print(f'{bottle} bottle of beer on the wall! {bottle} bottle of beer! You take one down, pass it around!' )
