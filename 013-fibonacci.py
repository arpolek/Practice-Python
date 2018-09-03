def fib(k):
    a = 1
    b = 1
    print(a)
    print(b)
    while k > 2:
        c = a+b
        print(c)
        a = b
        b = c
        k = k-1


number = int(input("How long the Finonacci code? "))
fib(number)