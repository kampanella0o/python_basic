try:
    import random

    num = random.randrange(1, 15)

    while True:
        guess = int(input("Try to guess the number! "))
        if guess == num:
            answer = input("Nailed it! Want to play again? (Y/n):")
            if answer == "n":
                break
        elif guess > num:
            print("Smaller!")
        elif guess < num:
            print("Greater!")
except ValueError:
    print("I'm not playing like that!")