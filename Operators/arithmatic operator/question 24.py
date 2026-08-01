"""Take a 4-digit number and find sum of digits using % and //."""

num = int(input("Enter the 4-digit number"))

digit4 = num % 10
remaining_num = num // 10
digit3 = remaining_num % 10
remaining_num = remaining_num // 10
digit2 = remaining_num % 10
digit1 = remaining_num // 10

digit_sum = digit1 + digit2 + digit3 + digit4

print("sum of the digit is = " , digit_sum)