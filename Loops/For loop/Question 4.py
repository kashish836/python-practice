"""1. Count Even Numbers

Problem:

Given N, count how many even numbers exist between 1 and N.

Input:

Integer N.

Output:

Count of even numbers.

Example:

Input: 10

Output:"""

N = int(input("Enter the number:"))
count = 0
for i in range(2,N + 1, 2):
    count += 1
print("count no.:", count)


"""Simpler way

Since every 2 numbers contain 1 even number:

N/2

N/2


So you can directly write:"""

N = int(input("Enter the no.:"))

print("Count of even no.:", N//2)