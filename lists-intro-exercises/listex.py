guests = ['Guest1', 'Guest2', 'Guest3', 'Guest4']

print(f"{guests[0]}, you are invited to dinner")
print(f"{guests[1]}, you are invited to dinner")
print(f"{guests[2]}, you are invited to dinner")

print(guests)

print(f"{guests[3]} is not coming, replacing with Guest5")

guests[3] = "Guest5"

print(guests)

print(f"{guests[0]}, you are invited to dinner")
print(f"{guests[1]}, you are invited to dinner")
print(f"{guests[2]}, you are invited to dinner")
print(f"{guests[3]}, you are invited to dinner")

for i in guests:
    print(i+", we found a bigger table")
    
guests.insert(0, "Guest0")
guests.insert(3, "GuestX")
guests.append('GuestZ')

for i in guests:
    print(i+", You are invited to dinner")
    
print("table lost -2 spots left")

print(guests[0:2])

guests.pop()
print(guests)
guests.pop()
print(guests)

print(len(guests))
x = len(guests)
for i in guests:
    if x > 2:
        guests.pop()
        x-=1
    else:
        break
print(guests)
for i in guests:
    print(f"you're invited {i}")
del guests[0:2]
print(guests)
        
