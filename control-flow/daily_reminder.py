# daily_reminder.py

# Prompt the user for a task description
task = input("Enter your task: ")

# Check if the task input is not empty
if not task:
    print("Task description cannot be empty. Please try again.")
else:
    # Prompt for the task's priority
    priority = input("Priority (high/medium/low): ").lower()

    # Check if priority is valid
    if priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please choose from 'high', 'medium', or 'low'.")
    else:
        # Prompt if the task is time-bound
        time_bound = input("Is it time-bound? (yes/no): ").lower()

        # Check if time-bound input is valid
        if time_bound not in ['yes', 'no']:
            print("Invalid input for time-bound. Please answer 'yes' or 'no'.")
        else:
            # Process the task based on priority using Match Case
            match priority:
                case "high":
                    reminder = f"Reminder: '{task}' is a high priority task"
                case "medium":
                    reminder = f"Reminder: '{task}' is a medium priority task"
                case "low":
                    reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
                case _:
                    reminder = "Invalid priority. Please choose from 'high', 'medium', or 'low'."
            
            # Modify the reminder if the task is time-bound
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            elif time_bound == "no":
                reminder += "."

            # Output the final customized reminder
            print(reminder)
