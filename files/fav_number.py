from pathlib import Path
import json

def get_stored_number(path):
    """Get stored number if available."""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def get_new_number(path):
    """Prompt for a new username."""
    number = input("what is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number
    
def guess_number():
    """Guess favorite numer."""
    path = Path('favnumber.json')
    number = get_stored_number(path)
    if number:
        print(f"Your number is {number}!")
    else:
        number = get_new_number(path)
        print(f"We'll remember your number is {number}!")
        
guess_number()