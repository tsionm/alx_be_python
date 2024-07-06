def perform_operation(num1, num2, operation):
  """
  This function performs basic arithmetic operations based on the provided parameters.

  Args:
      num1 (float): The first number.
      num2 (float): The second number.
      operation (str): The arithmetic operation to perform ("add", "subtract", "multiply", or "divide").

  Returns:
      float: The result of the arithmetic operation, or a specific message for division by zero.
  """

  # Handle division by zero
  if operation == "divide" and num2 == 0:
    return "Error: Cannot divide by zero"

  # Perform operation based on input
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    return num1 / num2
  else:
    # Handle invalid operation input
    return "Error: Invalid operation"



def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
