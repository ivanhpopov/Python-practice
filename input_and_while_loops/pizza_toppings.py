prompt = "\nWhat pizza toppings would you like?"
prompt += "\n(type quit to exit.)"


toppings =[]
while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"You've added {topping}!")

print(toppings)