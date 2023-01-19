#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import time
import random

URL= "https://opentdb.com/api.php?amount=3&category=20&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    #print("Data: ",data)
    #print(data.keys())
    
    #get results from json data
    results = data['results']
    #print("Data['results']: ",results)

    all_answers = []

    for result in results:
        print(result['question'])

        #trying to implment random to display random incorrect answer order // not working yet
        random_ans = random.randint(0,3)
        
        time.sleep(2)
        
        correct_answer = result['correct_answer']
        all_answers.append(correct_answer)

        #print incorrect and correct answers
        for incorrect_answer in result['incorrect_answers']:
            all_answers.append(incorrect_answer)
        
        print(all_answers)
        #clear list for new results object answers
        all_answers.clear()

        #print correct answer after 5 seconds
        print("The correct answer is: \n")
        time.sleep(5)
        print(result['correct_answer'])
        
        print()

    print("That's all the trivia questions, thanks for playing!")




    #get first trivia object
    #first_trivia = results[0]
    #option1 = first_trivia['incorrect_answers'][0]
    #option2 = first_trivia['incorrect_answers'][1]
    #option3 = first_trivia['incorrect_answers'][2]
    
    #provide options for answer
    #print(first_trivia['question'])
    #print(first_trivia['correct_answer'])
    #print(option1)
    #print(option2)
    #print(option3)
    
    #print()
    #set timer for 10 seconds until showing correct answer
    #time.sleep(10) 
    #print(first_trivia['correct_answer'])

if __name__ == "__main__":
    main()

