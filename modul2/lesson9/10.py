my_list = []

for i in range(1001):
    if i % 5 == 0:
        my_list.append(i)

print(my_list)

my_list_two = [x if x % 3 == 0 else -1 for x in range(1001) if x % 5 == 0]
print(my_list_two)