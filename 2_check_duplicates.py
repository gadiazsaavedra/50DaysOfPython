"""check_duplicates"""
fruits = ["apple", "orange", "banana", "apple", "banana", "kiwi"]
names = ["Yoda", "Moses", "Joshua", "Mark"]
print("cant. de elementos en lista : ", len(fruits))
fruits_set = set(fruits)
print("cant.element. NO duplicados : ", len(fruits_set))

unique_items = []
duplic_items = []
for fruit in fruits:
    if fruit not in unique_items:
        unique_items.append(fruit)
    else:
        duplic_items.append(fruit)
print("lista filtrada : ", unique_items)
print("lista de duplicados : ", duplic_items)


def check_duplicates(*args):
    """check_duplicates"""
    unique_items = []
    duplic_items = []
    for arg in args:
        if arg not in unique_items:
            unique_items.append(arg)
        else:
            duplic_items.append(arg)
    return unique_items


names = ["Yoda", "Moses", "Joshua", "Mark", "Yoda"]

print(check_duplicates(["apple", "orange", "banana", "apple", "banana", "kiwi"]))
