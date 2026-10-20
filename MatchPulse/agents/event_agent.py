import json

def load_events(filepath):

    with open(filepath, "r") as file:
        events = json.load(file)

    return events