import random
import string
def gen_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase  # Always include lowercase letters
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    if length < 1:
        return "Password length must be greater than 0."
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input.")
        return
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = gen_password(length, include_uppercase, include_numbers, include_special)
    print("Generated password:",password)

if __name__ == "__main__":
    main()
