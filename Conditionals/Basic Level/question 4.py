""" Take marks and print:
    - "Fail" if < 35
    - "Pass" if 35–59
    - "First Class" if 60–79
    - "Distinction" if 80+"""

Marks = int(input("Enter Your Scored Marks:"))

if Marks < 35:
    print("Failed")

elif Marks >= 35 and Marks <= 59:
    print("Passed")

elif Marks >=60 and Marks <= 79:
    print("First Class")

else:
    print("Distinction")