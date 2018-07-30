word = input("Type a word: ")
b = word[::-1]
if word == b:
    print("Word is palindrome!")
else:
    print("Word is not palindrome")