import pandas as pd
import random
from datetime import datetime, timedelta

# Load employees
employees = pd.read_csv("employees.csv")

shift_records = []

# Shift definitions
shifts = {
    "Morning": {
        "start": "09:00",
        "end": "17:00"
    },
    "Evening": {
        "start": "13:00",
        "end": "21:00"
    },
    "Night": {
        "start": "21:00",
        "end": "05:00"
    }
}

# Generate shifts for the last 90 days
start_date = datetime.now() - timedelta(days=90)

for _, employee in employees.iterrows():

    for day in range(90):

        date = start_date + timedelta(days=day)

        # Skip Saturday and Sunday
        if date.weekday() >= 5:
            continue

        # Select a random shift
        shift_type = random.choice(list(shifts.keys()))

        start_time = shifts[shift_type]["start"]
        end_time = shifts[shift_type]["end"]

        # Random overtime
        overtime_hours = random.choice([
            0, 0, 0, 1, 1, 2, 3
        ])

        # Shift status
        status = random.choices(
            ["Scheduled", "Completed", "Swapped"],
            weights=[10, 85, 5]
        )[0]

        # Swap information
        swap_requested = status == "Swapped"

        shift_records.append({
            "employee_id": employee["employee_id"],
            "date": date.strftime("%Y-%m-%d"),
            "shift_type": shift_type,
            "start_time": start_time,
            "end_time": end_time,
            "status": status,
            "overtime_hours": overtime_hours,
            "swap_requested": swap_requested
        })


# Convert to DataFrame
shift_df = pd.DataFrame(shift_records)

# Save dataset
shift_df.to_csv("shifts.csv", index=False)

print("Shift dataset created successfully!")
print("Total shift records:", len(shift_df))
print(shift_df.head())