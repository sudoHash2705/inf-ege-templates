# Источник: kompege.ru
# id задачи: 31423

# В этом шаблоне рассматривается прототип 12 номера,
# где дано двоичное число и надо найти число, которое получилось
# после обработки какого-то алгоритма и записать его
# в 10 системе счисления

# Для того чтобы 'отобразить' алгоритм из условия задачи, нам
# понадобится класс Enum
from enum import Enum


# Класс состояний(может больше или меньше чем здесь!)
class States(Enum):
    Q_0 = "q0"
    Q_1 = "q1"
    Q_2 = "q2"
    Q_3 = "q3"


# Команды алгоритма
class Commands(Enum):
    LEFT = "L"
    RIGHT = "R"
    STOP = "S"


# Символы из условия задачи(могут быть другие!)
class Symbols(str, Enum):
    ZERO = "0"
    ONE = "1"
    LAMBDA = "l"


# Число из условия задачи
INPUT_NUM = 1325
# 'Границы числа', по условию задачи их бесконечно много, но
# нам будет достаточно 5
BORDERS = Symbols.LAMBDA * 5
# Вот тут мы и переносим алгоритм из условия задачи
PROGRAMS = {
    # (Текущее состояние, ткущий символ головки): (на что заменить символ, куда сдвигаться, на какое состояние поменять)
    (States.Q_0, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.RIGHT, States.Q_1),
    (States.Q_1, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

    (States.Q_2, Symbols.ZERO): (Symbols.ZERO, Commands.RIGHT, States.Q_2),
    (States.Q_2, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

    (States.Q_3, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.STOP, States.Q_3),
    (States.Q_3, Symbols.ZERO): (Symbols.ONE, Commands.RIGHT, States.Q_2),
    (States.Q_3, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

}
# Переводим число в двоичную систему счисления
binary_num = bin(INPUT_NUM)[2:]
# тут мы добавляем к числу границы и виде лямбд
initial_tape = BORDERS + binary_num + BORDERS
# Тут мы разбиваем каждый символ на отдельные индексы начиная с 0
tape = {i: Symbols(char) for i, char in enumerate(initial_tape)}

# Текущее состояние алгоритма
state = States.Q_0
# В начальный момент времени головка расположена в
# ближайшей слева к последовательности ячейке.
head = len(BORDERS) - 1

while True:
    # Если индекс вдруг вышел за пределы границ,
    # то выбрасываем исключение, чтобы найти ошибку
    if head < 0 or head >= len(tape):
        raise ValueError("HEAD cannot be < 0 or >= length tape")

    # Получаем текущий символ
    current_symbol = tape.get(head, Symbols.LAMBDA)
    # Получаем новый символ, команду и новое состояние
    new_symbol, command, new_state = PROGRAMS[(state, current_symbol)]

    # Заменяем символ
    tape[head] = new_symbol
    # Меняем состояние
    state = new_state

    # Сдвигаем головку
    if command == Commands.LEFT:
        head -= 1
    elif command == Commands.RIGHT:
        head += 1
    elif command == Commands.STOP:
        break

# Выводим ответ
result_binary = ''.join(
    tape[i] for i in tape if tape[i] != Symbols.LAMBDA
)
print(int(result_binary, 2))
