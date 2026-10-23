# Итак, если у вас задачи такого рода: 'Операнды арифметического
# выражения записаны в системе счисления с основанием ...' То это именно тот шаблон,
# который вам нужен

# Импорт всех прописных букв латинского алфавита
from string import ascii_lowercase

# Смотрим, какая система счисления указана в задаче
BASE = 22
# Смотрим, какой делитель в задаче
DIVISOR = 21

# В некоторых задачах будут системы счисления, в которых будут буквы
# Тут мы инициализируем все возможные буквы
# Далее к ним можно обращаться, например LETTERS['a'], выведет 10
LETTERS = {}
start = 10
for i in range(start, len(ascii_lowercase) + start):
    char = ascii_lowercase[i - 10]
    LETTERS[char] = i

# Функция, которая переводит из любой системы в 10
def to_dec(num: list, from_base: int) -> int:
    num_10 = 0
    for i, digit in enumerate(reversed(num)):
        # Если у вас вдруг есть число, которое больше, чем система счисления
        # или равна ей, то будет исключение
        if digit >= from_base:
            raise ValueError(f"{digit} is bigger than number base: {from_base}")
        num_10 += digit * (from_base ** i)
    return num_10

# Далее мы ищем x. Он ДОЛЖЕН быть меньше, чем система счисления
# Если нам нужно найти минимальный x то пишем 'for x in range(BASE)'
# Если нам нужно найти максимальный x, то пишем 'for x in range(BASE - 1, -1, -1)'
for x in range(BASE):
    expression = to_dec([2, 7, x, 9, 8, 8, 7, 6], BASE) + \
                 to_dec([2, 6, x, 5, 1], BASE) + \
                 to_dec([7, 1, 1, x, 5], BASE)
    # Далее нам нужно найти такой x, чтобы выражение делилось без остатка
    if expression % DIVISOR == 0:
        # Выводим ответ
        print(expression / DIVISOR)
        break
    
