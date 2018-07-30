a = [1, 1, 3, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = int(input("Type an int: "))
for i in range(0, len(a)):
    if a[i] < c:
        b.append(a[i])
print(b)