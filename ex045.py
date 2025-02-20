from random import choice
from time import sleep

print("-*-" * 25)
print("""Let`s play Jokepo! We must choose one of these: scissor, paper or rock.
scissor beat paper, paper beat rock and rock beat scissor.""")
print("-*-" * 25)
print("I will choose my")
print("\033[1;35mChoosing..\033[m")
sleep(4)
computerChoice = choice(["rock", "scissor", "paper"])
playerChoice = str(input("What was your choice? ")).strip().lower()

if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissor":
    print("-*-" * 15)
    print("\033[1;31mInvalid Option, try again!\033[m")
    print("-*-" * 15)
else:
    print("-*-" * 15)
    sleep(1)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!")

    if playerChoice.lower() == "scissor" and computerChoice == "paper":
        print("\033[1;32mYou win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "scissor" and computerChoice == "rock":
        print("\033[1;31mI win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "scissor" and computerChoice == "scissor":
        print("\033[1;33mIt`s a draw\033[m")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "paper" and computerChoice == "rock":
        print("\033[1;32mYou win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "paper" and computerChoice == "scissor":
        print("\033[1;31mI win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "paper" and computerChoice == "paper":
        print("\033[1;33mIt`s a draw\033[m")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "rock" and computerChoice == "rock":
        print("\033[1;33mIt`s a draw\033[m")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "rock" and computerChoice == "scissor":
        print("\033[1;32mYou win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))
    elif playerChoice.lower() == "rock" and computerChoice == "paper":
        print("\033[1;31mI win\033[m!")
        print("I choice {} and you {}".format(computerChoice, playerChoice))

