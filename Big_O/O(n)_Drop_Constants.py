#Although it is running n+n times, we can asssume that the time complexity be O(2n).
#But for this case we drop the constants and the complexity will be O(n).

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)