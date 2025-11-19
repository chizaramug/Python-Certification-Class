# Initialize a list to store the total steps for each month
monthly_totals = [0] * 12

# Open the steps.txt file for reading
with open('steps.txt', 'r') as file:
    lines = file.readlines()

# Check if the file contains 365 lines (one for each day)
if len(lines) != 365:
    print("Invalid data: The file should contain 365 lines.")
else:
    # Iterate through the lines and accumulate monthly totals
    for day, steps in enumerate(lines, start=1):
        month = (day - 1) // 30  # Determine the month (0 to 11)
        monthly_totals[month] += int(steps)

    # Calculate and display the average steps per month
    for month, total_steps in enumerate(monthly_totals):
        days_in_month = 30 if month != 1 else 28  # February has 28 days
        average_steps = total_steps / days_in_month
        print(f"Month {month + 1}: {average_steps:.2f} average steps per day")
