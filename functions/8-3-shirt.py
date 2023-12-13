def make_shirt(size, textsa):
    """Display info about ordered shirt"""
    print(f"You've chosen size \"{size.title()}\" t-shirt with text \"{textsa}\". ")

make_shirt(size='S', textsa='Networks are fun')

def large_shirts(front, size = 'L'):
    print(f"Shirt size {size}, text = {front}.")

large_shirts('I love Python')

def describe_city(city, country='Bulgaria'):
    print(f"{city} is in the country of {country.title()}.")
    
describe_city('Sofia')