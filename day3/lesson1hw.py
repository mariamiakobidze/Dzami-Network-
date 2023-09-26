import random

my_number = random.randint(1, 100)
attempts = 0
maxsimumi_attempts = 5

print("Welcome to Maro's Game!")
print("I'm thinking of a number between 1 and 100.")

while attempts < maxsimumi_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < my_number:
        print("TOO DABALI!")
    elif guess > my_number:
        print("TOO MAGALI!")
    else:
        print(f"Congratulations, You guessed the number {my_number} in {attempts} attempts.")
        
else:
    print(f"Sorry, you've reached the maximum number of attempts, The secret number was {my_number}.")
    

    

