# ============================= Q1 Solution: Password Validation ============================= #

# The loop continues until the password criteria are met
pwd = input('Enter your password: ')
while not (pwd.isalnum() and not pwd.isalpha() and len(pwd) > 8):
    print("Password must be at least 8 characters and include a number.")
    pwd = input('Enter your password: ')
print('Password accepted.')

# pwd.isalnum(): Ensures the password is alphanumeric, meaning it contains only letters and numbers (no special characters).
# not pwd.isalpha(): Ensures the password is not just letters; it must contain at least one number.
# len(pwd) >= 8: Ensures the password is at least 8 characters long.


# ============================ Q2 Solution: Abundant Number Check ============================ #
# This program checks if a given number is an "abundant number."
# An abundant number is one for which the sum of its proper divisors is greater than the number itself.
# Steps:
# 1. Iterate from 1 to the number-1, checking divisors.
# 2. Sum all proper divisors (i.e., divisors excluding the number itself).
# 3. Compare the sum with the number to determine if it is abundant.

num = int(input("Enter a number to check for abundance: "))

i = 1
divisor_sum = 0  # renamed 'sum' to avoid overwriting built-in sum function
while i < num:
    if num % i == 0:
        divisor_sum += i
    i += 1

print(('Not ' if divisor_sum <= num else '') + 'Abundant')


# ======================== Q3 Solution: Area and Perimeter Calculator ======================== #
PI = 3

while True: # Continues until user chooses to stop
    shape = input('Enter kind (1:Circle, 2:Square, 3:Equilateral Triangle): ')

    if shape == '1': # Circle, ask for radius
        radius = float(input('Radius of circle: '))
        area = 3 * radius ** 2
        perimeter = 2 * PI * radius
    elif shape == '2': # Square, ask for edge length
        edge_len = float(input('Edge length: '))
        area = edge_len ** 2
        perimeter = 4 * edge_len
    elif shape == '3': # Equilateral Triangle, ask for edge length
        edge_len = float(input('Edge length: '))
        area = (3 ** .5) / 4 * edge_len ** 2 # Formula for area of an equilateral triangle
        perimeter = 3 * edge_len
    else: # Invalid input
        print('Invalid kind. Please enter 1, 2, or 3.')
        continue # Restart the loop
    
    print('Calculated area:', area)
    print('Calculated perimeter:', perimeter)
    
    
    cont = input('Do you want to calculate another shape? (Y/N): ')
    if cont.upper() != 'Y': # If the user does not want to continue (by entering 'y' or 'Y'), break the loop
        break # Exit the loop

print('Goodbye!')
