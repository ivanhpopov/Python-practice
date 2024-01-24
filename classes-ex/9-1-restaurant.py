class Restaurant:
    def __init__(self, name, type):
        """Initialize name and cuisine type"""
        self.name = name
        self.type = type
        
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The restaurant is called {self.name}.")
        print(f"The type of cuisine is {self.type}.")
    
    def open_restaurant(self):
        """Restaurant Open message"""
        print(f"\n{self.name} is open!")
        
        
cactus = Restaurant("Cactus", 'Bulgarian')
cactus.describe_restaurant()
cactus.open_restaurant()
