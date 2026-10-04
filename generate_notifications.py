import pandas as pd
import random
from datetime import datetime, timedelta

employees = pd.read_csv("employees.csv")

notification_types = [
    "Shift Reminder",
    "Leave Update",
    "Attendance Alert",
    "Training Reminder",
    "Performance Review",
    "Payroll Notification",
    "Birthday",
    "Work Anniversary"
]

statuses = [
    "Unread",
    "Read"
]

messages = {
    "Shift Reminder": "Your upcoming shift is scheduled.",
    "Leave Update": "Your leave request has been updated.",
    "Attendance Alert": "Please check your attendance record.",
    "Training Reminder": "You have a pending training course.",
    "Performance Review": "Your performance review is due.",
    "Payroll Notification": "Your payroll information has been processed.",
    "Birthday": "Happy Birthday!",
    "Work Anniversary": "Happy Work Anniversary!"
}

notification_records = []

for _, employee in employees.iterrows():

    number_of_notifications = random.randint(2, 5)

    for _ in range(number_of_notifications):

        notification_type = random.choice(notification_types)

        created_date = (
            datetime.now()
            - timedelta(days=random.randint(0, 90))
        )

        notification_records.append({
            "employee_id": employee["employee_id"],
            "notification_type": notification_type,
            "message": messages[notification_type],
            "status": random.choice(statuses),
            "created_date": created_date.strftime("%Y-%m-%d")
        })

notifications_df = pd.DataFrame(notification_records)

notifications_df.to_csv(
    "notifications.csv",
    index=False
)

print("Notifications dataset created successfully!")
print("Total notification records:", len(notifications_df))
print(notifications_df.head())