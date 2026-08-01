"""
Take age and print:
    - "Child" if age < 13
    - "Teen" if age 13–19
    - "Adult" otherwise

"""

Age = int(input("Enter Your Age:"))

if Age < 13:
    print("You are a child")

elif Age >= 13 and Age <= 19:
    print("You are a Teen")

else:
    print("You are an Adult")