import random
game_list = ["rock","paper","scissors"]
computer = random.choice(game_list)
user_point = 0
computer_point = 0

print("------------------Three points wins----------------------")

while (computer_point != 3 or user_point != 3):

    computer = random.choice(game_list)

    user = input("Choose: Rock/Paper/Scissors ").lower()
    print("---------------------------------------------------------")

    if user not in game_list:
        print("Please enter a Rock/Paper/Scissors: ")

    elif user == computer:
        print("Draw!")
        print(f"Computer choose: {computer}")
        print(f"Computer: {computer_point} - You: {user_point} ")
        print("---------------------------------------------------------")

    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You '+1' point!")
        print(f"Computer choose: {computer}")
        user_point+=1
        print(f"Computer: {computer_point} - You: {user_point} ")
        print("---------------------------------------------------------")

    else:   
        print("Computer '+1' point!")
        print(f"Computer choose: {computer}")
        computer_point+=1
        print(f"Computer: {computer_point} - You: {user_point} ")
        print("---------------------------------------------------------")

    if user_point == 3:
        print("You won!")
        break

    elif computer_point == 3:
        print("Computer won!")
        break


  


