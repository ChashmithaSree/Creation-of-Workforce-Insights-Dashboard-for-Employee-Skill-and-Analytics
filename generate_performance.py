import pandas as pd
import random
from datetime import datetime, timedelta

employees = pd.read_csv("employees.csv")

performance_records = []

review_statuses = ["Completed", "Pending"]

strengths = [
    "Good technical skills",
    "Strong communication",
    "Good teamwork",
    "Problem solving",
    "Leadership",
    "Fast learner"
]

improvement_areas = [
    "Time management",
    "Communication",
    "Technical skills",
    "Leadership",
    "Team collaboration",
    "Problem solving"
]

for _, employee in employees.iterrows():

    kpi_score = random.randint(60, 100)
    goal_completion = random.randint(60, 100)
    productivity_score = random.randint(60, 100)
    manager_rating = random.randint(1, 5)

    # Calculate overall performance
    performance_rating = round(
        (kpi_score + goal_completion + productivity_score) / 3,
        2
    )

    review_status = random.choices(
        review_statuses,
        weights=[80, 20]
    )[0]

    review_date = datetime.now() - timedelta(
        days=random.randint(0, 90)
    )

    performance_records.append({
        "employee_id": employee["employee_id"],
        "review_date": review_date.strftime("%Y-%m-%d"),
        "kpi_score": kpi_score,
        "goal_completion": goal_completion,
        "productivity_score": productivity_score,
        "manager_rating": manager_rating,
        "performance_rating": performance_rating,
        "review_status": review_status,
        "strengths": random.choice(strengths),
        "improvement_area": random.choice(improvement_areas)
    })


performance_df = pd.DataFrame(performance_records)

performance_df.to_csv(
    "performance.csv",
    index=False
)

print("Performance dataset created successfully!")
print("Total performance records:", len(performance_df))
print(performance_df.head())