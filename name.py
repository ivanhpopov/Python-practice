name = "edno dve"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "first"
last_name = "last"
full_name = f"{first_name} {last_name}"
print(full_name)

greeting = f"Hello {first_name}, I believe your last name was {last_name}."
print(greeting)

message = f"Hello, {full_name.title()}!"
print(message)
print("first line \nSecond line \nThird line")

white = " space "
#nowhite = white.rstrip()
#nowhite = nowhite.lstrip()
nowhite = white.strip()

print(nowhite)

#removing prefixes

random_link = 'https://random.link.bro'
random_link = random_link.removeprefix('https://')
print(random_link)


#escape characters
escape = "One of python\'s strengths is it\'s simplicity."
print(escape)