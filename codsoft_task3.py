import random

def play():
    uScore = 0
    cScore = 0

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in ["rock", "paper", "scissors"]:
            print("Invalid,try again.")
            continue

        computer = random.choice(["rock", "paper", "scissors"])
        print("Your choice:", user)
        print("Computer's choice:", computer)
        res = winner(user, computer)
        print(res)

        if res == "You win!":
            uScore += 1
        elif res == "Computer wins!":
            cScore += 1

        again = input("Do you want to play again? [yes || no]: ").lower()
        if again != "yes":
            break

    print("Final Scores:")
    print("Your score:", uScore)
    print("Computer score:", cScore)

    
def winner(user, computer):
    if user == computer:
        return "tie!"
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"    

play()