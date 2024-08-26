def ask_users_choice():
    choice = input("Enter your pick (Rock/Paper/Scissor): ")
    return choice
    
def computers_choice():
    import random
    choices = ["rock","paper","scissor"]
    final = random.choice(choices)
    return (final)

def result(x,y):
    x=x.upper()
    y=y.upper()
    if x == y:
        return "Draw"
    elif (x == "ROCK" and y == "PAPER") or (x == "PAPER" and y == "SCISSOR") or (x == "SCISSOR" and y == "ROCK"):
        return "COMPUTER WINS"
    else:
        return "HUMAN WINS"
    
def main():
    x = ask_users_choice()
    y = computers_choice()
    z = result(x,y)
    print(f"Your choice is {x} and the machine's choice is {y}, thus {z}")

if __name__ == "__main__":
    main()
