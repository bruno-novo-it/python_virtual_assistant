# A python program for checking local time in cities.
from datetime import datetime

class TimeService(object):

    def __init__(self):
        pass

    def get_local_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        output = "Your current local time is " + current_time
        return output
