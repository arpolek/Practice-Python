import random

x = random.randint(15, 20)
a = random.sample(range(1, 30), x)
y = random.randint(5, 10)
b = random.sample(range(1, 30), y)
c = []
print(a)
print(b)
c = [number for number in a if number in b and number not in c]
print(c)