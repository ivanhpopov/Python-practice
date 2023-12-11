pet1 = {'name': 'Ty1', 'type': 'dog', 'color': 'red', 'owner': 'owner1'}
pet2 = {'name': 'Ty2', 'type': 'cat', 'color': 'orange', 'owner': 'owner2'}
pet3 = {'name': 'Ty3', 'type': 'parrot', 'color': 'yellow', 'owner': 'owner3'}

pets = [pet1, pet2, pet3]
for pet in pets:
    for key, value in pet.items():
        print(key, value)
    print('---------')
