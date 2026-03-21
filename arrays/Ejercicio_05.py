import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 1000))

print(numbers)
numbers.sort()
print(numbers)

