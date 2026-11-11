# Источник: kompege.ru
# id задачи: 31371
# В этом примере рассматривается кластеризация
# звёзд со специальными характеристиками.

# Примечание: этот шаблон может быть не актуален в 2027,
# так как с 2027 в 27 задании будет только 1 файл
# и кластеризация будет происходить по кинетической энергии

# Импортируем нужные библиотеки
from dataclasses import dataclass
from fnmatch import fnmatch
from math import dist


# Дата-класс
@dataclass
class Star:
    x: float
    y: float
    special_characteristics: str


# Нахождение центра кластера
def find_center(cluster: list[Star]) -> Star:
    min_sum = float("inf")
    center = None

    for current_star in cluster:
        # Будем называть центром кластера точку этого кластера,
        # сумма расстояний от которой до всех остальных точек кластера минимальна.
        current_sum = sum(dist((current_star.x, current_star.y),
                               (other_star.x, other_star.y)) for other_star in cluster)
        if current_sum < min_sum:
            min_sum = current_sum
            center = current_star

    return center


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
    for line in a_file:
        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        special_characteristics = parts[2]
        if y > 6:
            a_clusters[0].append(Star(x, y, special_characteristics))
        else:
            a_clusters[1].append(Star(x, y, special_characteristics))

    for line in b_file:
        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        special_characteristics = parts[2]
        if y < 4:
            b_clusters[0].append(Star(x, y, special_characteristics))
        elif x > 8:
            b_clusters[1].append(Star(x, y, special_characteristics))
        else:
            b_clusters[2].append(Star(x, y, special_characteristics))


center_cluster_1 = find_center(a_clusters[0])
center_cluster_2 = find_center(a_clusters[1])
# А1 - расстояние между центрами кластеров
a1 = dist((center_cluster_1.x, center_cluster_1.y),
          (center_cluster_2.x, center_cluster_2.y))

# Находим голубые субкарлики в 1 и 2 кластерах, "O?IV",
# где О - голубой, IV - субкарлик, ? - может стоять любой 1 символ
blue_stars_cluster_1 = [star for star in a_clusters[0] if fnmatch(star.special_characteristics, "O?VI")]
blue_stars_cluster_2 = [star for star in a_clusters[1] if fnmatch(star.special_characteristics, "O?VI")]

# Находим минимальное расстояние между 2 голубыми субкарликами,
# относящихся к разным кластерам
min_dist = float("inf")
for star_1 in blue_stars_cluster_1:
    for star_2 in blue_stars_cluster_2:
        p1 = (star_1.x, star_1.y)
        p2 = (star_2.x, star_2.y)
        min_dist = min(dist(p1, p2), min_dist)
a2 = min_dist

# Начало координат
start_coords = (0, 0)

# Находим кластер, который наиболее близок к началу координат,
# и кластер, который наиболее удалён от начала координат.
closest_cluster = None
farthest_cluster = None
closest_dist = float("inf")
farthest_dist = float("-inf")
for cluster in b_clusters:
    current_center = find_center(cluster)
    distance = dist(start_coords, (current_center.x, current_center.y))
    if distance < closest_dist:
        closest_dist = distance
        closest_cluster = cluster
    if distance > farthest_dist:
        farthest_dist = distance
        farthest_cluster = cluster

farthest_center = find_center(farthest_cluster)

# B1 - количество голубых субкарликов в кластере,
# центр которого наиболее близок к началу координат
b1 = len([star for star in closest_cluster if fnmatch(star.special_characteristics, "O?VI")])

# B2 - количество голубых субкарликов,
# находящихся на расстоянии не более 0,9 от центра кластера,
# который наиболее удалён от начала координат.
b2 = len([star for star in farthest_cluster if fnmatch(star.special_characteristics, "O?VI") and
          dist((star.x, star.y), (farthest_center.x, farthest_center.y)) <= 0.9])

print(int(a1 * 10_000), int(a2 * 10_000))
print(b1, b2)
