#will keep track of time and make an announcement at a set interval

import time
import user_config
import wavPlayer2

def countdown(seconds_till_start):
    #Counts down to when alarm should start
    #may be moved to announcer.py
    time_to_start = time.time() + seconds_till_start
    while True:
        time.time()
        time.sleep(5)
            if time.time() = time_to_start:

                #if asctime = name of file -> init
                #code for alarm to sound
                #probably in announcer.py

def choose_file():
    #take the asctime and exclude the extraneous output
    #(day, Month, day of month, and year)
    hour_now = time.asctime().split(" ")
    hour_now = hour_now[3]
    hour_now = hour_now.split(":")
    hour_now = 24 - hour_now[0]
    if hour_now ==
    #create library of time to spelling?
