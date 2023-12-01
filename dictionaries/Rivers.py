rivers = {'Nile': 'egypt', 'Amazon': 'iquitos', 'Yangtze': 'Qinghai'}
for river, city in rivers.items():
    print(f"{river.title()} passes through {city.title()}.")

print('\n')

for river in rivers.keys():
    print(river.title())

print('\n')

for city in rivers.values():
    print(city.title())