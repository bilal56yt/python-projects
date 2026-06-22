import random

def number_guess():
    print("=" * 40)
    print("  🎮 Number Guessing Game")
    print("=" * 40)
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!\n")
            continue
        
        attempts += 1
        
        if guess == number:
            print(f"\n🎉 Correct! You got it in {attempts} attempts!")
            break
        elif guess < number:
            print("📈 Too low! Try higher.\n")
        else:
            print("📉 Too high! Try lower.\n")
    else:
        print(f"\n😢 Game over! The number was {number}.")
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        number_guess()
    else:
        print("Thanks for playing! 👋")

if __name__ == "__main__":
    number_guess()
