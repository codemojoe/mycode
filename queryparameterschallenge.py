#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import time

URL= "https://opentdb.com/api.php?amount=3&category=20&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    #print(data)
    #print(data.keys())
    
    #get results from json data
    results = data['results']
    #print(results)

    #get first trivia object
    first_trivia = results[0]
    option1 = first_trivia['incorrect_answers'][0]
    option2 = first_trivia['incorrect_answers'][1]
    option3 = first_trivia['incorrect_answers'][2]
    
    #provide options for answer
    print(first_trivia['question'])
    print(first_trivia['correct_answer'])
    print(option1)
    print(option2)
    print(option3)
    
    print()
    #set timer for 10 seconds until showing correct answer
    time.sleep(10) 
    print(first_trivia['correct_answer'])

if __name__ == "__main__":
    main()

