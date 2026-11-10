# Источник: kompege.ru
# id задачи: 31371
# В этом примере рассматривается кластеризация
# звёзд со специальными характеристиками.

# Примечание: этот шаблон может быть не актуален в 2027,
# так как с 2027 в 27 задании будет только 1 файл
# и кластеризация будет происходить по кинетической энергии

# Импортируем нужные библиотеки
from math import sqrt
from dataclasses import dataclass
from fnmatch import fnmatch


# Дата-класс
@dataclass
class Star:
    cords: tuple[float, float]
    special_characteristics: str


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
# Открываем файлы А и Б и копируем содержимое из файлов(убедитесь,
# что x и y находятся в разных столбцах), удаляем 3 столбец,
# он нам не нужен для построения точечного графика

# После этого уже распределяем звёзды по кластерам
# Как я распределил кластеры можно посмотреть на скриншотах,
# которые лежат на репозитории
with open("27_A_31371.txt") as a_file, \
        open("27_B_31371.txt") as b_file:
    for line in a_file.readlines():
        parts = line.replace(",", ".").split()
        cords = (float(parts[0]), float(parts[1]))
        special_characteristics = parts[2]
        if cords[1] > 6:
            a_clusters[0].append(Star(cords, special_characteristics))
        else:
            a_clusters[1].append(Star(cords, special_characteristics))

    for line in b_file.readlines():
        parts = line.replace(",", ".").split()
        cords = (float(parts[0]), float(parts[1]))
        special_characteristics = parts[2]
        if cords[1] < 4:
            b_clusters[0].append(Star(cords, special_characteristics))
        elif cords[0] > 8:
            b_clusters[1].append(Star(cords, special_characteristics))
        else:
            b_clusters[2].append(Star(cords, special_characteristics))


center_cluster_1 = find_center(a_clusters[0])
center_cluster_2 = find_center(a_clusters[1])
# А1 - расстояние между центрами кластеров
a1 = find_dist(center_cluster_1, center_cluster_2)

# Находим голубые субкарлики в 1 и 2 кластерах, "O?IV",
# где О - голубой, IV - субкарлик, ? - может стоять любой 1 символ
blue_stars_cluster_1 = [star for star in a_clusters[0] if fnmatch(star.special_characteristics, "O?VI")]
blue_stars_cluster_2 = [star for star in a_clusters[1] if fnmatch(star.special_characteristics, "O?VI")]

# Находим минимальное расстояние между 2 голубыми субкарликами,
# относящихся к разным кластерам
min_dist = float("inf")
for star_1 in blue_stars_cluster_1:
    for star_2 in blue_stars_cluster_2:
        dist = find_dist(star_1.cords, star_2.cords)
        min_dist = min(dist, min_dist)
a2 = min_dist

# Начало координат
start_cords = (0, 0)

# Находим кластер, который наиболее близок к началу координат,
# и кластер, который наиболее удалён от начала координат.
closest_cluster = None
farthest_cluster = None
closest_dist = float("inf")
farthest_dist = float("-inf")
for cluster in b_clusters:
    dist = find_dist(start_cords, find_center(cluster))
    if dist < closest_dist:
        closest_dist = dist
        closest_cluster = cluster
    if dist > farthest_dist:
        farthest_dist = dist
        farthest_cluster = cluster

farthest_center = find_center(farthest_cluster)

# B1 - количество голубых субкарликов в кластере,
# центр которого наиболее близок к началу координат
b1 = len([star for star in closest_cluster if fnmatch(star.special_characteristics, "O?VI")])

# B2 - количество голубых субкарликов,
# находящихся на расстоянии не более 0,9 от центра кластера,
# который наиболее удалён от начала координат.
b2 = len([star for star in farthest_cluster if fnmatch(star.special_characteristics, "O?VI") and
          find_dist(star.cords, farthest_center) <= 0.9])

print(int(a1 * 10_000), int(a2 * 10_000))
print(b1, b2)
