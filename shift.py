# Import the datetime module
import datetime

# Define the shift schedule
SHIFT_SCHEDULE = ["day", "night", "free", "free"]

# Define a function to calculate the future shift
def future_shift(prev_date: datetime.date, prev_shift: str, future_date: datetime.date) -> str:
  # Find the index of the previous shift in the shift schedule
  prev_shift_index = SHIFT_SCHEDULE.index(prev_shift)

  # Calculate the number of days between the two dates
  num_days = (future_date - prev_date).days

  # Calculate the index of the shift that will be worked on the future date
  shift_index = (prev_shift_index + num_days) % len(SHIFT_SCHEDULE)

  # Return the shift that will be worked on the future date
  return SHIFT_SCHEDULE[shift_index]

# Prompt the user to enter the previous date
prev_date_input = input("Enter the previous date (YYYY-MM-DD): ")

# Parse the previous date from the user input
prev_date = datetime.datetime.strptime(prev_date_input, "%Y-%m-%d").date()

# Prompt the user to enter the previous shift
prev_shift = input("Enter the previous shift (day/night/free): ")

# Prompt the user to enter the future date
future_date_input = input("Enter the future date (YYYY-MM-DD): ")

# Parse the future date from the user input
future_date = datetime.datetime.strptime(future_date_input, "%Y-%m-%d").date()

# Calculate the future shift
future_shift = future_shift(prev_date, prev_shift, future_date)

# Print the result
print(f"The future shift on {future_date} will be {future_shift}")
