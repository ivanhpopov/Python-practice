person_info = {'first_name': 'John', 'last_name': 'Black', 'age': 26, 'city': 'Boston'}

for key in person_info:
    print(key, person_info[key])

favorite_numbers = {'james': 1, 'sarah': 2, 'Jorge': 3, 'nick': 4, 'roy': 5}
favorite_numbers['james'] = input("Provide a number for james")
print(favorite_numbers)

glossary = {'list': 'list of items', 'integer': 'number', 'conditional': 'statement to execute by condition', 'loop': 'An action which stops when a condition is met or runs through everything.'}
for gloss in glossary:
    print(f"{gloss}\n\t{glossary[gloss]}")