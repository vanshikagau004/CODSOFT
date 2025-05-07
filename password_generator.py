import random
import string

def generate_password(length):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
