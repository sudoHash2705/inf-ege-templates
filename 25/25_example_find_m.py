# Источник: kompege.ru
# id задачи: 31161
# В этом примере рассматривается прототип задачи - нахождение M

# Импортируем isqrt - ищет ближайший квадрат числа
# Пример isqrt(2) -> 1
# isqrt(5) -> 2
from math import isqrt

# Начальное число по условию задачи
START_NUM = 8_117_600_756


# Алгоритм проверки, простое ли это число
def is_prime(n: int) -> bool:
    # 1 и меньше числа не являются простыми числами
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    # Чётные числа не являются простыми(кроме 2, но мы это учли выше)
    if n % 2 == 0:
        return False

    # Проверяем нечётные делители до квадрата исходного числа + 1
    limit = isqrt(n) + 1
    return all(n % i != 0 for i in range(3, limit, 2))


# Пусть М - разность максимального и минимального простых натуральных делителей
# целого числа, не считая самого числа
def find_m(n: int) -> int:
    divisors = []

    if n % 2 == 0:
        divisors.append(2)
        while n % 2 == 0:
            n //= 2

    # Здесь представлен алгоритм нахождения простых делителей
    factor = 3
    # умножение НАМНОГО быстрее, чем возведение в степень
    while factor * factor <= n:
        if n % factor == 0:
            divisors.append(factor)
            while n % factor == 0:
                n //= factor
        factor += 2

    if n > 1:
        divisors.append(n)

    # Если таких делителей у числа нет, то значение М считается равным нулю.
    if len(divisors) < 2:
        return 0

    # Разность максимального и минимального делителей
    return divisors[-1] - divisors[0]


# Проверяем числа > START_NUM
current_num = START_NUM + 1
result = {}
# Находим первые пть чисел
while len(result) < 5:
    m = find_m(current_num)
    # M должно быть простым и содержать не менее 4 единиц
    if is_prime(m) and str(m).count("1") >= 4:
        result[current_num] = m

    current_num += 1

# Выводим ответ
print(result)
