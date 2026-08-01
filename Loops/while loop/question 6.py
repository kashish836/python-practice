"""Print multiplication table of N"""

N = int(input("Enter the table no. :"))
i = 1

while i <= 10:
    print(N, "x", i, "=", N*i )
    i += 1