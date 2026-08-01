"""Take two numbers and print remainder without using % (use formula)."""


num1 = int(input("Enter the num1 value : "))

num2 = int(input("Enter the num2 value : "))

quotient = num1 // num2
remainder = num1 - (num2 *  quotient )

print("the Remaainder :", remainder)