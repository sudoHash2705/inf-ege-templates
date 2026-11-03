# Источник: kompege.ru
# id задачи: 31510

# Создаём функцию с num(текущее число) и target(число,
# которое мы хотим получить)
def f(num: int, target: int) -> int:
    if num == target:
        return 1
    # Мы идём по возрастанию, поэтому, если число больше, чем нам надо, то
    # нам это число не подходит
    if num > target:
        return 0

    # Создаём кол-во 'путей' к числу
    ways = f(num + 1, target)
    str_num = str(num)
    # 'цифра в разряде десятков по значению меньше цифры,
    # стоящей в разряде единиц'
    if str_num[-2] < str_num[-1]:
        new_num = str_num[:-2] + str_num[-1] + str_num[-2]
        ways += f(int(new_num), target)
    return ways


# Выводим ответ
print(f(100, 141))
