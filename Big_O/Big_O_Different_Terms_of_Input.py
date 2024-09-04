def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)
print_items(5, 6)

def print_items_nested(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)
print_items_nested(5, 6)