# Add type hints for the functions
def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")


def calculate(operation, num1, num2):
    try:
        if operation == '1':
            return add(num1, num2), '+'
        elif operation == '2':
            return subtract(num1, num2), '-'
        elif operation == '3':
            return multiply(num1, num2), '*'
        elif operation == '4':
            return divide(num1, num2), '/'
    except ValueError as e:
        print(e)
        return None, None

def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = get_user_input("Enter the first number: ")
        num2 = get_user_input("Enter the second number: ")

        result, operation = calculate(choice, num1, num2)

        if result is not None and operation is not None:
            print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid Input")

if __name__ == '__main__':
    main()
