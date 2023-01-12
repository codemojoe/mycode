#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    count = 0
    configlist = configfile.readlines()
    for x in configfile:
        count += 1
print(count)
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
