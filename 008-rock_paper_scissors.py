decision = True

rock = "rock"
paper = "paper"
scissors = "scissors"

while (decision == True):
    a = input("1st player plays (rock/paper/scissors): ")
    b = input("2nd player plays (rock/paper/scissors): ")
    if a == rock and b == paper:
        print("Paper wins!")
    elif a == rock and b == scissors:
        print("Rock wins!")
    elif a == paper and b == scissors:
        print("Scissors wins!")
    elif a == paper and b == rock:
        print("Paper wins!")
    elif a == scissors and b == paper:
        print("Scissors wins!")
    elif a == scissors and b == rock:
        print("Rock wins!")
    elif a == b:
        print("It's a draw!")

    d = input("Do you wanna play again? (yes/no): ")
    if d == "yes":
        decision == True
    else:
        decision == False