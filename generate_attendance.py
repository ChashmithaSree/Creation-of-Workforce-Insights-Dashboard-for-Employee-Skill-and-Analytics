import pandas as pd
import random
from datetime import datetime, timedelta

# Load employees
employees = pd.read_csv("employees.csv")

attendance_records = []

# Generate attendance for the last 90 days
start_date = datetime.now() - timedelta(days=90)

for _, employee in employees.iterrows():

    for day in range(90):

        date = start_date + timedelta(days=day)

        # Skip weekends
        if date.weekday() >= 5:
            continue

        employee_id = employee["employee_id"]

        # Random attendance status
        status = random.choices(
            ["Present", "Late", "Absent"],
            weights=[85, 10, 5]
        )[0]

        check_in = None
        check_out = None
        work_hours = 0
        overtime_hours = 0

        if status == "Present":

            # Normal check-in between 8:45 and 9:30
            check_in_hour = random.randint(8, 9)
            check_in_minute = random.randint(0, 59)

            check_in = f"{check_in_hour:02d}:{check_in_minute:02d}"

            # Normal checkout between 17:00 and 18:30
            check_out_hour = random.randint(17, 18)
            check_out_minute = random.randint(0, 59)

            check_out = f"{check_out_hour:02d}:{check_out_minute:02d}"

            work_hours = round(random.uniform(7.5, 9.0), 2)

            if work_hours > 8:
                overtime_hours = round(work_hours - 8, 2)

        elif status == "Late":

            check_in_hour = random.randint(9, 10)
            check_in_minute = random.randint(0, 59)

            check_in = f"{check_in_hour:02d}:{check_in_minute:02d}"

            check_out_hour = random.randint(17, 19)
            check_out_minute = random.randint(0, 59)

            check_out = f"{check_out_hour:02d}:{check_out_minute:02d}"

            work_hours = round(random.uniform(6.5, 8.0), 2)

            if work_hours > 8:
                overtime_hours = round(work_hours - 8, 2)

        # Attendance method
        attendance_method = random.choice([
            "Biometric",
            "Face Recognition",
            "QR",
            "GPS"
        ])

        # Anomaly detection simulation
        anomaly = False
        anomaly_reason = None

        if status == "Late" and random.random() < 0.3:
            anomaly = True
            anomaly_reason = "Repeated late check-in"

        elif status == "Absent" and random.random() < 0.2:
            anomaly = True
            anomaly_reason = "Unexpected absence"

        attendance_records.append({
            "employee_id": employee_id,
            "date": date.strftime("%Y-%m-%d"),
            "status": status,
            "check_in": check_in,
            "check_out": check_out,
            "work_hours": work_hours,
            "overtime_hours": overtime_hours,
            "attendance_method": attendance_method,
            "anomaly": anomaly,
            "anomaly_reason": anomaly_reason
        })


# Convert to DataFrame
attendance_df = pd.DataFrame(attendance_records)

# Save CSV
attendance_df.to_csv("attendance.csv", index=False)

print("Attendance dataset created successfully!")
print("Total records:", len(attendance_df))
print(attendance_df.head())