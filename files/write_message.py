from pathlib import Path

path = Path('programming.txt')

contents = "I love programming.\n"
contents += "I love hacking!\n"
contents += "I love reading code.\n"

path.write_text(contents)

text = path.read_text()
print(text)