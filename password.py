import random

print('Welcome to our Password Generator')
print('=================================')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'

# Function to get valid integer input from user
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get user inputs with validation
number = get_valid_int('Amount of Password generate: ')
length = get_valid_int('Enter the length of Password Generate: ')

# Generate passwords
print('\nHere is your Password:')
for pwd in range(number):
    Passwords = ''
    for c in range(length):
        Passwords += random.choice(chars)
    print(Passwords)
