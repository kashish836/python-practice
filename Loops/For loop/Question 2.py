"""1. Sum of First N Numbers

Problem:

Given N, compute the sum of numbers from 1 to N.

Input:

Integer N.

Output:

Single integer representing the sum.

Example:

Input: 5

Output:

15"""

N = int(input("Enter the number:"))
total = 0

for i in range(1,N+1):
    total += i

    print(total)


"""You can also do it using the formula:

N(N+1)//2


N(N+1)//2


Python code for formula method:"""

N = int(input("Enter number:"))

sum = N*(N+1)//2

print(sum)