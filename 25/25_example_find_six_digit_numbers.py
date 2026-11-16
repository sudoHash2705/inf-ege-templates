# kompege
# 29938
START_NUM = 99_999
END_NUM = 1_000_000
DIVISOR = 197


def find_valid_power(n: int) -> int | None:
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
    if str(current_num).count("1") != 0:
        continue

    power = find_valid_power(current_num)
    if power:
        result[current_num] = power

    if len(result) == 7:
        break

print(result)
