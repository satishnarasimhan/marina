# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import functions as f
import phrases as ph
            
# Initialization / Driver Code 
if __name__ == "__main__":
    
    f.speak("Hello there. This is Marina, your digital assistant. How can I be of help? What is your name?")
    
    person = f.get_audio()
    if person == 0:
        person = 'there'
        
    f.speak("Hello " + person + '.')
    f.speak("What can i do for you?")
    myname = "Marina"
    wake = myname
    
while(1): 
    
    data = f.get_audio()
    
    if data == 0: 
        continue

    if "Marina" in str(data) or "hey Marina" in str(data) or data.count(wake) > 0:
        f.speak("I'm listening . . Go ahead " + person)
                   
    if "exit" in str(data) or "Good bye" in str(data) or "sleep" in str(data) or "please stop" in str(data) :
        if (person == 'there'):
                f.speak("Ok. Bye for now")
        else:
            f.speak("Ok. Bye "+ person +'.')
        break       
    
    ph.talkback(data,person)

