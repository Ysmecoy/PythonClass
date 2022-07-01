class Duration:
    #constructor
    """Output the duration time
    """
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        
    def __str__(self):
        minute_string = str(self.minutes)
        if self.minutes < 10:
            minute_string = '0{}'.format(minute_string)
        return '{}:{}'. format(self.hours, minute_string)
    
half_day = Duration (12,0)
print(half_day)


class Duration1:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes)
tuesday_time = Duration1(6,30)
monday_time = Duration1(9, 45)
workday = Duration1(9,45)

print(tuesday_time == workday)
print(monday_time == workday)

        