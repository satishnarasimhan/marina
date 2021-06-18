# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:12:55 2021

@author: Satish Narasimhan
"""
from datetime import datetime
import functions as f
import ISS_Info as iss

base_url = '<<Provide base URL here>>'
api_key = '<<Provide the API Key here>>' # Celestrak, N2YO

def visual_pass(latitude, longitude):
    lat = latitude
    lon = longitude
    req_type = 'visualpasses' # tle, visualpasses, positions, radiopasses
    norad_id = str(25544) #Default is ISS Norad Id , 20580 for Hubble
    
    append_api_key = ('&apiKey=')+api_key
    alt = str(0) # Altitude
    dur = str(100) # duration for which pass is visible
    days = str(10) # number of days. Max is 10
    const_url = [base_url,req_type,norad_id,lat,lon,alt,days,dur,append_api_key]
    
    visual_pass_url = f.url_const_ops('/',const_url)
    visual_pass_response = f.get_Response(visual_pass_url)
    risetime = f.extract_element_from_json(visual_pass_response, ["passes","startUTC"])
    dur = f.extract_element_from_json(visual_pass_response, ["passes","duration"])
        
    duration = dur[0]
        
    minutes_dur = str(int(duration/60))
    seconds_dur = str(duration%60)
        
    flybydate = datetime.fromtimestamp(risetime[0]).strftime("%A, %d %B %Y")
    flybytime = datetime.fromtimestamp(risetime[0]).strftime("%I:%M %p")
    print(flybydate, flybytime)
    
    return (flybydate, flybytime, minutes_dur, seconds_dur)

def iss_crew():
    iss_occupants = iss.iss_people_in_space()
    crew_name = f.extract_element_from_json(iss_occupants, ["people","name"])
    num = len(crew_name)
    f.speak("There are " + str(num) +" members in the I S S. The crew members are")
    print(crew_name)
    
    for i in range(len(crew_name)):
        f.speak(str(crew_name[i]))
             
    st = "I hope that was useful "
    return st