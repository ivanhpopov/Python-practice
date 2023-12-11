person1_info = {'first_name': 'John', 'last_name': 'Black', 'age': 26, 'city': 'Boston'}
person2_info = {'first_name': 'Will', 'last_name': 'Smith', 'age': 24, 'city': 'City1'}
person3_info = {'first_name': 'Kenny', 'last_name': 'Roberts', 'age': 23, 'city': 'City2'}

people = [person1_info, person2_info, person3_info]
for person in people:
    for key, value in person.items():
        print(key, value)
    print('------------')
    


#for key in person_info:
#    print(key, person_info[key])

favorite_numbers = {'james': 1, 'sarah': 2, 'Jorge': 3, 'nick': 4, 'roy': 5}
favorite_numbers['james'] = input("Provide a number for james")
print(favorite_numbers)

glossary = {'list': 'list of items', 'integer': 'number', 'conditional': 'statement to execute by condition', 'loop': 'An action which stops when a condition is met or runs through everything.'}
for gloss in glossary:
    print(f"{gloss}\n\t{glossary[gloss]}")
print("\n")
for key in glossary.keys():
    print(key)