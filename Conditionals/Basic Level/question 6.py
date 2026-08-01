"""6. Take salary and classify:
    - Low (< 30000)
    - Medium (30000–70000)
    - High (> 70000)"""

Salary = int(input("Enter your salary:"))

if Salary < 30000:
    print("Salary is Low")

elif Salary >= 30000 and Salary <= 70000:
    print("Salary is Medium")

else:
    print("Salary is High")