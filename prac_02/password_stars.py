"""CP1404 Password Stars program"""

min_password_length = 10
password = input("Password: ")
while len(password) < min_password_length:
    print("Password too short")
    password = input("Password:")
print("*" * len(password))
