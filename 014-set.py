def loop_method(l):
    print(l)
    new_list = []
    count = 0
    for item1 in l:
        for item2 in l:
            if item1 == item2:
                count = count + 1
        if count < 2:
            new_list.append(item1)
        count = 0
    return new_list


def set_method(l):
    numbers = set()
    for item in l:
        numbers.add(item)
    return numbers


a = [4, 4, 3, 2, 2, 1]
print(loop_method(a))
print(set_method(a))