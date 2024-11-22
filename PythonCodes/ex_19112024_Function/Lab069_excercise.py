def get_number(prompt, default_value):
    user_input = input(prompt)
    if user_input.strip() == "":
        return default_value
    try:
        return float(user_input)
    except ValueError:
        print("Invalid input. Using default value.")
        return default_value

def main():
    print("Enter three numbers (press Enter to use the default values):")
    num1 = get_number("Enter first number (default 100): ", 100)
    num2 = get_number("Enter second number (default 200): ", 200)
    num3 = get_number("Enter third number (default 300): ", 300)

    total = num1 + num2 + num3
    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":
    main()
