"""1. Define a function called user_name that takes an email as input.
2. Find the index of the @ symbol in the email.
3. Slice the email string from the beginning to the index of the @ symbol.
4. Return the sliced string as the user name.
"""


def user_name(email):
    at_index = email.index("@")
    return email[:at_index]


email = input("Enter your email: ")
username = user_name(email)
print("Your username is:", username)
