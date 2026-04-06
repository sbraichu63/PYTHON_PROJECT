import random

emojis = {"r":"🪨","p":"📜","s":"✂️"}
choices = ("r",'p','s')
while True:
    user_choice = input("Rockor Paper or Scissor? (r,p,s) :").lower()
    if user_choice not in choices:
     print("Plz enter the valid option")
    computer_choice = random.choice(choices)

    print(f"The option you chosed is {emojis[user_choice]}")
    print(f"The option choosed by the computer is {emojis[computer_choice]}")

    if user_choice == computer_choice:

     print("you both choosed the same option \n The game is tied.")

    elif((user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p')):
     print("You won")

    else:
     print("You lost")


    play_on = input("do you want to keep playing the game (Y/N):").upper()
    if play_on == 'N':
      print("thankyou for playing my game")
      break



 
