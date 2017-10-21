#user configuration for alarm settings

import time

def user_config():
    """Parent function; unites all other functions within this module.
Utilizes all other functions to determine a start time for the alarm and pass
it to announcer.py"""

    user_input = input("""Please enter when you would like the alarm to begin. \n
Use the 'hour, minute, second, am/pm' format: """)

    #convert input into 24-hour day format integers
    hours, minutes, seconds = determine_input(user_input)

    #for sake of debugging
    if type(seconds) is NoneType:
        print("ERROR: seconds is NoneType")
    elif type(minutes) is NoneType:
        print("ERROR: minutes is NoneType")
    elif type(hours) is NoneType:
        print("ERROR: hours is NoneType")

    #get the current time from asctime and convert it to integers
    current_hour, current_minute, current_second = split_time()
    current_hour, current_minute, current_second = int(current_hour), int(current_minute), int(current_second)

    #calculate when the alarm will start
    start_hour = hours - current_hour
    start_minute = minutes - current_minute
    start_second = seconds - current_second

    #convert time until start into seconds
    seconds_till_start = seconds_time(start_hour, start_minute, start_second)

    #return to whatever module calls user_config()
    return seconds_till_start




def determine_input(user_input):
    """Convert user input into separate units of time (hour, minute, second)"""

    #split string into a list
    config_list = user_input.split(",")

    #prevents errors from lack of or superfluous input
    if len(user_input) != 4:
        print("ERROR: not enough input information")
        print(config_list)
        print(len(config_list))

    #Convert appropiate places in list to integers representing a time
    hours = int(config_list[0])
    minutes = int(config_list[1])
    seconds = int(config_list[2])
    time_of_day = config_list[3]

    #convert to a 24-hour day format
    hours = army_time(hours, time_of_day)

    return hours, minutes, seconds


def army_time(hours, time_of_day):
    """Convert the hours input into a 24-hour day format"""

    #added space to am and pm because of input style
    if time_of_day == " pm":
        hours += 12
        return hours

    elif hours == " am":
        return hours

    else:
        print("ERROR: time of day must be ' am' or ' pm'")
        print(time_of_day)


def split_time():
    """Get only the time from time.asctime()"""

    #retrieve only the time from time.asctime,
    #split it by hours, minutes, and seconds
    only_time = time.asctime().split(" ")
    only_time = only_time[3]
    only_time = only_time.split(":")
    return only_time


def seconds_time(start_hour, start_minute, start_second):
    """Convert everything into seconds, making it easier to do the math"""

    start_hour *= 3600
    start_minute *= 60

    #combine everything for a countdown
    seconds_till_start = start_hour + start_minute + start_second

    return seconds_till_start



user_config()
