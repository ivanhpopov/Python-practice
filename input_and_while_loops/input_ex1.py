car = input("What car you need?")
print(f"Let me see if I can find a {car} for you.")

people = input("how many people are you?")
people = int(people)
if people > 8:
    print("You'll have to wait for a table.")
else:
    print("We have room for you.")
    
num = input("Give me a number.")
num = int(num)
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")