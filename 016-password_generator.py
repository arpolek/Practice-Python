import random

source = "abcdefghijklmnopqrstuvxyz01234567890ABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&*()?"
lenght = random.randint(10, 15)
password = "".join(random.sample(source, lenght))
print(password)