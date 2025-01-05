# initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# loop to get numbers from the user
while True:
    # ask for user input
    user_input = input("enter a number (or type 'stop' to finish): ")

    # check if the user wants to stop
    if user_input.lower() == "stop":
        break  # exit the loop

    # convert the input to an integer
    number = int(user_input)

    # check if the number is even or odd
    if number % 2 == 0:
        even_count += 1  # increase the even counter
    else:
        odd_count += 1  # increase the odd counter

# display the final counts
print(f"total even numbers: {even_count}")
print(f"total odd numbers: {odd_count}")
