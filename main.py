

# 1st program
result = 9 ** 0.5 * 5
print(result)

# 2nd program
result = 9.99 > 9.98 and 1000 != 1000.1
print(result)


# 3rd program
no_priority = 2 * 2 + 2  # Умножение выполняется перед сложением
with_priority = 2 * (2 + 2)  # Сначала выполняем сложение в скобках
comparison_result = no_priority == with_priority

print(no_priority)
print(with_priority)
print(comparison_result)


# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10, смещаем запятую
first_digit_after_decimal = int(shifted_number) % 10  # Берем остаток от деления на 10

print(first_digit_after_decimal)  # Выводим первую цифру после запятой
