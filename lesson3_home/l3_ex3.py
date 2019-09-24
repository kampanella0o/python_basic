import random

try:
    num = random.randrange(1, 15)

    while True:
        guess = int(input("Try to guess the number! "))
        if guess == num:
            answer = input("Nailed it! Want to play again? (Y/n):")
            num = random.randrange(1, 15)
            if answer == "n":
                break
        elif guess > num:
            print("Smaller!")
        elif guess < num:
            print("Greater!")
except ValueError:
    print("I'm not playing like that!")