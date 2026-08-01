#Print all odd numbers up to N

"""N = int(input("enter the no:"))
i = 1

while(i <= N):
    print(i)
    i += 2
"""

N = int(input("enter the no:"))
i = 1

while (i <= N):
    if i % 2 !=0:
        print(i)

    i += 1
