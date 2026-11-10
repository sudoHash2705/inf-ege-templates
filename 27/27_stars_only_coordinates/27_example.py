# Источник: kompege.ru
# id задачи: 29979
# В этом примере рассматривается кластеризация
# звёзд ТОЛЬКО с координатами

# Примечание: этот шаблон может быть не актуален в 2027,
# так как с 2027 в 27 задании будет только 1 файл
# и кластеризация будет происходить по кинетической энергии

# Импортируем нужные библиотеки
from math import sqrt
from dataclasses import dataclass


# Дата-класс
@dataclass
class Star:
    cords: tuple[float, float]


# Евклидово расстояние между 2 точками
def find_dist(p1: tuple, p2: tuple) -> float:
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Нахождение центра кластера
def find_center(cluster: list[Star]) -> tuple[float, float]:
    min_sum = float("inf")
    center = cluster[0].cords

    for current_star in cluster:
        # Будем называть центром кластера точку этого кластера,
        # сумма расстояний от которой до всех остальных точек кластера минимальна.
        current_sum = sum(find_dist(current_star.cords, other_star.cords) for other_star in cluster)
        if current_sum < min_sum:
            min_sum = current_sum
            center = current_star

    return center.cords


# В А файле 2 кластера, в Б файле 3 кластера
a_clusters = [[], []]
b_clusters = [[], [], []]
# Итак, перед распределением звёзд по кластерам,
# нам потребуется электронная таблица(неважно какая),
# чтобы построить точечные графики и увидеть как расположены
# кластеры.
# Открываем файлы А и Б и копируем координаты из файлов(убедитесь,
# что x и y находятся в разных столбцах) и строим точеные графики

# После этого уже распределяем звёзды по кластерам
with open("27_A_29979.txt") as a_file, \
        open("27_B_29979.txt") as b_file:
    for line in a_file.readlines():
        parts = line.replace(",", ".").split()
        cords = (float(parts[0]), float(parts[1]))
        if cords[1] < 15:
            a_clusters[0].append(Star(cords))
        else:
            a_clusters[1].append(Star(cords))

    for line in b_file.readlines():
        parts = line.replace(",", ".").split()
        cords = (float(parts[0]), float(parts[1]))
        if cords[0] > 25:
            b_clusters[0].append(Star(cords))
        elif cords[1] < 20:
            b_clusters[1].append(Star(cords))
        else:
            b_clusters[2].append(Star(cords))

# Сортируем кластеры по кол-ву звёзд
a_clusters.sort(key=lambda cluster: len(cluster))
center_cluster_1 = find_center(a_clusters[0])
center_cluster_2 = find_center(a_clusters[1])

# A1 - в кластере с наименьшим количеством точек число точек,
# абсцисса которых не больше абсциссы центра этого кластера
a1 = len([star for star in a_clusters[0] if star.cords[0] <= center_cluster_1[0]])

# А2 - расстояние между центрами кластеров.
a2 = find_dist(center_cluster_1, center_cluster_2)

# Сортируем кластеры по кол-ву звёзд
b_clusters.sort(key=lambda cluster: len(cluster))

xc, yc = find_center(b_clusters[1])
b1_count = 0
for star in b_clusters[1]:
    x, y = star.cords
    if xc - 1 <= x <= xc + 1 and yc - 1 <= y <= yc + 1:
        b1_count += 1
# b1 - в среднем по количеству точек кластере число точек,
# находящихся внутри квадрата с центром в центре этого же кластера,
# сторонами, параллельными координатным осям и длиной 2,0.

# Звучит это очень сложно,
# если простыми словами - в кластере со средним значением звёзд найти ко-во звёзд,
# которые входят в квадрат со стороной 2.0, стороны параллельны осям координат,
# центром квадрата является центр кластера
b1 = b1_count

# b2 - расстояние по оси ординат между центрами кластеров с наименьшим и наибольшим количеством точек.
b2 = abs(find_center(b_clusters[0])[1] - find_center(b_clusters[-1])[1])

# Выводим ответ
print(a1, int(a2 * 10_000))
print(b1, int(b2 * 10_000))
