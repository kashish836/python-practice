"""1. Count Digits

Problem:

Given an integer N, count how many digits it contains.

Input:

Integer N.

Output:

Digit count.

Example:

Input: 12345

Output:"""


N = int(input("enter the no.:"))

number_str = str(abs(N))

count = 0
for i in number_str:
    count += 1

print(count)

"""Why this works:
abs(N): This removes any negative sign so the code doesn't accidentally count - as a digit.
str(...): This turns a number like 12345 into text characters "12345".
for digit in number_str: The loop runs exactly once for every single character in that text.
count += 1: Every time the loop finds a character, it adds 1 to your total counter.
"""