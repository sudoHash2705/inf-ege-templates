# kompege
# 31161
from math import isqrt


START_NUM = 8_117_600_756


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if not (n & 1):
        return False

    limit = isqrt(n) + 1

    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


def find_m(n: int) -> int:
    if n < 2:
        return 0

    divisors = []

    if not (n & 1):
        divisors.append(2)
        while not n & 1:
            # n //= 2
            n >>= 1

    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            divisors.append(factor)
            while n % factor == 0:
                n //= factor
        factor += 2

    if n > 1:
        divisors.append(n)

    if len(divisors) < 2:
        return 0

    return sum(divisors[-2:])


current_num = START_NUM + 1
result = {}
while len(result) < 5:
    m = find_m(current_num)
    if is_prime(m) and str(m).count("1") >= 4:
        result[current_num] = m

    current_num += 1

print(result)
