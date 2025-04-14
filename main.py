# Import required libraries
import string  # For string operations (letters, digits, punctuation)
import random  # For shuffling and randomization

# Define character sets for password generation
s1 = list(string.ascii_lowercase)  # Lowercase letters (a-z)
s2 = list(string.ascii_uppercase)  # Uppercase letters (A-Z)
s3 = list(string.digits)          # Digits (0-9)
s4 = list(string.punctuation)     # Punctuation/symbols (!, @, #, etc.)

# Ask user for password length
characters_number = input("How many characters do you need for the password? ")

# Validate user input (must be a number and at least 8 characters)
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 8:
            print('Password must be at least 8 characters long.')
            characters_number = input("Please enter the length again: ")
        else:
            break  # Valid input, exit loop
    except ValueError:
        print("Invalid input. Please enter a number only.")
        characters_number = input("How many characters do you need for the password? ")

# Shuffle each character set for randomness
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate password composition (30% letters, 20% digits & symbols)
part1 = round(characters_number * (30 / 100))  # 30% for lowercase & uppercase
part2 = round(characters_number * (20 / 100))  # 20% for digits & symbols

password = []  # Initialize empty password list

# Add shuffled characters to password (alternating between sets)
for i in range(part1):
    password.append(s1[i])  # Add lowercase
    password.append(s2[i])  # Add uppercase

for i in range(part2):
    password.append(s3[i])  # Add digit
    password.append(s4[i])  # Add symbol

# Shuffle the final password for better randomness
random.shuffle(password)

# Convert list to string and trim to exact length (in case of rounding errors)
password = "".join(password[:characters_number])

# Output the generated password
print("\nGenerated Password:", password)
print("Password generation complete! ✅")