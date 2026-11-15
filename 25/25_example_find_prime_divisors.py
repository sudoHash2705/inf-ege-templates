# kompege.ru
# 31519

from math import isqrt

START_NUM = 1_103_285_717


def is_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True

    if n <= 1 or not (n & 1):
        return False

    limit = isqrt(n) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


def has_one_element(n: int, element: str) -> bool:
    return str(n).count(element) == 1


def find_prime_divisors(n: int) -> tuple[int, int] | None:
    if not (n & 1):
        return None

    max_limit = isqrt(n) + 1
    for first_divisor in range(3, max_limit, 2):
        if n % first_divisor == 0:
            second_divisor = n // first_divisor

            if not has_one_element(first_divisor, "16") or \
                    not has_one_element(second_divisor, "16"):
                break

            if not is_prime(first_divisor) or \
                    not is_prime(second_divisor):
                break

            return first_divisor, second_divisor

    return None


result = {}
current_num = START_NUM + 1
while len(result) < 5:
    divisors = find_prime_divisors(current_num)
    if divisors:
        result[current_num] = min(divisors)
    current_num += 1

print(result)
