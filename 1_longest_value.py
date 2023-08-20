# sourcery skip: avoid-global-variables, docstrings-for-functions, docstrings-for-modules
def longest_value(**kwargs):  # sourcery skip: docstrings-for-functions
    longest = None
    for value in kwargs.values():
        if longest is None or len(value) > len(longest):
            longest = value
    return longest


fruits = {"fruit": "apple", "color": "green"}

print(longest_value(**fruits))
