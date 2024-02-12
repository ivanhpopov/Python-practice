from pathlib import Path

path_cats = Path('cats.txt')
path_dogs = Path('dogs.txt')
try:
    dogs = path_dogs.read_text()
except FileNotFoundError:
    dogs = ("dogs.txt is not found")
try:
    cats = path_cats.read_text()
except FileNotFoundError:
    pass

print(dogs)
try:
    print(cats)
except NameError:
    pass