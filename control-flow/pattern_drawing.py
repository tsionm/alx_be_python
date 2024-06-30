def main():
  """Draws a square pattern of asterisks based on user input."""

  # Get user input for pattern size
  while True:
    try:
      size = int(input("Enter the size of the pattern (positive integer): "))
      if size > 0:
        break
      else:
        print("Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Draw the pattern using nested loops
  for row in range(size):
    for col in range(size):
      print("*", end="")
    print()  # Move to the next line after each row

if __name__ == "__main__":
  main()
