from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username= {}
    username["Name"] = input("what is your name? ")
    username["Age"] = input("what is your Age? ")
    username["Position"] = input("what is your Position? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
    
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        decision = input(f"Hello, are you {username["Name"]}? Say yes to clarify!")
        if decision == "yes":
            username = get_stored_username(path)
            if username:
                print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        
greet_user()