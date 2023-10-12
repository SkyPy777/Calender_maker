
import calendar

def generate_calendar(year, month):
    cal = calendar.month(year, month)
    return cal

while True:
    print("\n--- Calendar Maker ---")
    year = int(input("Enter the year (e.g., 2023): "))
    month = int(input("Enter the month (1-12): "))

    # Check if the input is valid
    if year < 1 or month < 1 or month > 12:
        print("Invalid input. Please enter a valid year and month.")
        continue

    # Generate and print the calendar
    print("\nCalendar:")
    print(generate_calendar(year, month))

    another = input("Do you want to generate another calendar? (yes/no): ").lower()
    if another != 'yes':
        break
