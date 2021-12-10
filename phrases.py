# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:55:12 2021

@author: Satish Narasimhan
"""

import os
from gtts import gTTS
from playsound import playsound
from newspaper import Article
import webbrowser
import time
from datetime import datetime
import geocoder
import functions as f
import space_info as spi
import weather as wea
import static as s

def talkback(data, person):
    myname = "Marina"
    name = person
 
    if "how are you" in data:
        f.speak("I am fine " + name + ". Thank you.")

    if "what is your name" in data or "who are you" in data or "identify yourself" in data:
        f.speak("My name is " + myname + ". I am a digital assistant. What can I do for you today ? How can I be of help?")
        
    if "what is the time" in data:
        currtime = datetime.now().strftime("%I:%M %p")
        f.speak("It is " + currtime)
        
    if "what day is it" in data:
        currdate = datetime.now().strftime("%A, %d %B %Y")
        f.speak("It is " + currdate)
            
    if "where is" in data:
        idx = 2
        delimiter = " "
        search_string = f.search_ops(idx, delimiter, data)
        f.speak("Hold on, I will show you where " + search_string + " is.")
        webbrowser.open_new_tab("https://www.google.nl/maps/place/" + search_string + "/&amp;")

    if "good morning" in str(data) or "good evening" in str(data) or "good afternoon" in str(data) or "good night" in str(data):
        
        meridian = time.strftime('%p')
        greeting = str(data)
        if (meridian == "PM" and (greeting != "good morning")) or (meridian == "AM" and greeting == "good morning"):
            f.speak("hi " + greeting)
        elif meridian == "AM":
            f.speak("It is already morning " + person + ". So good morning. Hope you had a good night's sleep")
        elif meridian == "PM":
            f.speak("It is already late in the evening " + person + ". Hope you had a good day")
    
    if "Google this" in data:
        f.speak("Opening Google")
        idx = 2
        delimiter = " "
        search_string = f.search_ops(idx, delimiter, data)
        webbrowser.open_new_tab("https://www.google.com/search?q=" + search_string + "&start=")
        
    if "search Wikipedia for" in data:
        f.speak("Opening Wikipedia")
        idx = 3
        delimiter = '_'
        search_string = f.search_ops(idx, delimiter, data)
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/" + search_string)

    if "search video" in data:
        f.speak("Hold on, " + name + " . Opening You Tube")
        idx = 2
        delimiter = '+'
        search_string = f.search_ops(idx, delimiter, data)
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + search_string)
        
    if "play video" in data:
        f.speak("Hold on, " + name + " . Opening You Tube")
        idx = 2
        delimiter = '+'
        search_string = f.search_ops(idx, delimiter, data)
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + search_string +"?autoplay=1&mute=1")
    
    if "when is the next Space Station pass over" in data: 
        idx = 8
        delimiter = ''
        search_string = f.search_ops(idx, delimiter, data)
        g = geocoder.opencage( search_string , key = s.open_cage_api_key)
        lat = str(round(g.latlng[0],4))
        lon = str(round(g.latlng[1],4))
        
        # iss_json = iss.iss_passes(g.latlng[0], g.latlng[1], 5, 1)
        issinfo = spi.visual_pass(lat, lon)
        
        flybydate = issinfo[0]
        flybytime = issinfo[1]
        mins = issinfo[2]
        secs = issinfo[3]
        
        f.speak("The next flyby of the International Space Station over " + search_string + " is on " + flybydate + " at " + flybytime + " for a duration of " + mins + " minutes and " + secs + " seconds.")
        #speak(flybydate.strftime("%A, %d %B %Y"))
        #speak(flybytime.strftime("%I:%M %p"))
    
    if "Space Station crew" in data or "Space Station staff" in data or "who are the Space Station crew" in data or "who are the Space Station staff" in data:
        f.speak("Here you go")
        resp = spi.iss_crew()
        f.speak(resp)

    if "what is in the news" in data:
        f.speak("Hold on, I will read the main headline for you " + name)
        url = 'https://www.axios.com/'
        article = Article(url, language="en")
        article.download()
        article.parse()
        # nltk.download('punkt')
        article.nlp()
        #converting article into text 
        text = article.text
        speech = gTTS(text = text, lang = "en")
        speech.save('news.mp3')
        playsound('news.mp3')
## Remove file after playing. There would be no need to re-run the program    
        os.remove('news.mp3')
                
    if "how is the local weather" in data:
        winfo = wea.weather_info_local()
        
        search_string = winfo[0]
        description = winfo[1]
        temp = winfo[2]
        humidity = winfo[3]
        
        f.speak ("Currently the weather in " + search_string + " is " + description +" . The temperature is " + temp + " degrees Celsius and humidity is " + humidity + " percent")

        
    if "how is the weather in" in data :
        idx = 5
        delimiter = ''
        search_string = f.search_ops(idx, delimiter, data)
        
        g = geocoder.opencage( search_string , key = s.open_cage_api_key)
        lat = g.latlng[0]
        lon = g.latlng[1]
        
        winfo = wea.weather_info(search_string, lat, lon)
        
        search_string = winfo[0]
        description = winfo[1]
        temp = winfo[2]
        humidity = winfo[3]
                
        f.speak ("Currently the weather in " + search_string + " is " + description +" . The temperature is " + temp + " degrees Celsius and humidity is " + humidity + " percent")
        
    if "write into to do list" in data or "update to do list with" in data:
        f.speak("Here you go " + name)
        idx = 5
        delimiter = ''
        search_string = f.search_ops(idx, delimiter, data)
        f.write_file(search_string)
        
    if "read my to do list" in data or "what is in my to do list" in data :
        f.speak("Hold on")
        f.speak("Here you go " + name)
        f.read_file()
    
    if ("expert level knowledge" in data or "expert level check" in data or "expert level capability" in data or "expert mode" in data):
        f.speak ("Let me see if I can help you")
        f.speak ("Go ahead with your query")
        f.get_compute_response()
        