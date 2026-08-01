"""Take total marks of 5 subjects and calculate percentage."""

Maths = int(input("Enter ur maths marks out of 100: "))
Science = int(input("Enter ur sci marks out of 100: "))
English = int(input("Enter ur eng marks out of 100: "))
SST = int(input("Enter ur SST marks out of 100: "))
Hindi = int(input("Enter ur Hindi marks out of 100: "))

Total_markes_obtained = Maths+Science+English+SST+Hindi
OUT_of = 500

percentage = (Total_markes_obtained/OUT_of)*100

print("Your scored percentage is :", percentage)