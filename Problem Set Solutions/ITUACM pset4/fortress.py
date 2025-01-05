import random

FORTRESS_FILE = "fortress.txt"

def write_square_to_file(size, filename):
    """Writes a square wall of the given size to the file."""
    with open(filename, "a") as file:
        for _ in range(size):
            file.write("#" * size + "\n")

def display_fortress(filename):
    """Reads and displays the contents of the fortress file."""
    try:
        with open(filename, "r") as file:
            contents = file.read()
            if contents.strip():
                print("\nCurrent Fortress:\n")
                print(contents)
            else:
                print("\nThe fortress is empty.\n")
    except FileNotFoundError:
        print("\nThe fortress file does not exist yet. Add a wall to create it.\n")

def clear_fortress(filename):
    """Clears all content from the fortress file."""
    open(filename, "w").close()  # Open in write mode to overwrite with nothing
    print("\nThe fortress has been cleared!\n")

def main():
    """Main function to interact with the fortress."""
    print("Welcome to the Kingdom of CodeLand! Let’s add to the fortress.")
    
    while True:
        user_input = input("Enter the size of the wall (or type 'clear', 'random', or 'exit' to quit): ").strip()
        
        if user_input.lower() == "clear":
            clear_fortress(FORTRESS_FILE)
        elif user_input.lower() == "random":
            size = random.randint(1, 10)
            print(f"\nA random wall of size {size} was added to fortress.txt!\n")
            write_square_to_file(size, FORTRESS_FILE)
        elif user_input.isdigit() and int(user_input) > 0:
            size = int(user_input)
            print(f"\nWall of size {size} added to fortress.txt!\n")
            write_square_to_file(size, FORTRESS_FILE)
        elif user_input.lower() == "exit":
            print("\nExiting the fortress builder. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("\nInvalid input. Please enter a positive number, 'clear', 'random', or 'exit'.\n")
        
        display_fortress(FORTRESS_FILE)

# Run the program
if __name__ == "__main__":
    main()
