def perform_operation(num1, num2, operation):
    # Perform the operation based on the 'operation' argument
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
