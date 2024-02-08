number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while True:
    if guess == 'q':
        print(f"The number was {number}.")
        break

    guess = int(guess)
   
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input(f"Sorry! Try again. What number am I thinking of? ")
