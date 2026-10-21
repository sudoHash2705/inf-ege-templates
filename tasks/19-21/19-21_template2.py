#Выигрышная сумма камней
WIN_S = 133
#кол-во камней в 1 куче
START_S1 = 17

# функция, которая ищет возможные выигрышные стратегии
# Если такие есть, то она вернёт True, если таких нет, то False
def game_perfect(s1: int, s2: int, move: int):
    # Тут стоит обратить внимание на это. Если в задаче игроки УМЕНЬШАЮТ кол-во камней, то знак <=, иначе >=
    if s1 + s2 >= WIN_S:
        return not(move & 1)

    if move == 0:
        return False

    next_move = move - 1
    # Возможные ходы из задачи
    moves = [
        game_perfect(s1 + 4, s2, next_move),
        game_perfect(s1 * 2, s2, next_move),
        game_perfect(s1, s2 + 4, next_move),
        game_perfect(s1, s2 * 2, next_move),
    ]
    # Когда ходит наш игрок, ему не нужно, чтобы абсолютно все его ходы вели к победе. 
    # Ему достаточно найти хотя бы один (any) удачный ход, который гарантированно приведет его к выигрышу. 
    # Если такой ход есть, функция возвращает True

    if not(next_move & 1) == 0:
        return any(moves)
    # Когда ходит соперник, мы не можем контролировать его выбор. Соперник умён и будет пытаться испортить нам игру. 
    # Поэтому наша стратегия будет выигрышной только в том случае, если при любом (all) возможном ходе соперника мы все равно сможем победить. 
    # Если хотя бы при одном своем ходе соперник может нас обыграть, то all() вернет False.
    else:
        return all(moves)

#Итак, в задаче могут быть условия по типу: 'Ваня выиграл после неудачного хода Пети' или 
#'Известно, что Ваня выиграл своим 1 ходом. Укажите <...> S, когда такое возможно'
#В данном случае Петя делет САМЫЙ НЕВЫГОДГНЫЙ для него ход
def game_19_bad_move(s1: int, s2: int, move: int):
    if s1 + s2 >= WIN_S:
        return not(move & 1)

    if move == 0:
        return False

    next_move = move - 1
    moves = [
        game_19_bad_move(s1 + 4, s2, next_move),
        game_19_bad_move(s1 * 2, s2, next_move),
        game_19_bad_move(s1, s2 + 4, next_move),
        game_19_bad_move(s1, s2 * 2, next_move),
    ]
    # Петя делает неудачный ход
    if move == 2:
        return any(moves)

    if not(next_move & 1):
        return any(moves)
    else:
        return all(moves)


answer19 = []
answer20 = []
answer21 = []

for s in range(1, 116):
    # Неудачный ход
    if game_19_bad_move(START_S1, s, 2):
        answer19.append(s)
    # 2 ход Пети, НО не гарантированно выиграть 1 ходом
    if game_perfect(START_S1, s, 3) and not game_perfect(START_S1, s, 1):
        answer20.append(s)
    # 2 ход Вани, НО не гарантированно выиграть своим 1 ходом
    if game_perfect(START_S1, s, 4) and not game_perfect(START_S1, s, 2):
        answer21.append(s)

# Далее если нам нужен МИНИМАЛЬНЫЙ, то указываем индекс 0, а если максимальный, то -1
print(answer19[0])
print(answer20[0], answer20[1])
print(answer21[0])
