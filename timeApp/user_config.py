#user configuration for alarm settings

#When should the alarm sound
def user_config():
    user_input = input("""Please enter when you would like the alarm to sound. \n
      Use the 'hour, minute, second' format""" end = " ")
    #turn user_input into usable variables
    hours, minutes,seconds = determine_variable(user_input)
    #convert user_input into seconds
    hours *= 3600
    minutes *= 60
    #make a countdown to keep track of how long it has been since the last alarm
    #based off of user input
    ##
    #Have user input how often it should go off
    #Have user input days on which it should go off 



def determine_variable(user_input):
    #split the input into a list of integers
    config_list = user_input.split(",")
    hours = int(config_list[0])
    minutes = int(config_list[1])
    seconds = int(config_list[3])
    return hours, minutes, seconds


"""
    #code that I forget the point of
    #doubt its still useful, have changed approach
    var = time.time() - 60s
    one_minute = time.time - var
    minutes *= 60
    hours *= 3600
    interval = seconds + minutes + hours
    return interval
"""
