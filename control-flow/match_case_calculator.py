def main():
  """Performs basic arithmetic operations using match-case."""

  # Get user input for numbers
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get user input for operation
  operation = input("Choose the operation (+, -, *, /): ")

  # Perform calculation using match-case (requires Python 3.10+)
  match operation:
    case "+":
      result = num1 + num2
      print(f"The result is {result}.")
    case "-":
      result = num1 - num2
      print(f"The result is {result}.")
    case "*":
      result = num1 * num2
      print(f"The result is {result}.")
    case "/":
      if num2 == 0:
        print("Cannot divide by zero.")
      else:
        result = num1 / num2
        print(f"The result is {result}.")
    case _:
      print("Invalid operation symbol. Please use +, -, *, or /.")

if __name__ == "__main__":
  main()

