prompt = "\nWhat age are you?"
prompt += "\n(Type 'quit' to quit.)"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket's free!")
        elif age >= 3 and age <= 12:
            print("Your ticket is $10")
        elif age > 12:
            print("Your ticket is $15!")
        else:
            break