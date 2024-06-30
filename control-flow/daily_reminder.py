def main():
  """Provides a reminder based on a user-defined task and its urgency."""

  # Get user input for task
  task = input("Enter your task: ")

  # Get user input for priority
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Get user input for time sensitivity
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Process task information and create reminder
  urgency_message = ""
  if time_bound == "yes":
    urgency_message = " that requires immediate attention today!"

  match priority:
    case "high":
      reminder = f"Reminder: '{task}' is a high priority task{urgency_message}"
    case "medium":
      reminder = f"Reminder: '{task}' has a medium priority. Consider completing it when you have a chance."
    case "low":
      reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

  print(reminder)

if __name__ == "__main__":
  main()

