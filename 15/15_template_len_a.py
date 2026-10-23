# Итак, если вам нужно нафти длинну отрека,
# то этот шаблон для вас
# Инициализируем точки в промежутке от 0 до 6000 с шагом в 0.5
POINTS = [i * 0.5 for i in range(6000)]

# Далее в задаче будут отмечены промеутки,
# например, B = [100, 340], C = [50, 65] и т д
# соответвенно пишем функцию у указываем
# 'return "начало промежутка" <= n <= "конец промежутка" '
# и по такому принципу пишем другие
def in_b(n: float) -> bool:
    return True


def in_c(n: float) -> bool:
    return True

# Главная функция, где будет логичекое условие из задачи
def f(x: float, a_flag: bool) -> bool:
    return True

# Тут мы указываем максимальная или минимальная длинна нам нужна
is_max_len = True
x_in_a = is_max_len
# принимает при любых значениях 0 или 1
is_true_for_any_x = True
# Результат
result_points = []
for x in POINTS:
    if is_max_len:
       if f(x, x_in_a) is is_true_for_any_x:
           result_points.append(x)
    else:
        if f(x, x_in_a) is not is_true_for_any_x:
           result_points.append(x)

# Вычисляем длинну отрезка
print(max(result_points) - min(result_points))
