from random import randint

random_number = randint(1, 10)

while True:
    guess = int(input("Enter a guess between 1 and 10. "))

    if guess > random_number:
        print("Too high!, Try again.")
    elif guess < random_number:
        print("Too low!, Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break
