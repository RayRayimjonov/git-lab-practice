def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("=== CALCULATOR V2 ===")
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(4, 3))
    print(divide(10, 2))
