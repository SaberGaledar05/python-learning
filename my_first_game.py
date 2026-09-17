# Make gmae rock paper scissors

import random

print("rock")
print("paper")
print("scissors")
print("----------------")


Player_1_wins = 0
Player_2_wins = 0
finalScore = 4

while Player_1_wins < finalScore and Player_2_wins < finalScore:
    print(f"player 1 score = {Player_1_wins} | player 2 score = {Player_2_wins}")
    Player_1 = input("player_1 , make your move : ").lower()
    computerMove = random.choice(["rock", "paper", "scissors"])
    Player_2 = computerMove
    print(f"Player_2 , make your move : {computerMove}")
    if Player_1 == "q" or Player_1 == "quit":
        print("game is the finish")
        break
    if Player_1 == Player_2:  # this syntaxes is not different
        print("thats a tie")
    elif Player_1 == "rock":
        if Player_2 == "paper":
            print("player_2 is wins!...")
            Player_2_wins += 1
        elif Player_2 == "scissors":
            print("player_1 is wins!...")
            Player_1_wins += 1
    elif Player_1 == "paper":
        if Player_2 == "rock":
            print("player_1 is wins!...")
            Player_1_wins += 1
        elif Player_2 == "scissors":
            print("player_2 is wins!...")
            Player_2_wins += 1
    elif Player_1 == "scissors":
        if Player_2 == "paper":
            print("player_1 is wins!...")
            Player_1_wins += 1
        elif Player_2 == "rock":
            print("player_2 is wins!...")
            Player_2_wins += 1
    else:
        print("somthing went wrong...")

print(
    f"final score player 1 = {Player_1_wins} | final score player 2 = {Player_2_wins}"
)
if Player_1_wins == finalScore:
    print("player 1 is winner....")
else:
    print("player 2 is winner....")
