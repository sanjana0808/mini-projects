import random
# #where to find the list of random numbers?
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Enter a number between 1 and {x}: "))
#         if guess < random_number:
#             print("You have entered a low guess")
#         elif guess > random_number:
#             print("Your guess is too high")
#     print(f"You won! The correct answer is {random_number}")
# guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer has guessed the number, {guess} correctly")
computer_guess(3)