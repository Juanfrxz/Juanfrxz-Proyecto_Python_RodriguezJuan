import json

def load_json(filename, default_value):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return default_value

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
