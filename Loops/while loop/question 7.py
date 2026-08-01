"""Count digits in a number"""

num = int(input("Enter the no: "))
count = 0

while num > 0:
    count += 1
    num = num // 10  # This removes the last digit

print(count)
