import random
user_choice = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    computer_choice = random.randint(0, 2)
    print("computer chose:")
    print(computer_choice)

    if computer_choice == user_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2):
        print("You win!")
    elif (user_choice == 1 and computer_choice == 0):
        print("You win!")
    elif (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
