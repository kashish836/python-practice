"""1. Multiplication Table

Problem:

Given an integer N, print its multiplication table up to 10.

Input:

Integer N.

Output:

N x 1 = …"""

N = int(input("Enter the number you want table of:"))

for i in range(1,11):
    print(N, "x", i, "=", N*i)

"""A cleaner version using f-strings:"""

N = int(input("Enter the number you want table of: "))

for i in range(1, 11):
    print(f"{N} x {i} = {N*i}")