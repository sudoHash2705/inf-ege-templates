# Если у вас условие задачи звучит так: 'Значение арифметического выражения <>
# где х - целое положительное число, не превышающее ...',
# то этот шаблон для вас
# Обычно в задаче задаётся система счисления и максимальный x
# Импорт всех прописных букв латинского алфавита
from string import ascii_lowercase

# В некоторых задачах будут системы счисления, в которых будут буквы
# Тут мы инициализируем все возможные буквы
# Далее к ним можно обращаться, например LETTERS['a'], выведет 10
LETTERS = {}
start = 10
for i in range(start, len(ascii_lowercase) + start):
    char = ascii_lowercase[i - 10]
    LETTERS[char] = i

BASE = 7
MAX_X = 2030
# Перевод из 10 в n систему счисления
def to_base_n(num: int, to_base: int) -> list:
    result = []
    while num:
        result.append(num % to_base)
        num //= to_base
    return list(reversed(result))

# Выражение из условия задачи БЕЗ x
expression = (7**170) + (7**100)
# Далее мы перебираем все возможные x
# Если нас справишают минимальный x то пишем 'for x in range(1, MAX_X + 1)'
# Если нас справишают максимальный x то пишем 'for x in range(MAX_X, 0, -1)'
for x in range(MAX_X, 0, -1):
    # Далее пишем условие, указанного в задаче
    # Потом переводим число в n сисему счисления с x
    if to_base_n(expression - x, BASE).count(0) == 70:
        # Выводим ответ
        print(x)
        break
