# Источник: kompege.ru
# id задачи: 31519

# Импортируем isqrt - ищет ближайший квадрат числа
# Пример isqrt(2) -> 1
# isqrt(5) -> 2
from math import isqrt

# Начальное число по условию задачи
START_NUM = 1_103_285_717


# Алгоритм проверки, простое ли это число
def is_prime(n: int) -> bool:
    # 1 и меньше числа не являются простыми числами
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    # Чётные числа не являются простыми(кроме 2, но мы это учли выше)
    # & 1 альтернатива % 2
    if not (n & 1):
        return False

    # Проверяем нечётные делители до квадрата исходного числа + 1
    limit = isqrt(n) + 1
    return all(n % i != 0 for i in range(3, limit, 2))
    # for i in range(3, limit, 2):
    #     if n % i == 0:
    #         return False
    #
    # return True


def has_one_element(n: int, element: str) -> bool:
    return str(n).count(element) == 1


# Эта функция пытается представить число в виде произведения
# двух простых чисел, в записи которых '16' встречается 1 раз
def find_prime_divisors(n: int) -> tuple[int, int] | None:
    # Такие большие чётные числа нельзя представить
    # в виде произведения двух простых чисел
    if not (n & 1):
        return None

    max_limit = isqrt(n) + 1
    for first_divisor in range(3, max_limit, 2):
        # Находим 1 делитель
        if n % first_divisor == 0:
            # Находим второй делитель
            second_divisor = n // first_divisor

            # Если в каком-то числе '16' содержится > 1 раза,
            # то такие числа нам не подходят
            if not has_one_element(first_divisor, "16") or \
                    not has_one_element(second_divisor, "16"):
                break

            # Если какое-то число не простое,
            # то такие числа нам не подходят
            if not is_prime(first_divisor) or \
                    not is_prime(second_divisor):
                break

            return first_divisor, second_divisor

    return None


result = {}
current_num = START_NUM + 1
# Находим первые 5 чисел
while len(result) < 5:
    divisors = find_prime_divisors(current_num)
    # Если такие делители существуют
    if divisors:
        # В ответе нужно записать число и наименьший делитель
        result[current_num] = min(divisors)
    current_num += 1

# Выводим ответ
print(result)
