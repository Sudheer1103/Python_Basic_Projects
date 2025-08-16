import random
import string

def generate_password(length, use_digits, use_symbols, use_uppercase, use_lowercase):
    """Generate a password based on user preferences with rules enforced."""

    # Build the pool of characters
    char_pools = []
    all_chars = ""

    if use_lowercase:
        char_pools.append(string.ascii_lowercase)
        all_chars += string.ascii_lowercase
    if use_uppercase:
        char_pools.append(string.ascii_uppercase)
        all_chars += string.ascii_uppercase
    if use_digits:
        char_pools.append(string.digits)
        all_chars += string.digits
    if use_symbols:
        char_pools.append(string.punctuation)
        all_chars += string.punctuation

    if not all_chars:  # Safety check
        return "No character types selected! Please choose at least one."

    if length < len(char_pools):
        return f"Password must be at least {len(char_pools)} characters long to include all selected types."

    # Ensure at least one character from each selected pool
    password_chars = [random.choice(pool) for pool in char_pools]

    # Fill the rest randomly from all available characters
    password_chars += [random.choice(all_chars) for _ in range(length - len(char_pools))]

    # Shuffle to avoid predictable order
    random.shuffle(password_chars)

    return "".join(password_chars)


print("🔐 Welcome to the Dynamic Password Generator!")

try:
    # Ask user for preferences
    length = int(input("How long should the password be? "))

    lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    digits = input("Include numbers? (y/n): ").strip().lower() == "y"
    symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    # Generate and show password
    result = generate_password(length, digits, symbols, upper, lower)
    print("\nHere is your generated password:")
    print(result)

except ValueError:
    print("Oops! Please enter a valid number for the length.")
