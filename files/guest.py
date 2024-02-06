from pathlib import Path

path = Path('guest.txt')
contents =''
x = ''

x = input("Please provide your name.")
x += '\n'
contents += x

path.write_text(contents)

text = path.read_text()
print(text)