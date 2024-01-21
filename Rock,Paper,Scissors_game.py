import pyautogui
import secrets
print("::::::Rock,Paper,Scissors game::::::")
base_game = ["rock", "paper", "scissors"]
user_input = str(input("Enter your choice:(rock, paper, or scissors)\n>> ")).strip().lower()
computer_choice = secrets.choice(base_game)

if user_input in base_game:
    while range(5):
        if user_input == computer_choice:
            print("")
        elif user_input == "rock" and computer_choice == "scissors":
            print("You won...")
        elif user_input == "scissors" and computer_choice == "paper":
            print("You won...")
        elif user_input == "paper" and computer_choice == "rock":
            print("You won...")
        else:
            print("I won... :)")
        print(f"My choice is:{computer_choice}")
        break
else:
    print("Your choice must be rock,paper or scissors!!!")