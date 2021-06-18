# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:55:53 2021

@author: Satish Narasimhan
"""

from pyowm import OWM # for weather

owm_api_key = "<<Provide OWM API key>>"
open_cage_api_key = '<<Provide Open Cage API key>>'
local = 'Bengaluru, IN'

def weather_info(search_string, latitude, longitude):
    # OWM API Key
    owm = OWM(owm_api_key)
    mgr = owm.weather_manager()
    search_string = search_string
    lat = latitude
    lon = longitude
    # Search for current weather in a given city and get details
    observation = mgr.weather_at_coords(lat, lon)
    w = observation.weather
    temp = str(w.temperature('celsius')['temp'])
    humidity = str(w.humidity)
    description = str(w.detailed_status)
    
    return(search_string, description, temp, humidity)
    
    
def weather_info_local():
    owm = OWM(owm_api_key)
    mgr = owm.weather_manager()
    search_string = "Bengaluru"
        
    # Search for current weather in a given city and get details
    observation = mgr.weather_at_place(local)
    w = observation.weather    
    temp = str(w.temperature('celsius')['temp'])
    humidity = str(w.humidity)
    description = str(w.detailed_status)
    
    return(search_string, description, temp, humidity)
        