from random import choice

values = ('a', 'b', 2, 's', 'c', 't', 3, 1, 5, 6, 7, 8, 9, 10, 12)
lottery =choice(values)
list = []
for i in range (1, 5):
    lottery =choice(values)
    list.append(lottery)
    
print(list)
