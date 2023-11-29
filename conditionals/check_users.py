current_users = ['george', 'stanley', 'jose', 'admin', 'roshi']

lower_users=[]
for user in current_users:
    user=user.lower
    lower_users.append(user)
    
new_users = ['george', 'user1', 'user2', 'user3', 'jose']

for new_user in new_users:
    if new_user.lower in lower_users:
        print(f"User {new_user} exists!")
    else:
        print(f"Username {new_user} is available!")
        