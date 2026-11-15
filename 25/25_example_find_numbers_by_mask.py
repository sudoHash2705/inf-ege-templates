# komgege
# 27778
from fnmatch import fnmatch


DIVISOR = 271
LIMIT = 10 ** 8
MASK = "12??15*6"

result = {}
for number in range(DIVISOR, LIMIT, DIVISOR):
    if fnmatch(str(number), MASK):
        result[number] = number // DIVISOR

print(result)
