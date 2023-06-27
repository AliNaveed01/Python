# now we are gonna make a guessing game in which the computer will have the number and we will guess it 
import random

def get_num(x):
    num = random.randint(0, x)
    # this will return the random number between 0 and x
    
    while 1:
        guess = int(input("Guess the number: "))
        if guess == num:
            print("You guessed it right!")
            break
        elif guess > num:
            print("Too high!")
        else:
            print("Too low!")
            
get_num(10)


# Now the guess the number from User side
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "C":
        nu = random.randint(low, x)
        feedback = input(f"Is {nu} too high (H), too low (L), or correct (C)?? ").upper()
        if feedback == "H":
            high = nu - 1
        elif feedback == "L":
            low = nu + 1
            
    print(f"Yay! The computer guessed your number, {nu}, correctly!")
    
computer_guess(10)

    