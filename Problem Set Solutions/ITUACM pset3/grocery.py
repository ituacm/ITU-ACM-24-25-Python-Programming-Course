def calculate_prices(user_input):
    # dictionary of item prices per kilogram
    prices = {"apple": 1.5, "banana": 0.5, "milk": 2.5, "bread": 3.0, "tomatoes": 3.5}

    # check for input format validity
    if "kg of" not in user_input:
        return "Invalid input format. Please use '<quantity> kg of <item>'."

    # split the input to extract quantity and item
    quantity_part, item = user_input.split("kg of")
    try:
        quantity = float(quantity_part.strip())
    except ValueError:
        return "Invalid input. Please enter the quantity as a number."

    item = item.strip()

    # check for negative quantities
    if quantity < 0:
        return "Invalid input. Quantity cannot be negative."
    if item not in prices:
        return f"Item '{item}' not found in the price list."
    # calculate total price
    total_price = quantity * prices[item]
    return f"The total price for {quantity} kg of {item} is {total_price:.2f} dollars."


def main():
    # take user input in the format "<quantity> kg of <item>"
    result = calculate_prices(
        input("Enter item and quantity (e.g., '3 kg of apple'): ").strip()
    )
    print(result)


if __name__ == "__main__":
    main()
