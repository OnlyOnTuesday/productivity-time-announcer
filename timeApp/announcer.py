#will keep track of time and make an announcement at a set interval

import time

TIME = time.time()

CTIME = time.ctime()

#How often should the alarm sound
def user_config(hours default = 0, minutes default = 0, seconds default = 0):
    var = time.time() - 60
    one_minute = time.time - var
    minutes *= 60
    hours *= 3600 
    interval = seconds + minutes + hours
    return interval

def alarm(interval):
    #fix interval in user_config
    #play sound files at interval
