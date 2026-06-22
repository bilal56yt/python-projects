import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True, use_upper=True):
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 45)
    print("  🔐 Password Generator — Muhammad Bilal")
    print("=" * 45)
    
    try:
        length = int(input("Password length (default 12): ") or 12)
        symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
        numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        upper = input("Include uppercase? (y/n, default y): ").lower() != 'n'
        count = int(input("How many passwords to generate? (default 5): ") or 5)
    except ValueError:
        print("Invalid input, using defaults.")
        length, symbols, numbers, upper, count = 12, True, True, True, 5
    
    print(f"\n✅ Generated {count} password(s):\n")
    for i in range(count):
        pwd = generate_password(length, symbols, numbers, upper)
        print(f"  {i+1}. {pwd}")
    
    print("\nTip: Use a password manager to store these safely! 🛡️")

if __name__ == "__main__":
    main()
