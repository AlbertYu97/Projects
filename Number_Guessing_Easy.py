logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
# Generate random number between 1 and 100
import random
number = random.randint(1, 100)

# Opening text
print(logo)
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

# Choose diffculty, easy gives a player 10 tries and hard gives 5 tris
diffculty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diffculty == 'easy':
  life = 10
elif diffculty == 'hard':
  life = 5

# Create a function to check guess againest actual answer
def check_guess(guess, number):
  if guess > number:
    print("Too High.")
  elif guess < number:
    print("Too low.")
  else:
    print(f"You got it! The answer was {guess}.")

# Create a while loop to keep looping until life = 0 or the user get the correc answer
while life > 0:
  print(f"You have {life} attempts remaining to guess the number.")
  # Get the guess from the player
  guess = int(input("Make a guess: "))
  check_guess(guess, number)
  if guess != number:
    life -= 1
    if life > 0:
      print("Guess Again")
    else:
      print("You've run out of guesses, you lose.")
  if guess == number:
    life = -1