import random
#where to find the list of random numbers?
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("You have entered a low guess")
        elif guess > random_number:
            print("Your guess is too high")
    print(f"You won! The correct answer is {random_number}")
guess(10)