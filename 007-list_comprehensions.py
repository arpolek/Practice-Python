a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# regular loop
b = []
for i in a:
    b.append(1+i)
print(b)

# list comprehension
c = [j+10 for j in a]
print(c)

# check if even
f = []
for l in a:
    if l%2 == 0:
        f.append(l)
print(f)

# list comprehension, even numbers
e = [number for number in a if number % 2 == 0]
print(e)