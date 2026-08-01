##"""Take a number and check if it is divisible by 3, 5, or both."""

Num = int(input("Enter the number of your choice:"))

if Num % 3 == 0 and Num % 5 == 0:
    print("The choosen no. is divisible by 3 and 5 both")
elif Num % 3 == 0:
    print("The choosen no. is divisible by 3")
elif Num % 5 == 0:
    print("The choosen no. is divisibe by 5")
else:
    print("Not divisible by both")
