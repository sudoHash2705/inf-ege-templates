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


result = {}
current_num = START_NUM + 2
while len(result) < 5:
    max_limit = isqrt(current_num) + 1
    for first_divisor in range(3, max_limit, 2):
        if current_num % first_divisor == 0:
            second_divisor = current_num // first_divisor

            if has_one_element(first_divisor, "16") and has_one_element(second_divisor, "16"):
                if is_prime(first_divisor) and is_prime(second_divisor):
                    result[current_num] = first_divisor

            break

    current_num += 2

print(result)
