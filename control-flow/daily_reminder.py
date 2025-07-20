"""daily_reminder
"""

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bounded = input("Is it time-bound (yes/no): ")

match priority:
    case "high":
        if time_bounded == "yes":
            print(f"Your task '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Your task '{task}' is a {priority} task. Consider completing it when you have free time.")
        
    case "medium":
        if time_bounded == "yes":
            print(f"Your task '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Your task '{task}' is a {priority} task. Consider completing it when you have free time.")
    
    case "low":
        if time_bounded == "yes":
            print(f"Your task '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Your task '{task}' is a {priority} task. Consider completing it when you have free time.")
        
        