class Restaurant:
    def __init__(self, name, type):
        """Initialize name and cuisine type"""
        self.name = name
        self.type = type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The restaurant is called {self.name}.")
        print(f"The type of cuisine is {self.type}.")
    
    def open_restaurant(self):
        """Restaurant Open message"""
        print(f"\n{self.name} is open!")
    
    def read_served(self):
        print(f"{self.name} has served {self.number_served} customers.")
        
    def set_number_served(self, cust_served):
        self.number_served = cust_served
        
    def increment_number_served(self, increment):
        self.number_served += increment
    
        
cactus = Restaurant("Cactus", 'Bulgarian')
cactus.describe_restaurant()
cactus.open_restaurant()
cactus.read_served()
cactus.set_number_served(4)
cactus.read_served()
cactus.increment_number_served(5)
cactus.read_served()