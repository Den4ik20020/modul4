list_one = []
list_two = []

for i in range(1, 11):
    a = int(input(f"Введите число под номером {i}: "))
    if a % 2 == 0:
        list_one.append(a)
    else:
        list_two.append(a)

print(f"Вы ввели четные числа: {list_one} ")
print(f"Вы ввели не четные числа: {list_two} ")
