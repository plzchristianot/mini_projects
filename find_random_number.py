import random

print("Hi! Welcome to this game where you will need to find the correct number")

number_to_find = random.randrange(50)
max_attempts = 5
counter = 0

while counter <=5:
    my_guess = int(input("Dame un número: "))
    counter += 1

    if my_guess == number_to_find:
        print(f"Congrats! You have found the correct number {my_guess} at the attempt {counter}")
        break
    
    elif my_guess < number_to_find:
        print(f"Sorry bro, your number {my_guess} is lesser")
    
    elif my_guess > number_to_find:
        print(f"Sorry bro, your number {my_guess} is higher")
    
    elif counter == max_attempts and my_guess != number_to_find:
        print(f"Sorry, you haven't been able to find the correct number {number_to_find}, better luck next time")
    
