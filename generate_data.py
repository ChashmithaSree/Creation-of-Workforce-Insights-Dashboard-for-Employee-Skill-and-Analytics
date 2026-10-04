import random
import pandas as pd
from faker import Faker

fake = Faker()

# Make the generated data reproducible
random.seed(42)
Faker.seed(42)

NUM_EMPLOYEES = 500

departments = [
    "Engineering",
    "Data Science",
    "Human Resources",
    "Finance",
    "Marketing",
    "Sales",
    "Operations",
    "IT Support"
]

roles = {
    "Engineering": [
        "Software Engineer",
        "Senior Software Engineer",
        "Tech Lead"
    ],
    "Data Science": [
        "Data Scientist",
        "ML Engineer",
        "Data Analyst"
    ],
    "Human Resources": [
        "HR Executive",
        "HR Manager",
        "Recruiter"
    ],
    "Finance": [
        "Financial Analyst",
        "Accountant",
        "Finance Manager"
    ],
    "Marketing": [
        "Marketing Executive",
        "Marketing Analyst",
        "Marketing Manager"
    ],
    "Sales": [
        "Sales Executive",
        "Sales Manager",
        "Business Development Executive"
    ],
    "Operations": [
        "Operations Executive",
        "Operations Manager",
        "Operations Analyst"
    ],
    "IT Support": [
        "IT Support Engineer",
        "System Administrator",
        "IT Manager"
    ]
}

locations = [
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Mumbai",
    "Delhi"
]

employment_types = [
    "Full-Time",
    "Part-Time",
    "Contract"
]

skill_pool = [
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

employees = []

for i in range(1, NUM_EMPLOYEES + 1):

    department = random.choice(departments)

    employee_role = random.choice(
        roles[department]
    )

    first_name = fake.first_name()
    last_name = fake.last_name()

    name = f"{first_name} {last_name}"

    email = (
        f"{first_name.lower()}."
        f"{last_name.lower()}"
        f"{i}@novacore.com"
    )

    joining_date = fake.date_between(
        start_date="-10y",
        end_date="today"
    )

    experience = random.randint(0, 12)

    salary = random.randint(
        300000,
        1800000
    )

    performance_score = round(
        random.uniform(4.5, 10.0),
        1
    )

    job_satisfaction = random.randint(
        1,
        10
    )

    overtime_hours = random.randint(
        0,
        40
    )

    training_hours = random.randint(
        0,
        80
    )

    promotion_count = random.randint(
        0,
        4
    )

    absenteeism_days = random.randint(
        0,
        20
    )

    employee_skills = random.sample(
        skill_pool,
        random.randint(2, 5)
    )

    # Generate attrition based on several factors
    attrition_probability = 0.10

    if job_satisfaction <= 4:
        attrition_probability += 0.20

    if overtime_hours >= 25:
        attrition_probability += 0.15

    if performance_score <= 6:
        attrition_probability += 0.10

    if promotion_count == 0 and experience >= 5:
        attrition_probability += 0.10

    attrition = (
        "Yes"
        if random.random() < attrition_probability
        else "No"
    )

    employee = {
        "employee_id": f"EMP{i:04d}",
        "name": name,
        "email": email,
        "role": employee_role,
        "department": department,
        "location": random.choice(locations),
        "joining_date": joining_date,
        "employment_type": random.choice(
            employment_types
        ),
        "experience_years": experience,
        "salary": salary,
        "performance_score": performance_score,
        "job_satisfaction": job_satisfaction,
        "overtime_hours": overtime_hours,
        "training_hours": training_hours,
        "promotion_count": promotion_count,
        "absenteeism_days": absenteeism_days,
        "skills": ", ".join(employee_skills),
        "attrition": attrition
    }

    employees.append(employee)


# Convert to DataFrame
df = pd.DataFrame(employees)

# Save dataset
df.to_csv(
    "employees.csv",
    index=False
)

print("Dataset created successfully!")
print("Number of employees:", len(df))
print()
print(df.head())