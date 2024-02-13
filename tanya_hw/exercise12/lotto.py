# imports random module
import random

num = 6
start = 0
end = 50

lotto = random.sample(range(start, end), num)
# imports sample func from random module
# .sample picks a random selection of values within specified range then produces them as a list
# syntax is random.sample(range([start value], [end value]), [desired selection])

print(f'Your lucky numbers are: {lotto} \nFingers crossed!')


# help function returns information on the different functions in the random module from the Python file sources
# help function provides information about modules, classes, functions and modules.
# help(range)

# TODO: write a program that generate and display 6 unique random lottery numbers between 1 - 50

# created variable and assigned it to an empty list
# chose list as it is mutable to print a new set of 6 unique random lottery numbers
lottery_list = []

# range function returns a sequence of integers starting from 0 and increments by 1 (default)
# range: stops at a specified num
# for loop iterates over a sequence of integers 6 times from 0 and does not include six
for num in range(6):
    # append method adds a random integer as an element to the end of the empty lottery_list
    # randrange function from module creates a sequence which starts at 1 - 50 and picks random numbers
    lottery_list.append(random.randrange(1, 51))

    # ALTERNATIVES:
    # randint(start, end) function generates a random integer between 1 - 50
    # lottery_list.append(random.randint(1, 51))
    # extend: adds the specifies list elements to the end of the list
    # lottery_list.extend([random.randint(1, 51)])

# print function passes the new list after six iteration of for loop as an argument
print(lottery_list)




