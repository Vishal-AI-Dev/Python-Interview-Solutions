import random

def guess_the_number(): # Function to implement Guess the Number Game
    target_number = random.randint(1, 100)
    print(f"I have guessed a number. Try to find it.")
    attempts = 0  # To count number of attempts also declared outside the loop

    while True: #creating infinite loop until user finds the number
        try:
            user_number = int(input("Guess Your Number : "))
            attempts += 1

            if user_number < target_number:
                print("Too low !, Guess another Number  ")

            elif user_number > target_number:
                print("Too high ! , Guess another Number ")

            else:
                print(f"Congrats You won. You found the Number with {attempts} attempts") #formatted string to show attempts
                break
            
        except ValueError:
            print("Please enter a integer to play the game")

if __name__ == "__main__":
  guess_the_number()
    
