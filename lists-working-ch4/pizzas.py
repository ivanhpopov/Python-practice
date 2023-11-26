pizzas = ['margherita', 'barbequelogia', 'burgerza']
friend_pizzas=pizzas[:]
pizzas.append('wolfza')
friend_pizzas.append('Quatro')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())