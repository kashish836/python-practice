##Take password input and check if it equals "admin".

password = int(input("Enter the password:"))

admin = 12345

if password == admin:
    print("correct password, access granted")

else:
    print("wrong password , no access granted")