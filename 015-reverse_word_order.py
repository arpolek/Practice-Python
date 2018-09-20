def reverse(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]
    output = ' '.join(inputwords)
    return output


sentence = input("Please type a multiple word string: ")
print(reverse(sentence))