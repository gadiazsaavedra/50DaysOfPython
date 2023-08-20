def only_floats(a, b):
    # Check if both arguments are floats
    if isinstance(a, float) and isinstance(b, float):
        return 2
    # Check if only one argument is a float
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    # If neither argument is a float, return 0
    else:
        return 0
print(only_floats(12, 23))
