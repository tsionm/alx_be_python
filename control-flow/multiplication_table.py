def main():
  """Generates a multiplication table for a user-specified number."""

  # Get user input for the number
  number = int(input("Enter a number to see its multiplication table: "))

  # Print multiplication table header
  print("Multiplication Table for", number)

  # Use for loop to iterate from 1 to 10
  for i in range(1, 11):
    # Calculate product and print the table row
    product = number * i
    print(f"{number} * {i} = {product}")

if __name__ == "__main__":
  main()

