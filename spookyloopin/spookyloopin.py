#!/usr/bin/env python3

#read in content of Dracula novel as file object
with open("dracula.txt", "r") as dracula_file:
    count = 0
    with open("vampytimes.txt", "a") as vampyfile:
        for line in dracula_file:
            if "vampire" in line.lower():
                count += 1
                print(line)
                vampyfile.write(line)
    print("Vampire occurs in: ",count, "lines")
