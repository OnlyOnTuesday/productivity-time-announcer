#will keep track of time and make an announcement at a set interval

import time
from playsound import playsound

#outputs the time in seconds since the epoch format
TIME = time.time()

#outputs the time in hour : minute : second format
LOCALTIME =str( time.localtime().tm_hour ) + " : " + str(time.localtime().tm_min) + " : " + str(time.localtime().tm_sec )

def alarm(interval):
    if LOCALTIME

    #fix interval in user_config
    #play sound files at interval
