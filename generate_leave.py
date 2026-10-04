import pandas as pd
import random
from datetime import datetime, timedelta

# Load employees
employees = pd.read_csv("employees.csv")

leave_records = []

leave_types = [
    "Casual Leave",
    "Sick Leave",
    "Earned Leave",
    "Work From Home"
]

statuses = [
    "Approved",
    "Pending",
    "Rejected"
]

# Generate leave requests
for _, employee in employees.iterrows():

    # Each employee gets 0–6 leave requests
    number_of_requests = random.randint(0, 6)

    for _ in range(number_of_requests):

        start_date = datetime.now() - timedelta(
            days=random.randint(0, 90)
        )

        number_of_days = random.randint(1, 5)

        end_date = start_date + timedelta(
            days=number_of_days - 1
        )

        leave_type = random.choice(leave_types)

        status = random.choices(
            statuses,
            weights=[70, 20, 10]
        )[0]

        # Reason based on leave type
        if leave_type == "Sick Leave":
            reason = random.choice([
                "Fever",
                "Health issue",
                "Medical appointment",
                "Not feeling well"
            ])

        elif leave_type == "Casual Leave":
            reason = random.choice([
                "Personal work",
                "Family function",
                "Personal emergency",
                "Travel"
            ])

        elif leave_type == "Earned Leave":
            reason = random.choice([
                "Vacation",
                "Family vacation",
                "Personal break",
                "Travel"
            ])

        else:
            reason = random.choice([
                "Personal work",
                "Remote work requirement",
                "Travel",
                "Family situation"
            ])

        # Approved by manager only when approved
        if status == "Approved":
            approved_by = random.choice([
                "Manager",
                "HR Manager",
                "Team Lead"
            ])
        else:
            approved_by = None

        leave_records.append({
            "employee_id": employee["employee_id"],
            "leave_type": leave_type,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "number_of_days": number_of_days,
            "reason": reason,
            "status": status,
            "requested_date": (
                start_date - timedelta(days=random.randint(1, 10))
            ).strftime("%Y-%m-%d"),
            "approved_by": approved_by
        })


# Convert to DataFrame
leave_df = pd.DataFrame(leave_records)

# Save CSV
leave_df.to_csv("leave_requests.csv", index=False)

print("Leave dataset created successfully!")
print("Total leave requests:", len(leave_df))
print(leave_df.head())