from datetime import datetime, timedelta

def display_current_datetime():
  """
  Gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
  """
  Calculates the future date based on the provided number of days added to the current date.

  Args:
      days (int): The number of days to add.

  Returns:
      datetime: The future date.
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  return future_date

def main():
  """
  Drives the program execution by calling the defined functions.
  """
  display_current_datetime()

  # Clear previous output or add a separator for better user experience
  # Option 1: Clear the console/terminal (uncomment if desired)
  # import os
  # os.system('cls' if os.name == 'nt' else 'clear')  # Clear console based on OS

  # Option 2: Add a separator line (uncomment if desired)
  # print("-" * 30)

  while True:
    try:
      days = int(input("Enter the number of days to add to the current date (or 'q' to quit): "))
      if days == 'q':
        break
      future_date = calculate_future_date(days)
      formatted_future_date = future_date.strftime("%Y-%m-%d")
      print(f"Future date: {formatted_future_date}")
    except ValueError:
      print("Invalid input. Please enter an integer or 'q' to quit.")

if __name__ == "__main__":
  main()
