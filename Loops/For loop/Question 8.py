"""1. Sum of Digits

Problem:

Given N, find sum of its digits.

Input:

Integer N.

Output:

Sum of digits.

Example:

Input: 123

Output:"""

N = int(input("enter the number:"))
number_str = str(abs(N))
total = 0
for i in number_str:
    total += int(i)

print(total)