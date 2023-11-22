cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars_one = ['bmw', 'audi', 'toyota', 'subaru']

print(f"Here is the original: {cars_one}")
print(f"\nHere is the sorted list: {sorted(cars_one)}")
print(f"\nHere is the original list again: {cars_one}")

cars_one.reverse()
print(cars_one)