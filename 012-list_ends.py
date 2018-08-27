import random


def list_ends(list):
    lenght = len(list)
    new_list = []
    new_list.append(list[0])
    last = list[lenght-1]
    new_list.append(last)
    return new_list


def random_list():
    a = random.randint(5, 10)                   #random lenght of a list
    list = random.sample(range(0, 50), a)       #random list, elements between 0 and 50
    print(list)
    return list


b = random_list()
print(list_ends(b))