# Источник: kompege.ru
# id задачи: 29977 

# Создаём функцию с num(текущее число),
# target(число, которое мы хотим получить, и exclude_num(число, которое мы НЕ хотим включать в
# траекторию вычислений
def f(num: int, target: int, exclude_num: int = -1) -> int:
    if num == target:
        return 1
    # Если число меньше чем 'target' или число равняется 'exclude_num',
    # то возвращаем 0
    if num < target or num == exclude_num:
        return 0

    return f(num - 1, target, exclude_num) + \
        f(num - 3, target, exclude_num) + \
        f(num // 2, target, exclude_num)


# Мы хотим включить число 12 в траекторию вычислений, поэтому применяем правило
# умножения как в комбинаторике и выводим ответ
print(f(19, 12) * f(12, 3, 9))
