#will keep track of time and make an announcement at a set interval

import time
from playsound import playsound

#outputs the time in seconds since the epoch format
TIME = time.time()

#outputs the time in hour : minute : second format
LOCALTIME =str( time.localtime().tm_hour ) + " : " + str(time.localtime().tm_min) + " : " + str(time.localtime().tm_sec )

#How often should the alarm sound
def user_config(hours default = 0, minutes default = 0, seconds default = 0):
    var = time.time() - 60
    one_minute = time.time - var
    minutes *= 60
    hours *= 3600
    interval = seconds + minutes + hours
    return interval

def alarm(interval):
    if LOCALTIME

    #fix interval in user_config
    #play sound files at interval
