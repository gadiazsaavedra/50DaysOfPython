def convert_add(**kwargs):
    """Converts a string to a float and adds it to the total"""
    return sum(float(value) for value in kwargs.values())

list1 = ["1", "2", "3"]
print(convert_add(**list1))

