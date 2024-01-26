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
    
class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
    def get_flavours(self):
        flavours_list =[]
        x=0
        while x != 'stop':
            x = input("Please provide a few flavours, enter \"stop\" to stop:")
            x=str(x)
            if x !='stop':
                flavours_list.append(x)
            else:
                break
       
        print(f"{flavours_list} flavours are available")
        
cactus = IceCreamStand('Cactus', 'Spanish')
cactus.get_flavours()
        