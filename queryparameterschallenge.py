#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=3&category=20&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    #print(data)
    print(data.keys())
    #print("\nTrivia1:", data['question'])

    
    print(data['results'][0].get("question"))

if __name__ == "__main__":
    main()

