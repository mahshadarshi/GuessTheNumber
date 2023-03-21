import random 
import time 
import winsound 

random_num = random.randint(1, 100) # generate a random number between 1 and 100

number_of_guesses = 0 # keep track of the number of guesses the user has made

start_time = time.time() # get the current time

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you the number?")

while True:
    user_guess = input("Please guess a number between 1 - 100 or type 'quit' to exit: ") # ask the user to guess a number
    
    if user_guess.lower() == 'quit': # check if the user wants to quit
        print(f"Exiting the game... (The random number was {random_num})")
        break
        
    try: # check if the user entered a valid number
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input! Please enter a valid number or type 'quit' to exit.")
        continue
    
    number_of_guesses += 1
    
    if user_guess == random_num: # check if the user guessed the correct number
        end_time = time.time()
        time_taken = round(end_time - start_time, 2) # calculate the time taken to guess the number
        print(f"Well done, you guessed the number in {number_of_guesses} guesses in {time_taken} seconds!") # print a message if the user guessed the correct number
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)  # play a sound effect
        break
    
    elif user_guess > random_num: # check if the user guessed too high
        print("Your guess was too high!")
    
    else: # check if the user guessed too low
        print("Your guess was too low!")