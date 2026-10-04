import pandas as pd
import random

employees = pd.read_csv("employees.csv")

skills = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "AWS",
    "Azure",
    "Docker",
    "React",
    "Node.js",
    "Excel",
    "Power BI",
    "Communication",
    "Leadership",
    "Project Management"
]

skill_records = []

for _, employee in employees.iterrows():

    # Give each employee 3 to 6 random skills
    employee_skills = random.sample(
        skills,
        random.randint(3, 6)
    )

    for skill in employee_skills:

        proficiency = random.choice([
            "Beginner",
            "Intermediate",
            "Advanced",
            "Expert"
        ])

        skill_records.append({
            "employee_id": employee["employee_id"],
            "skill": skill,
            "proficiency": proficiency,
            "years_experience": round(random.uniform(0.5, 8), 1)
        })

skills_df = pd.DataFrame(skill_records)

skills_df.to_csv(
    "skills.csv",
    index=False
)

print("Skills dataset created successfully!")
print("Total skill records:", len(skills_df))
print(skills_df.head())