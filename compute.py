# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:19:17 2021

@author: Satish Narasimhan
"""

import wolframalpha
import static as s
import functions as f

def compute():
        
    # Taking input from user
    question = input('Question: ')
    
    # App id obtained by the above steps
    app_id = s.app_id
    
    # Instantiate a wolframalpha client class
    client = wolframalpha.Client(app_id)
    
    # Obtain a response for the question
    resp = client.query(question)
    
    # We are interested only in the response text
    #print(resp)
    #print(type(resp))
    #print(type(next(resp.results).text))
    answer = next(resp.results, "None").text
    #print(type(answer))
    f.speak(answer)
    
    print(answer)
    
    
compute()


# if (str(answer) == 'None'):
#     speak ("I am sorry. I can't help you with this at the moment")
# else:
#     speak(answer)
        