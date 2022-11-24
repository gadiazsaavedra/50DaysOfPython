list1 = ["1", "2", "3"]
for i in range(len(list1)):
    list1[i] = int(list1[i])
print("1er.metodo : ", sum(list1))

print("2do.metodo : ", sum(list(map(int, list1))))


def convert_add(*argv) -> None:
    """Converts a string to a float and adds it to the total"""
    return sum(int(arg) for arg in argv)


print("3er.metodo : ", convert_add(*list1))
