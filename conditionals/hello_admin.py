users = ['george', 'stanley', 'jose', 'admin', 'roshi']

for user in users:
    if user == 'admin':
        print(f"Hello {user}, you have higher privileges!")
    else:
        print(f"Hello {user}, you've logged in successfully.")
    
users = []
if users:
    for user in users:
        print(user)
else:
    print("\nWe need to find some users!")