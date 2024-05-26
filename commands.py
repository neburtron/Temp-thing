import json
import random

def read(filename):
    # Read contents from a file.
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ''
    
def load(filename):
    # Load contents from a json file.
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
        return None
    
def Roll_Dice(sides):
    X = random.randrange(1, sides)
    return (X)