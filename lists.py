test = ['tes', 'test', 'test3']
print(test[2])
test.append('newtest')
print(test[3].title())
print(test)

message = f"I am conducting a test with name {test[3].title()}"
print(message)

transport = ['car', 'bus', 'foot', 'trolly']

car = f"I like to drive my {transport[0].title()}, but sometimes I prefer travelling by {transport[-2].title()}."
print(car)

transport.insert(0, 'boat')
transport.append('something')
transport[2] = 'pesha'
del transport[3]
print(transport)
popped_transport = transport.pop()
print(popped_transport)
print(f"The item that i popped from the list has a value of \"{popped_transport}\"")
popone = transport.pop(0)
print(f"The value of the first popped item in the list is \"{popone}\"")


# Removing by value

print(transport)
transport.remove('pesha')
print(transport)
