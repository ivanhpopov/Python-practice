favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

for name in favorite_languages.keys():
    print(name.title())

print("\n")

for language in favorite_languages.values():
    print(language.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
#    favorite_languages['erin'] = input('What is your fav language')
#    print(favorite_languages['erin'])

print("\n")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")

poll_take = ['phil', 'sarah', 'john']
for name in poll_take:
    print(f"Checking if you've taken the poll {name.title()}...")
    if name in favorite_languages.keys():
        print(f"{name.title()}, you're all good. Thanks for taking the time!")
    else:
        print(f"{name.title()}, you have not taken the poll. Please do it at your earliest convenience!")