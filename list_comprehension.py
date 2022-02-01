'''List Comprehension'''

'''Creating a list from a string'''

l1 = list('human') #OR
l1 = [letter for letter in 'human']
print(l1)

'''Conditions in forming a list'''

l2 = [number for number in range(200) if number % 2 == 0 if number % 5 == 0]
print(l2)

l3 = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)]
print(l3)