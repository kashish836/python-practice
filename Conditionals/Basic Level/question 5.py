"""5. Take temperature and print:
    - "Cold" if < 15
    - "Warm" if 15–30
    - "Hot" if > 30"""

Temp = int(input("what's the temperature:"))

if Temp < 15:
    print("The Temperature is cold i.e :", Temp)

elif Temp >=15 and Temp <= 30:
    print("The Temperature is Warm i.e:", Temp)

else:
    print("The Temperature is Hot i.e:", Temp)