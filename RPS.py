'''Create a program that recreates Rock, Paper, Scissors'''
def rps():

    player1 = raw_input("Player 1: rock, paper, or scissors?").lower()
    player2 = raw_input("Player 2: rock, paper, or scissors?") .lower()
    
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!! " + player1 + " beats " + player2)
        elif player2 == "paper":
            print("Player 2 wins!! " + player2 + " beats " + player1)
        elif player2 == "rock":
            print("No one wins")
        else:
            print("Player 2: Please enter 'rock', 'paper', or 'scissors'")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!! " + player1 + " beats " + player2)
        elif player2 == "scissors":
            print("Player 2 wins!! " + player2 + " beats " + player1)
        elif player2 == "paper":
            print("No one wins")
        else:
            print("Player 2: Please enter 'rock', 'paper', or 'scissors'")

    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!! " + player1 + " beats " + player2)
        elif player2 == "rock":
            print("Player 1 wins!! " + player2 + " beats " + player1)
        elif  player2 == "scissors":
            print("No one wins")
        else:
            print("Player 2: Please enter 'rock', 'paper', or 'scissors'")

    else:
        print("Player 1: Please enter 'rock', 'paper', or 'scissors'")
