list1 = ["1", "2", "3"]
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(sum(list1)) 

def convert_add(*argv) -> None:
    """Converts a string to a float and adds it to the total"""
    for i in range(len(*argv)):
        lis[i] = int(argv[i])

#list1 = ["1", "2", "3"]
print("hola")
print(convert_add("1", "2", "3"))