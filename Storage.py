import json
import os
import Validation

FILE_PATH = "mindtrack_data.json"

def load_entries():
    """
    Reads and returns all entries from mindtrack_data.json safely.
    Returns an empty list if the file doesn't exist or is corrupted.
    """
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Warning: mindtrack_data.json is missing or corrupted. Initializing empty dataset.")
        return []

def save_entry(entry_dict):
    """
    Validates an entry using Validation.py, appends it to existing data, 
    and persists it to disk in mindtrack_data.json.
    """
    
    is_valid, message = Validation.validate_entry(entry_dict)
    if not is_valid:
        print(f"Validation failed: {message}. Entry not saved.")
        return False

    
    entries = load_entries()

    
    entries.append(entry_dict)
    
    
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(entries, f, indent=4)
        print("Success: Entry saved to mindtrack_data.json!")
        return True
    except OSError as e:
        print(f"File writing error: {e}")
        return False