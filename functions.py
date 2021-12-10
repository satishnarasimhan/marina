# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:49:48 2021

@author: Satish Narasimhan
"""

import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
from more_itertools import intersperse
import json
import urllib
import wolframalpha
import functions as f
import static as s


def speak(output): 
    print(output)
    tts = gTTS(text=output, lang='en', tld = 'co.uk') # com, co.uk, co.in, ca
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")

def search_ops(idx, delimiter, data):
    data = data.split(" ")
    search = data[idx:]
    ls = list(intersperse(delimiter,search))
    search_string = ' '.join(map(str,ls))
    return search_string

def url_const_ops(delimiter, const_url):
    search = const_url
    ls = list(intersperse(delimiter,search))
    search_string = ''.join(map(str,ls))
    return search_string

def get_Response(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def read_file():
    # File path, name
    filePath = 'C:\\Users\\Nithya\\Documents\\Python\\Projects\\Marina_v2\\Marina_v2\\'
    fileName = 'ToDo.txt'

    readfile = filePath+fileName
    
    
    with open(readfile,  encoding='utf-8' , mode='r', errors='ignore') as f:
        text = f.read().lower()
        
    # Read the file from the location. Replace EOF with a blank
    #file = open(readfile, "r").read().replace("\n", " ")
    # print(text)
    speech = gTTS(text = str(text),lang = "en")
    audiofile = "audio.mp3"
    speech.save(audiofile)
    # Play audiofile
    playsound(audiofile)
    # Remove audiofile
    os.remove(audiofile)
    
def write_file(data):
    # File path, name
    filePath = 'C:\\Users\\Nithya\\Documents\\Python\\Projects\\Marina_v2\\Marina_v2\\'
    fileName = 'ToDo.txt'
    
    readfile = filePath+fileName
    if str is bytes: 
           data = "{}".format(data).encode("utf-8")
    else: 
           data = "{}".format(data)
            
    with open(readfile, encoding='utf-8', mode='a+', errors='ignore') as w:
            w.write(data)
    
    print(data)
    speech = gTTS(text = data)
    speech.save(readfile)
    
    
def get_audio(): 
    rObject = sr.Recognizer()
    audio = ''
	
    with sr.Microphone() as source:
        print("Speak...") 
        audio = rObject.listen(source, phrase_time_limit = 5) 
    print("Stop.") # limit 5 secs 

    try: 
        
        data = rObject.recognize_google(audio, language ='en') 
        print("You : ", data)
        return data

    except sr.UnknownValueError: 
        print("Sorry. Could not understand the audio input")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service; {0}".format(e))
        
    return 0

def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr

def day_of_the_week(y,  m, d) :
 
    # array with leading number of days values
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
    
    # m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February. January, the first month would count as the 13th month of the previous year)      
    # if month is less than 3 reduce year by 1
    if (int(m) < 3) :
        y = int(y - 1)
          
    return int((y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7)

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def compute(data):
    # Taking input from user
    query = data
    
    # App id obtained by the above steps
    app_id = s.app_id
    
    # Instantiate wolframalpha cient with your app id i.e. client class
    client = wolframalpha.Client(app_id)
    
    # Obtain a response for the query
    resp = client.query(query)
    
    # We are interested only in the response text
    answer = next(resp.results).text
    
    # if (str(answer) == 'None'):
    #     answer = 'Unable to check this for you at the moment'
        
    try:
        #print (next(resp.results).text)
        f.speak (next(resp.results).text)
    except StopIteration:
        f.speak ("No results")
    return answer
  
def get_compute_response(): 
    rObject = sr.Recognizer()
    audio = ''
	
    with sr.Microphone() as source:
        print("Speak...") 
        audio = rObject.listen(source, phrase_time_limit = 5) 
    print("Stop.") # limit 5 secs 
    
    try: 
        data = rObject.recognize_google(audio, language ='en') 
        print("You : ", data)
        f.speak("Checking this for you . . ")
    
        # App id obtained by the above steps
        app_id = s.app_id
        
        # Instantiate wolframalpha cient with your app id i.e. client class
        client = wolframalpha.Client(app_id)
        
        # Obtain a response for the query
        resp = client.query(data)
        
        # Obtain response. Have a default message for no results
        answer = next(resp.results, "None").text
        
        if(str(answer) == "None" or str(answer) == '(none)' or str(answer) == 'none' ):
            f.speak("I'm sorry. I can't help you with that at the moment")
        else:
            f.speak(answer)
               
    except sr.UnknownValueError: 
        print("Sorry. Could not understand the audio input")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service; {0}".format(e))
    return 0
    