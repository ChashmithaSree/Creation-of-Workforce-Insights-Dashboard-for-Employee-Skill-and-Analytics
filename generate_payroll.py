import pandas as pd
import random

employees = pd.read_csv("employees.csv")

payroll_records = []

for _, employee in employees.iterrows():

    base_salary = employee["salary"]

    overtime_hours = random.randint(0, 20)
    overtime_pay = round(overtime_hours * 500, 2)

    leave_deduction = round(
        random.uniform(0, 5000), 2
    )

    incentives = round(
        random.uniform(0, 10000), 2
    )

    deductions = round(
        random.uniform(1000, 5000), 2
    )

    net_pay = round(
        base_salary
        + overtime_pay
        + incentives
        - leave_deduction
        - deductions,
        2
    )

    payroll_records.append({
        "employee_id": employee["employee_id"],
        "base_salary": base_salary,
        "overtime_hours": overtime_hours,
        "overtime_pay": overtime_pay,
        "leave_deduction": leave_deduction,
        "incentives": incentives,
        "other_deductions": deductions,
        "net_pay": net_pay,
        "payroll_status": random.choice([
            "Processed",
            "Pending"
        ])
    })

payroll_df = pd.DataFrame(payroll_records)

payroll_df.to_csv(
    "payroll_inputs.csv",
    index=False
)

print("Payroll dataset created successfully!")
print("Total payroll records:", len(payroll_df))
print(payroll_df.head())