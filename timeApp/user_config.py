#user configuration for alarm settings

import time

#When should the alarm sound
def user_config():
    user_input = str(input("""Please enter when you would like the alarm to sound. \n
Use the 'hour, minute, second, am/pm' format: """))
    #turn user_input into usable variables
    hours, minutes, seconds = determine_variable(user_input)
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    #prevent errors from user input occuring
    if type(seconds) is not NoneType:
        #gathr the current asctime
        current_hour, current_minute, current_second = split_time()
        current_hour, current_minute, current_second = int(current_hour), int(current_minute), int(current_second)
        #how long until the alarm should begin
        start_hour = hours - current_hour
        start_minute = minutes - current_minute
        start_second = seconds - current_second
        #convert all times to seconds
        seconds_till_start = seconds_time(start_hour, start_minute, start_second)
        return seconds_till_start
    else:
        print("ERROR #1 Not all fields were filled out.  Please try again.")


def determine_variable(user_input):
    #split the input into a list of integers
    config_list = user_input.split(",")
    #prevent errors from user input occuring
    if len(user_input) == 4:
        hours = int(config_list[0])
        minutes = int(config_list[1])
        seconds = int(config_list[2])
        #Did they type am or pm
        time_of_day = config_list[3]
        #get army time
        hours = army_time(hours, time_of_day)
        return hours, minutes, seconds
    else:
        print("ERROR #2 Not all fields were filled out.  Please try again.")

def split_time():
    #take the asctime and exclude the extraneous output
    #(day, Month, day of month, and year)
    atime = time.asctime().split(" ")
    atime = atime[3]
    atime = atime.split(":")
    atime = atime
    return atime

def army_time(hours, time_of_day):
    #convert time to army time
    if time_of_day == "pm":
        extra_hours = 24 - hours
        hours += extra_hours
        return hours
    elif time_of_day == "am":
        return hours

def seconds_time(start_hour, start_minute, start_second):
    #convert all hours and minutes to seconds
    start_hour *= 3600
    start_minute *= 60
    #add all three function inputs to get the amount of time until the start
    #of the alarm in seconds
    seconds_till_start = start_hour + start_minute + start_second
    return seconds_till_start

user_config()
