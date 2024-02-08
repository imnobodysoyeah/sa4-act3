number = 10
num_guesses = 9

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while num_guesses != 0:
    if guess == 'q':
        print(f"The number was {number}.")
        break

    guess = int(guess)
   
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        num_guesses -= 1
        if guess > number:
            guess = input(f"Sorry! You guessed too high. You have {num_guesses} guesses left. Try again. What number am I thinking of? ")
        else:
            guess = input(f"Sorry! You guessed too low. You have {num_guesses} guesses left. Try again. What number am I thinking of? ")
        if num_guesses == 1:
            print(f"Sorry! You have no more guesses left. The number was {number}.")
            break
   
        
