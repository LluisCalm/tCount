class Event:

    def __init__(self, name,hours):
        self.hours = hours
        self.name = name
    
    def update_hours(self, hours_added):
        self.hours += hours_added

    def get_hours(self):
        return self.hours
    
    def get_name(self):
        return self.name
    
    def to_string(self):
        return self.name+": "+str(round(self.hours,2))