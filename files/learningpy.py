from pathlib import Path

path = Path('empty.txt')
contents = path.read_text()
print(contents)

new_contents = contents.replace('Python', 'C')

list=[]

for line in new_contents.splitlines():
    list.append(line)

for item in list:
    print(item)

print('Done!')