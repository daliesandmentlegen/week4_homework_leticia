# Question 1 - Add Oke to the cheese list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

cheese += ['Oke']

# new additions to a list must have [ ] to be added properly
print(cheese)

cheese.append('Mozzarella')
print(cheese)

# Question 2
tup = 'Hello'
print(len(tup))
print(type(tup))
# python reads 'Hello' as str BC of ''
# len func. will count number of char in str
# so printing tup will lead to 5

tup2 = 'Hello',
print(len(tup2))
print(type(tup2))
# no brackets and lack of commas makes tup2 a tuple
# len func. will count the number of items in a tuple instead of char
# so printing tup2 will lead to 1