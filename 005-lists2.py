import random

x = random.sample(range(1, 30), 10)
y = random.sample(range(1, 30), 10)
z = []

for i in x:
   if i in y:
        if i not in z:
            z.append(i)
print(z)
