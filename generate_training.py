import pandas as pd
import random
from datetime import datetime, timedelta

employees = pd.read_csv("employees.csv")

training_courses = [
    "Python for Data Science",
    "Machine Learning Fundamentals",
    "Deep Learning",
    "AWS Cloud Fundamentals",
    "Docker and Kubernetes",
    "SQL and Database Management",
    "Power BI Analytics",
    "Leadership Skills",
    "Communication Skills",
    "Project Management",
    "Generative AI",
    "Cybersecurity Fundamentals"
]

training_statuses = [
    "Completed",
    "In Progress",
    "Not Started"
]

training_records = []

for _, employee in employees.iterrows():

    # Each employee gets 1 to 4 training courses
    number_of_courses = random.randint(1, 4)

    selected_courses = random.sample(
        training_courses,
        number_of_courses
    )

    for course in selected_courses:

        status = random.choices(
            training_statuses,
            weights=[60, 25, 15]
        )[0]

        if status == "Completed":
            completion_date = (
                datetime.now() -
                timedelta(days=random.randint(1, 180))
            ).strftime("%Y-%m-%d")

            score = random.randint(60, 100)

        elif status == "In Progress":
            completion_date = None
            score = None

        else:
            completion_date = None
            score = None

        training_records.append({
            "employee_id": employee["employee_id"],
            "course": course,
            "status": status,
            "completion_date": completion_date,
            "score": score
        })

training_df = pd.DataFrame(training_records)

training_df.to_csv(
    "training.csv",
    index=False
)

print("Training dataset created successfully!")
print("Total training records:", len(training_df))
print(training_df.head())