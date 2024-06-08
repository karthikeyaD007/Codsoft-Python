import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a pool of characters based on complexity level
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate the password by randomly choosing characters from the pool
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))

            if length <= 0:
                print("Please enter a valid positive integer length.")
                continue

            password = generate_password(length)
            print("Generated Password:", password)
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer length.")

if __name__ == "__main__":
    main()
