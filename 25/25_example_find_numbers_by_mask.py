# Источник: kompege.ru
# id задачи: 27778
# В этом примере рассматривается
# прототип задачи - нахождение числа по маске

# Импортируем 'маску'
from fnmatch import fnmatch

# Делитель по условию задачи
DIVISOR = 271
# Числа < этого лимита
LIMIT = 10 ** 8
# Маска числа из задачи
MASK = "12??15*6"

result = {}
for number in range(DIVISOR, LIMIT, DIVISOR):
    if fnmatch(str(number), MASK):
        result[number] = number // DIVISOR

# Выводим ответ
print(result)
