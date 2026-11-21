# 31423
from enum import Enum


class States(Enum):
    Q_0 = "q0"
    Q_1 = "q1"
    Q_2 = "q2"
    Q_3 = "q3"


class Commands(Enum):
    LEFT = "L"
    RIGHT = "R"
    STOP = "S"


class Symbols(str, Enum):
    ZERO = "0"
    ONE = "1"
    LAMBDA = "l"


INPUT_NUM = 1325
BORDERS = Symbols.LAMBDA * 5
PROGRAMS = {
    # state, symbol: replace_to, command, change_state
    (States.Q_0, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.RIGHT, States.Q_1),
    (States.Q_1, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

    (States.Q_2, Symbols.ZERO): (Symbols.ZERO, Commands.RIGHT, States.Q_2),
    (States.Q_2, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

    (States.Q_3, Symbols.LAMBDA): (Symbols.LAMBDA, Commands.STOP, States.Q_3),
    (States.Q_3, Symbols.ZERO): (Symbols.ONE, Commands.RIGHT, States.Q_2),
    (States.Q_3, Symbols.ONE): (Symbols.ONE, Commands.RIGHT, States.Q_3),

}

binary_num = bin(INPUT_NUM)[2:]
initial_tape = BORDERS + binary_num + BORDERS
tape = {i: Symbols(char) for i, char in enumerate(initial_tape)}
print(tape)

state = States.Q_0
head = len(BORDERS) - 1

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

result_binary = ''.join(
    tape[i] for i in tape if tape[i] != Symbols.LAMBDA
)
print(int(result_binary, 2))
