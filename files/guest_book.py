from pathlib import Path

path = Path('guest_book.txt')
contents = ''
x = ''

while x != "Stop":

    x = input("Please provide your name.")
    x += '\n'

    if x.strip() == "Stop":
        break

    else:
        contents += x
    
path.write_text(contents)

text = path.read_text()

print(text)