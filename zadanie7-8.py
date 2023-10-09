def multiply_until_one(n):
    while True:
        first_digit = int(str(n)[0])  # Получаем первую цифру числа
        result = n * first_digit      # Умножаем число на первую цифру
        if first_digit == 1 or result >= 1000000000:  # Проверяем условия остановки
            return result
        n = result   # Присваиваем полученный результат переменной n


n = int(input("Введите число: "))  # Ввод числа n
result = multiply_until_one(n)    # Вызов функции
print(result)                     # Вывод результата

