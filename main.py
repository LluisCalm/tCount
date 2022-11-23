# IMPORTS
from Event import Event
from datetime import datetime
import os
import time
import json

####################
#    FUNCTIONS
####################

def correct_event(to_check):
    for x in events:
        if x.get_name() == to_check:
            return True
    return False

# Converts the event object to JSON structure
def get_json(x):
    return {'name' : x.get_name(), 'hours' : x.get_hours()}

# Search the events.json or creates it 
def verify_json():
    if os.path.isfile('events.json'):
        return
    
    events = {}
    events['events'] = []
    with open("events.json","w") as f:
        json.dump(events,f)

# Checks if the event's name we're creating exists or not
def name_exist(name):
    for x in events:
        if x.getName() == name:
            return True

# It creates and appends a new event
def create_event():

    name = input("What's the name's event? ")
    while name_exist(name):
        name = input("Select a corret value ")
    
    events.append(Event(name,0))

# From events.json we obtains an array with all the events
def obtain_events():
    ev_array = []
    with open('events.json') as x:
        data = json.load(x)['events']

    for x in data:
        ev_array.append(Event(x['name'],x['hours']))

    return ev_array

def update_time(ev, time):
    for x in events:
        if x.get_name() == ev:
            x.update_hours(time/3600)

# Counts the time
def start_event():
    print("Events to select:")
    for x in events:
        print(x.get_name())

    ev_selected = input("Select any of these events: ")

    while not correct_event(ev_selected):
        ev_selected = input("Select any of these events: ")

    init_time = time.time()
    now = datetime.now()
    minutes = ""
    if len(str(now.minute))<2:
        minutes = "0"+str(now.minute)
    else:
        minutes = str(now.minute)
    
    entered = input("Start counting time at "+str(now.hour)+":"+minutes+", to stop press enter")
    print("Time spent = ",round((time.time()-init_time)/60,2),"minutes")
    update_time(ev_selected,time.time()-init_time)
    
# Save all the events in the event.json file
def save_events():
    to_save = {}
    to_save['events']=[]
    for x in events:
        to_save['events'].append(get_json(x))

    with open("events.json","w") as f:
        json.dump(to_save, f)


def show_statistics():
    print("------------------------------")
    for x in events:
        print(x.to_string())
    print("------------------------------")

####################
#       MAIN
####################

verify_json() 

events = obtain_events()

print("1. Add")
print("2. Count")
print("3. Statistics")
print("4. Exit")

try:
    selected = int(input("Select an option (1,2,3,4): "))
    while selected < 1 or selected > 4:
        selected =  int(input("Select a correct value (1, 2, 3 or 4): "))
except Exception:
    print("Invalid input, next time write a number")
    exit()

if selected == 1:
    create_event()
    save_events()
elif selected == 2:
    if len(events) == 0:
        print("There's no events")
        exit()
    start_event()
    save_events()
elif selected ==3:
    if len(events) == 0:
        print("There's no events")
        exit()
    show_statistics()
