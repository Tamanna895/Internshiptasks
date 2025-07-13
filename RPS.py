import random
ROCK= "👊"
PAPER="✋"
SCISSORS="✌️"
game_art=[ROCK,PAPER,SCISSORS]
user_choice=int(input(" Enter 0 for ROCK\n Enter 1 for PAPER\n Enter 2 for SCISSORS:"))
if user_choice >=3 or user_choice < 0:
    print("invalid choice .....you lose :(")
else:
    print(game_art[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(game_art[computer_choice])
    if computer_choice==user_choice:
        print("It's a DRAW ;)")
    elif computer_choice==0 and user_choice==2:
        print("You LOSE :(")
    elif computer_choice==2 and user_choice==0:
        print("You WIN")
    elif computer_choice > user_choice:
        print("You LOSE 4 :(")
    elif user_choice > computer_choice:
        print("You WIN :)")
    
