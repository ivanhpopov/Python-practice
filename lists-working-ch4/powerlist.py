squares = [value**2 for value in range(1, 11)]
print(squares)
twenty = list(range(1,21))
print(twenty)
milli = list(range(1, 1001))
for mil in milli:
    print(mil)
print(sum(milli))
print(min(milli))
print(max(milli))

odd = list(range(1,20,2))
print(odd)
threes = [tre*3 for tre in range(3,31) ]
print(threes)
cubes = [cube**3 for cube in range(1,11)]
for cube in cubes:
    print(cube)
print(cubes)

fours =[]
for value in range(1,5):
    value = value ** 4
    fours.append(value)
print(fours)