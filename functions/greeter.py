def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
    
greet_user('jesse')

def display_message(name, language, chapter):
    print(f"Hello, I'm {name.title()} and I'm learning {language.title()}. So far I've reached {chapter.title()}, it's really fun!")
    
display_message('Ivan', 'Python', 'Functions')

def favorite_book(title):
    print(f"My favorite book is {title.title()}!")
    
favorite_book('Pirates of the Carribean')