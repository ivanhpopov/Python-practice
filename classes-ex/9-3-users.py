class User:
    def __init__(self, first_name, last_name, department, title):
        """Initialize the first set of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.title = title
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Users name is {self.first_name} {self.last_name}.")
        print(f"User is in {self.department} department.")
        print(f"Users title is {self.title}.")
        
    def greet_user(self):
        print(f"Greetings {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
user_one = User('George', 'Leeman', 'IT', 'Manager')
user_one.describe_user()
user_one.greet_user()
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempts)