# -*- coding: utf-8 -*-

import requests
import json
import datetime
import pickle
import time

class Astro_miner:
    
    def __init__(self):
        self.start = datetime.datetime(1995, 6, 16, 0, 0, 0)
        self.today = datetime.datetime.today()
        print("To start mining, first obtain a key at https://api.nasa.gov/")
    
    def mine(self, key, start_from_pickle = False, file_name = "nasa_descriptions_test.txt"):
        if start_from_pickle:
            self.start = pickle.load(open("last_date", "rb"))
    
        date_list = [(self.start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((self.today-self.start).days)]
        
        nasa_descriptions = open(file_name, "a", encoding="utf-8")
        
        for c, date in enumerate(date_list):
            
            response = requests.get("https://api.nasa.gov/planetary/apod?api_key={}&date={}".format(key, date))
            
            #if too many requests have been made, the miner waits 10 minutes and tries again, untill response 429 is resolved.
            while response.status_code == 429:
                print("Trying again in 10 minutes")
                time.sleep(600)
                response = requests.get("https://api.nasa.gov/planetary/apod?api_key={}&date={}".format(key. date))
            
            #only write the the file when a 200 response has been received. Sometimes the server sends a 500 response for some reason.
            if response.status_code == 200:
                nasa_descriptions.write(response.json()["explanation"])
                
            #prints after 100 succesful requests the progress
            if c % 100 == 0:
                print(c, date)
                pickle.dump(date, open("last_date", "wb"))

        nasa_descriptions.close()    
