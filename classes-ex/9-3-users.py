class User:
    def __init__(self, first_name, last_name, department, title):
        """Initialize the first set of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.title = title
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Users\' name is {self.first_name} {self.last_name}.")
        print(f"User is in {self.department} department.")
        print(f"Users\' title is {self.title}.")
        
    def greet_user(self):
        print(f"Greetings {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1


class Privileges():
    def __init__(self, admin_privileges=1):
        self.admin_privileges = admin_privileges
        
    def escalate_privileges(self):
        self.admin_privileges = 1
        
    def de_escalate_privileges(self):
        self.admin_privileges = 0
        
    def get_privileges(self):
        
        if self.admin_privileges == 1:
            
            message = ['can add post', 'can delete post', 'can ban user']
        
        else:
            
            message = ['can\'t add post', 'can\'t delete post', 'can\'t ban user']
            
        print(message)

class Admin(User):
    def __init__(self, first_name, last_name, department, title):
        super().__init__(first_name, last_name, department, title)
        self.privileges = Privileges()
        
user_one = Admin('George', 'Leeman','\"IT\"', 'Manager')
user_one.privileges.get_privileges()
user_one.privileges.de_escalate_privileges()
user_one.privileges.get_privileges()