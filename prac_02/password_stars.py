"""CP1404 Password Stars program"""


def main():
    """Password Stars Program"""
    min_password_length = 10
    password = get_password(min_password_length)
    print_password_asterisks(password)


def print_password_asterisks(password):
    """Print the password length as asterisks"""
    print("*" * len(password))


def get_password(min_password_length):
    """Get a valid password with a minimum required length"""
    password = input("Password: ")
    while len(password) < min_password_length:
        print("Password too short")
        password = input("Password:")
    return password


main()
