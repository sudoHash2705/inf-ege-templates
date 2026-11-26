# Источник: kompege.ru
# id задачи: 25302

# В этом шаблоне рассматривается прототип 12 номера,
# где дано кол-во символов в строке, конечное число(0 или 1)
# после выполнения какого-то алгоритма. Нужно найти
# максимальное кол-во 0 или 1 в исходной строке

# Для того чтобы 'отобразить' алгоритм из условия задачи, нам
# понадобится класс Enum

# Почему Enum? Если вы будете решать кодом 12 номер на ЕГЭ,
# когда вы будете писать алгоритм из условия задачи, то есть шанс
# ошибиться, поэтому лучше обращаться к элементам из Enum
from enum import Enum


# Класс состояний(может больше или меньше состояний чем здесь!)
class States(Enum):
    Q_0 = "q0"
    Q_1 = "q1"


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


# 'Границы числа', по условию задачи их бесконечно много, но
# нам будет достаточно 5
BORDERS = Symbols.LAMBDA * 5
# Кол-во символов из условия задачи
SYMBOLS_COUNT = 800
# Сколько символов(именно 0 или 1) осталось после выполнения алгоритма
TARGET_SYMBOLS_COUNT = 420
# Вот тут мы и переносим алгоритм из условия задачи
PROGRAMS = {
    # (Текущее состояние, ткущий символ головки): (на что заменить символ, куда сдвигаться, на какое состояние поменять)
    (States.Q_0, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.LEFT, States.Q_1),
    (States.Q_1, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.STOP, States.Q_1),
    (States.Q_1, Symbols.ZERO): (Symbols.ZERO, Commands.LEFT, States.Q_1),
    (States.Q_1, Symbols.ONE): (Symbols.ONE, Commands.STOP, States.Q_1),
}


def find_remaining_symbols(seq: str, find_symbol: Symbols) -> int:
    initial_tape = BORDERS + seq + BORDERS
    # Тут мы разбиваем нашу строку на символы, у каждого символа
    # свой индекс, начиная с 0
    tape = {i: Symbols(ch) for i, ch in enumerate(initial_tape)}
    # Текущее состояние алгоритма
    current_state = States.Q_0
    # В начальный момент времени головка расположена в
    # ближайшей ячейке справа от последовательности.
    head = len(initial_tape) - len(BORDERS)

    while True:
        # Если индекс вдруг вышел за пределы границ,
        # то выбрасываем исключение, чтобы найти ошибку
        if head < 0 or head >= len(tape):
            raise ValueError("HEAD cannot be < 0 or >= length tape")

        # Получаем текущий символ
        current_symbol = tape.get(head, Symbols.LAMBDA)
        # Получаем новый символ, команду и новое состояние
        new_symbol, command, new_state = PROGRAMS[(current_state, current_symbol)]

        # Заменяем символ
        tape[head] = new_symbol
        # Меняем состояние
        current_state = new_state

        # Сдвигаем головку
        if command == Commands.LEFT:
            head -= 1
        elif command == Commands.RIGHT:
            head += 1
        elif command == Commands.STOP:
            break

    return sum(1 for val in tape.values() if val == find_symbol)


result_count = float("-inf")
# В цикле мы перебираем кл-во того, что нам нужно найти
# В данном случае это нули.
# Идём в порядке убывания, так как нас просят МАКСИМАЛЬНОЕ кол-во
for zeros in range(SYMBOLS_COUNT, -1, -1):
    ones = SYMBOLS_COUNT - zeros
    # Тут мы пишем последовательность из 0 и 1. Единой последовательности,
    # которая решает все прототипы этого номера нет, но вот
    # на что стоит обратить внимание при решении таких прототипов:

    # 1) Надо посмотреть, на каком символе программа останавливается,
    # КРОМЕ ЛЯМБД.

    # 2) Так как нам нужно максимальное кол-во нулей или единиц, то
    # В большинстве случаев сначала идут те символы,
    # которые прерывают программу, а потом — символы,
    # которые программу не прерывают(но всё равно лучше всё перепроверить 1000 раз).
    #
    # 3) Ну и наконец, записать эту последовательность из нулей и единиц.
    #
    sequence = Symbols.ONE * ones + Symbols.ZERO * zeros
    # Если нашли, прерываем цикл
    if find_remaining_symbols(sequence, Symbols.ONE) == TARGET_SYMBOLS_COUNT:
        result_count = zeros
        break

# Выводим ответ
print(result_count)
