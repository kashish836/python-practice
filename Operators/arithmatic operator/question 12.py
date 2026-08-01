"""Take principal, rate, time and calculate simple interest.(P*R*T/100)"""

P = int(input("Enter the principle value: "))
R = int(input("Enter the rate of interest: "))
T = int(input("Enter the time: "))

Simple_interest = P * R * T / 100

print(Simple_interest)