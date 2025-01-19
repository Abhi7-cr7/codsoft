import random
import string
import time
import sys

def generate_password(length):
    """
    Generate a strong, random password of the specified length.
    The password includes:
    - Lowercase letters
    - Uppercase letters
    - Digits
    - Special characters
    """
    # Define the character sets
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~

    # Combine all characters into a pool
    all_chars = lower + upper + digits + special_chars
    
    # Randomly select characters to form the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def typing_effect(text, speed=0.1):
    """
    Simulate a typing effect by printing characters one by one with a delay.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_animation(duration=3):
    """
    Display a loading animation (spinning dots) for a specified duration.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in ['|', '/', '-', '\\']:
            sys.stdout.write(f'\rGenerating your password... {char} ')
            sys.stdout.flush()
            time.sleep(0.2)

def main():
    print("Welcome to the Password Generator!")

    # User input: specify the length of the password
    try:
        length = int(input("Enter the desired password length: "))

        # Ensure password length is positive
        if length <= 0:
            print("Password length must be a positive integer!")
            return
        
        # Show loading animation while generating the password
        loading_animation()
        
        # Generate the password
        password = generate_password(length)

        # Simulate the typing effect for the password display
        print("\nGenerating password...")
        typing_effect(f"Your generated password is: {password}", speed=0.1)
    
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()