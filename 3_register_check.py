"""register_check"""
def register_check():
    """register_check"""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin":
        print("Welcome to the system")
    else:
        print("Invalid username or password")