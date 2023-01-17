#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - JSON to CSV"""

import pandas

def main():

    #create data frame from json
    df = pandas.read_json("5movies.json")

    #writeout df to CSV
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()