# Источник: kompege.ru
# id задачи: 29938

# Все шестизначные числа
START_NUM = 99_999
END_NUM = 1_000_000

# делитель по условию задачи
DIVISOR = 197


# Число нужно представить в виде степени 5 и чётного числа
# Например 29 можно представить в виде 5**2 + 4
# В этой функции мы это проверяем и возвращаем степень
def find_valid_power_five(n: int) -> int | None:
    current_power = 1
    while 5 ** current_power < n:
        remainder = n - 5 ** current_power
        if not (remainder & 1) and remainder > 0 and \
                remainder % DIVISOR == 0:
            return current_power
        current_power += 1

    return None


result = {}
for current_num in range(START_NUM + 1, END_NUM):
    # Нам нужны числа не имеющие в своей записи 1
    if str(current_num).count("1") != 0:
        continue

    power = find_valid_power_five(current_num)
    if power:
        result[current_num] = power

    # Если нашлись первые 7 чисел, выходим из цикла
    if len(result) == 7:
        break

# Выводим ответ
print(result)
