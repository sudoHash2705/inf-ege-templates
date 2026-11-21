# 25302
from enum import Enum


class States(Enum):
    Q_0 = "q0"
    Q_1 = "q1"


class Commands(Enum):
    LEFT = "L"
    RIGHT = "R"
    STOP = "S"


class Symbols(str, Enum):
    ZERO = "0"
    ONE = "1"
    LAMBDA = "l"


BORDERS = Symbols.LAMBDA * 5
SYMBOLS_COUNT = 800
TARGET_SYMBOLS_COUNT = 420
PROGRAMS = {
    (States.Q_0, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.LEFT, States.Q_1),
    (States.Q_1, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.STOP, States.Q_1),
    (States.Q_1, Symbols.ZERO): (Symbols.ZERO, Commands.LEFT, States.Q_1),
    (States.Q_1, Symbols.ONE): (Symbols.ONE, Commands.STOP, States.Q_1),
}


def find_remaining_symbols(seq: str, find_symbol: Symbols) -> int:
    initial_tape = BORDERS + seq + BORDERS
    tape = {i: Symbols(ch) for i, ch in enumerate(initial_tape)}
    state = States.Q_0
    head = len(initial_tape) - len(BORDERS)

    while True:
        if head < 0 or head >= len(tape):
            raise ValueError("HEAD cannot be < 0 or >= length tape")

        current_symbol = tape.get(head, Symbols.LAMBDA)
        new_symbol, command, new_state = PROGRAMS[(state, current_symbol)]
        tape[head] = new_symbol
        state = new_state

        if command == Commands.LEFT:
            head -= 1
        elif command == Commands.RIGHT:
            head += 1
        elif command == Commands.STOP:
            break

    return sum(1 for val in tape.values() if val == find_symbol)


max_zeros = float("-inf")
for zeros in range(SYMBOLS_COUNT, -1, -1):
    ones = SYMBOLS_COUNT - zeros
    sequence = Symbols.ONE * ones + Symbols.ZERO * zeros
    if find_remaining_symbols(sequence, Symbols.ONE) == TARGET_SYMBOLS_COUNT:
        max_zeros = max(max_zeros, zeros)

print(max_zeros)
