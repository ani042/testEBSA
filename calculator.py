"""A simple calculator with basic arithmetic operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Run an interactive calculator session."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit.\n")

    while True:
        expression = input("Enter expression (e.g. 3 + 4): ").strip()
        if expression.lower() == "quit":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Invalid input. Please enter: <number> <operator> <number>")
            continue

        num1_str, operator, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            continue

        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print(f"Unknown operator '{operator}'. Use +, -, *, /.")
                continue

            # Display integers without decimal point when result is whole number
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
