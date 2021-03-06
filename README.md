============
# Marina
============

Description
===========
Marina is a bespoke voice assistant built leveraging the Google Text To Speech(gTTS), Speech Recognition libraries integrated with Wolfram Alpha Computational Intelligence API. 

The voice assistant goes by the name Marina. Aside from answering simple greetings and queries like time, day of the week Marina can bring back computational results, google search results, wikipedia search results, youtube video search, weather forecast for a location, news headlines, and read an already created to-do list.

Marina has a keen interest in the International Space Station (ISS) and will bring back information on the next visible pass of the ISS over your city. Marina can also speak about the space station crew members.

This project has been built clearly from an academic point of view.

This is now integrated with computational intelligence using Wolfram Alpha (https://www.wolframalpha.com/)

Requirements
------------
Packages / pip installations required are:

speech_recognition, gTTS, ISS_info, geocoder, OWM, wolframalpha

Inputs to be provided for:
-----------------------------
## Provide the location to obtain Latitude and Longitude of location in search string
loc = ''
filepath = '' # Location of To-DO list .txt file

Open cage API key
open_cage_api_key = ''

OWM API Key
owm_api_key = ''

Celestrak or N2YO API Key
api_key = ''

Wolfram Alpha App Id
app_id = ''

Example(s)
------------
Sample phrases :
"search Wikipedia for aurora"
"when is the next Space Station pass over Bengaluru" 
"what is in the news"
"Space Station crew"
"how is the local weather"  -- Default is Bengaluru, India

For other cities mention the city name in the phrase
e.g. 'weather in London'

Computational Intelligence:
"what day of the week was 15th August 1947"
"what is the hundredth digit of the value of pi"
"what is the capital of the state of Goa"
"who was the 31st President of the United States"
