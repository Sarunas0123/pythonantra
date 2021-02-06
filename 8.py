player1 = input("First player choose rock, paper or scissors\n")
player2 = input("Second player choose rock, paper or scissors\n")

while True:
    if player1.lower() not in ["paper", "rock", "scissors"] or player2.lower() not in ["paper", "rock", "scissors"]:
        print("Wrong input!\n")
    elif player1.lower() == player2.lower():
            print("It's a draw!")
    elif (player1.lower() == "rock" and player2.lower() == "scissors") or (player1.lower() == "scissors" and player2.lower() == "paper") or (player1.lower() == "paper" and player2.lower() == "rock"):
        print("First player wins!")
    elif (player2.lower() == "rock" and player1.lower() == "scissors") or (player2.lower() == "scissors" and player1.lower() == "paper") or (player2.lower() == "paper" and player1.lower() == "rock"):
        print("Second player wins!")

    cont = input("Do you want to continue? y/n\n")
    if cont.lower() == "y":
        player1 = input("First player choose rock, paper or scissors\n")
        player2 = input("Second player choose rock, paper or scissors\n")
        continue
    else:
        break

