# Declaring aa class
class Time:
    second = 0
    hour = 0
    minute = 0


# Providing Inputs to variables of class
time = Time()
time.hour = 1  # 1 hour = 3600 seconds
time.minute = 10  # 10 minutes = 600 seconds
time.second = 20


# Function to convert Time in H:M:S format in to Seconds
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    print("Time converted in to seconds:", seconds)
    int_to_time(seconds)
    return(seconds)


# Function to convert Seconds in H:M:S Time format
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    print(time.hour, time.minute, time.second)
    return(time)


time_to_int(time)
