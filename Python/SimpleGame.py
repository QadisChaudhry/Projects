import random


def main():
    number = random.randint(1, 10)
    tries = 1

    username = input("Hello, what is your name? ")

    while username == "":
        username = input("Please tell me your name :( ")
    if username == "no":
        print("oh..okay...")
    else:
        print("Hello " + username + "!")

    question = input("Would you like to play a game? [y/n] ")
    question = question.lower()

    if question == "n":
        confirmation = input("Are you sure? [y/n] ")
        if confirmation == "y" or confirmation == "Y" or confirmation == "yes":
            print("oh..okay.")
            exit(0)
        else:
            while confirmation == "n":
                question = input("Would you like to play a game? [y/n] ")
                if question == "n":
                    print("Alright then, don't play :'(")
                    exit(0)
                else:
                    print("Yay! I'm thinking of a number between 1 & 10... ")
                    restart()
    elif question == "y":
        print("Yay! I'm thinking of a number between 1 & 10... ")

    while question != "n":
        while question != "y":
            question = input("You have to enter [y/n]... ")
            question = question.lower()
            if question == "n":
                confirmation = input("Are you sure? [y/n] ")
                if confirmation == "y" or confirmation == "Y" or confirmation == "yes":
                    print("oh..okay.")
                    exit(0)
                else:
                    while confirmation == "n":
                        question = input("Would you like to play a game? [y/n] ")
                        if question == "n":
                            print("Alright then")
                            exit(0)
                        else:
                            print("Yay! I'm thinking of a number between 1 & 10... ")
                            restart()
            elif question == "y":
                print("Yay! I'm thinking of a number between 1 & 10... ")

        try:
            guess = float(input("Take a Guess... "))
        except ValueError:
            guess = float(input("Enter a Number... "))
            pass
        if guess > number:
            tries += 1
            guess = float(input("Guess a little lower... "))
        elif guess < number:
            tries += 1
            guess = float(input("Guess a little higher... "))
        while guess != number:
            tries += 1
            guess = float(input("Try again "))
        if guess == number:
            print("You did it! A winner is you!! The number was", number, "and it only took you", tries)
            if tries == 1:
                print("try!")
            else:
                print("tries!")
            play_again()


def restart():
    number = random.randint(1, 10)
    tries = 1

    try:
        guess = float(input("Take a Guess... "))
    except ValueError:
        guess = float(input("Enter a Number... "))
        pass
    if guess > number:
        tries += 1
        guess = float(input("Guess a little lower... "))
    elif guess < number:
        tries += 1
        guess = float(input("Guess a little higher... "))
    while guess != number:
        tries += 1
        guess = float(input("Try again "))
    if guess == number:
        print("You did it! A winner is you!! The number was", number, "and it only took you", tries)
        if tries == 1:
            print("try!")
        else:
            print("tries!")
        play_again()


def play_again():
    reset = input("Would you like to play again? [y/n] ")
    reset = reset.lower()
    if reset == "y":
        restart()
    elif reset == "n":
        print("Okay!")
        exit(0)
    while reset != "n":
        while reset != "y":
            reset = input("Please enter [y/n]... ")
            reset = reset.lower()
            if reset == "y":
                restart()
            elif reset == "n":
                print("Okay!")
                exit(0)


main()
