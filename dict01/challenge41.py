#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) \n")

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy \n")

    ## display the entire dictionary
    marvelchars= {
    "Starlord":
      {"real name": "peter quill",
      "powers": "dance moves",
      "archenemy": "Thanos"},
    "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},
    "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }

    print(marvelchars[char_name][char_stat])
  #  print(marvelchars.values().lower().get(char_name).get(char_stat))

   # print(char_name + " " + char_stat + " is:" marvelchars.get(char_name.lower()))

# call our main function
if __name__ == "__main__":
    main()

