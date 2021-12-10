# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:31:11 2021

@author: Satish Narasimhan
Incomplete - To be worked on
"""

import geocoder
import static as s

def lat_lng(search_string):
    g = geocoder.opencage( search_string , key = s.open_cage_api_key)
    
    return