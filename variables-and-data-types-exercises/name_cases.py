first = input("What's your fist name?")
second = input("what's your last name?")
full_name = f"{first} {second}"
greeting = f"Hello, {first}! Your last name is {second}. How you doin?"
print(greeting)

print(full_name.upper())
print (full_name.lower())
print (full_name.title())

name1 = "Albert"
name2 = "Einstein"
name3 = f"{name1} {name2}"

quote = f"{name1} {name2} once said, \"A person who never made a mistake never tried anything new.\""
print(quote)

quote = f"{name3} once said, \"A person who never made a mistake never tried anything new.\""
print(quote)

name4 = "   Three spaces   \n  two spaces  \ttab\nnewlinenospaces"
print(name4.rstrip())
print(name4.lstrip())
print(name4.strip())

file_name = "file.py"
print(file_name.removesuffix(".py"))