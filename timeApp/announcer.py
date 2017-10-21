#will keep track of time and make an announcement at a set interval

import time
import user_config
import wavPlayer
import math
import sys
import user_config
#make the wav files available for import
sys.path.insert(0, "../times")

#associate integers with strings
#allows us to use asctime to call files from inside the times folder
times_library = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",\
8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"one", 14:"two", 15:"three",\
16:"four", 17:"five", 18:"six", 19:"seven", 20:"eight", 21:"nine", 22:"ten", 23:"eleven",\
24:"twelve"}
#allows us to know if it is am or pm
greater_than_twelve = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def countdown():
    seconds_till_start = user_config.user_config()
    #Counts down to when alarm should start
    time_to_start = math.floor(time.time() + seconds_till_start)
    while True:
        math.floor(time.time())
        time.sleep(5)
        if math.floor(time.time()) >= time_to_start:
            file_to_play, ampm = choose_file()
            #play the time
            wavPlayer.__init__(file_to_play)
            wavPlayer.play
            wavPlayer.close
            #play am or pm
            wavPlayer.__init__(ampm)
            wavPlayer.play
            wavPlayer.close

def choose_file():
    #take the asctime and exclude the extraneous output
    #(day, Month, day of month, and year)
    hour_now = time.asctime().split(" ")
    hour_now = hour_now[3]
    hour_now = hour_now.split(":")
    hour_now = int(hour_now[0])
    if hour_now in times_library:
        #if it is afternoon
        if hour_now in greater_than_twelve:
            #turn the hour into a importable module file
            file_to_call = times_library[hour_now] + ".wav"
            from times import file_to_call
            from times import pm
            pm = pm.wav
            return file_to_call, pm
        else:
            #turn the hour into a importable module file
            file_to_call = times_library[hour_now] + ".wav"
            from times import file_to_call
            from times import am
            am = am.wav
            return file_to_call, am

    #create library of time to spelling?

countdown()
