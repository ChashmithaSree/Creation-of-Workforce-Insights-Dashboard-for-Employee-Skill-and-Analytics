import pandas as pd
import random
from datetime import datetime, timedelta

employees = pd.read_csv("employees.csv")

timesheet_records = []

projects = [
    "AI Workforce Dashboard",
    "Employee Analytics",
    "HR Automation",
    "Customer Analytics",
    "Internal Tools"
]

clients = [
    "Internal",
    "ABC Technologies",
    "Global Solutions",
    "TechCorp",
    "Enterprise Client"
]

statuses = ["Approved", "Pending", "Rejected"]

start_date = datetime.now() - timedelta(days=30)

for _, employee in employees.iterrows():

    for day in range(30):

        date = start_date + timedelta(days=day)

        # Skip weekends
        if date.weekday() >= 5:
            continue

        project = random.choice(projects)
        client = random.choice(clients)

        hours_worked = round(random.uniform(6, 9), 2)

        overtime_hours = max(0, round(hours_worked - 8, 2))

        status = random.choices(
            statuses,
            weights=[80, 15, 5]
        )[0]

        timesheet_records.append({
            "employee_id": employee["employee_id"],
            "date": date.strftime("%Y-%m-%d"),
            "project": project,
            "client": client,
            "hours_worked": hours_worked,
            "overtime_hours": overtime_hours,
            "status": status
        })

timesheet_df = pd.DataFrame(timesheet_records)

timesheet_df.to_csv("timesheets.csv", index=False)

print("Timesheet dataset created successfully!")
print("Total timesheet records:", len(timesheet_df))
print(timesheet_df.head())