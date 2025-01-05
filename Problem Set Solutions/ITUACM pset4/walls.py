def main():
    try:
        print_square(int(input("please enter the size of walls: ")))
    except ValueError:
        print("please enter an integer")


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)

if __name__ == "__main__":
    main()