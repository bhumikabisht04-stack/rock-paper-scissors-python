"""
WORKFLOW OF PROJECT :
1- Input from user(Rock, Scissors, Paper)
2- Computer randomly selects one of the three options
3- Compare the choices to determine the winner
4- Display the result

Cases:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Wins
Rock - Scissors = Rock Wins

B- Paper
Paper - Rock = Paper Wins
Paper - Paper = Tie
Paper - Scissors = Scissors Wins

C- Scissors
Scissors - Rock = Rock Wins
Scissors - Paper = Scissors Wins
Scissors - Scissors = Tie
"""


import random 

choices = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
computer_choice = random.choice(choices)

print(f"You chose: {user_choice}, Computer chose: {computer_choice}")


if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "Rock":
      if computer_choice == "Paper":
          print("Paper covers Rock! =  Computer wins!")
      else:
            print("Rock smashes Scissors! =  You win!")

elif user_choice == "Paper":
     if computer_choice == "Scissors":
         print("Scissors cuts Paper! =  Computer wins!")
     else:
         print("Paper covers Rock! =  You win!")

elif user_choice == "Scissors":
     if computer_choice == "Rock":
         print("Rock smashes Scissors! =  Computer wins!")
     else:
         print("Scissors cuts Paper! =  You win!")

