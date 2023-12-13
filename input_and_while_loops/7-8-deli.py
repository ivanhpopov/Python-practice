sandwich_orders = ['tomatoe', 'pastrami', 'pastrami', 'pastrami', 'chicken', 'vegan', 'steak']
finised_sandwiches = []

print("We've run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    
    sandwich = sandwich_orders.pop()
    print(f"Making a {sandwich} sandwich.")
    finised_sandwiches.append(sandwich)

print("\nThe following sandwiches are done!\n")
for sandwiche in finised_sandwiches:
    print(f"{sandwiche}")