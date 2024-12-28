import random
import string


def generate_password(length=12):
    """
    Generate a secure random password.

    Parameters:
    length (int): The desired length of the password. Must be at least 4 characters.

    Returns:
    str: The generated password, or an error message if the length is invalid.
    """
    if length < 4:
        return "Error: Password length must be at least 4 characters."

    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("Welcome to the Secure Password Generator!")
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length (default is 12): "))
        print(f"Generated Password: {generate_password(length)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

