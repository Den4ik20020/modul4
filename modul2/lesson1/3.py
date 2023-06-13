try:
    number = int(input("Введите число "))
    number2 = int(input("Введите число "))
except ValueError as exc:
    print(exc)
    print("Если ошибка ValueError")
except IndentationError:
    print("Если ошибка IndentationError")
else:
    print(number + number2)
finally:
    print("Это точно произойдёт")