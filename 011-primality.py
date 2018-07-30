def check(a):
    b = True
    for i in range(2, a):
        if a%i == 0:
            b = False
            break
    return b

x = int(input("Type an int: "))
prime = check(x)
print("Is number prime? ", prime)