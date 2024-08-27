def ask_users_choice():
    while True:
        choice = input("Enter your pick (Rock/Paper/Scissor): ")
        choice = choice.upper()
        if choice == "ROCK" or choice == "SCISSOR" or choice =="PAPER":
            break
        else:
            print("Invalid Input, Try again")
            continue
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
    import time
    import os
    u = input("This is rock paper scissor game, can you beat the machine?? \n \r Type Y to Continue, N to Forfeit ")
    if u == "Y" or u == "y":
        while True:
            os.system('cls')
            print("**********WELCOME TO ROCK PAPER SCISSORS GAME**********\n")
            print("-----5 Game in a row, most win wins-----\n\n")  
            c=0
            h=0

            for i in range(5):
                x = ask_users_choice()
                y = computers_choice()
                z = result(x,y)
                if z == "COMPUTER WINS":
                    c+=1
                    print("COMPUTER WINS", end='', flush=True)
                    time.sleep(2)
                    print("\r" + " " * len("COMPUTER WINS") + "\r", end='', flush=True)

                elif  z == "HUMAN WINS":
                    h+=1
                    print("HUMAN WINS", end='', flush=True)
                    time.sleep(2)
                    print("\r" + " " * len("HUMAN WINS") + "\r", end='', flush=True)

                else:
                    print("DRAW", end='', flush=True)
                    time.sleep(2)
                    print("\r" + " " * len("DRAW") + "\r", end='', flush=True)
                    continue
            if c<h:
                print("\n\n------------------------------------------------------------------------------")
                print(f"\nYour Score is {h} and Machine Score is {c}")
                print("\nYOU WON THE MACHINE")
                print("\n------------------------------------------------------------------------------")
            elif c>h:
                print("\n\n------------------------------------------------------------------------------")
                print(f"\nYour Score is {h} and Machine Score is {c}")
                print("\nTHE MACHINE WON")
                print("\n------------------------------------------------------------------------------")
            else:
                print("\n\n------------------------------------------------------------------------------")
                print(f"\nYour Score is {h} and Machine Score is {c}")
                print("\nDRAW")
                print("\n------------------------------------------------------------------------------")
            con = input("\n\n DO YOU WANT TO CONTINUE (Y/N)")
            con = con.upper()
            if con == "Y":
                continue
            else:
                print("***THANK YOU, HOPE YOU ENJOYED THE GAME***")
                time.sleep(3)
                break
    else:
        print("TIMID MAN")
main()
