a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
duplicate = False

for i in range (0, a.__len__()):
   for j in range (0, b.__len__()):
        if a[i] == b[j]:
            for k in range (0, c.__len__()):
                if a[i] == c[k]:
                    duplicate = True
            if duplicate == False:
                c.append(a[i])
            duplicate = False
print(c)