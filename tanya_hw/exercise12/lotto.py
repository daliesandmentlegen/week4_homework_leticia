import random

num = 6
start = 0
end = 50

lotto = random.sample(range(start, end), num)

print(f'Your lucky numbers are: {lotto} \nFingers crossed!')
