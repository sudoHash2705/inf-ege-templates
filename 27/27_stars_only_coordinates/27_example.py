# Источник: kompege.ru
# id задачи: 29979
# В этом примере рассматривается кластеризация
# звёзд ТОЛЬКО с координатами

# Примечание: этот шаблон может быть не актуален в 2027,
# так как с 2027 в 27 задании будет только 1 файл
# и кластеризация будет происходить по кинетической энергии

# Импортируем нужные библиотеки
from dataclasses import dataclass
from math import dist


# Дата-класс
@dataclass
class Star:
    x: float
    y: float


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
# Открываем файлы А и Б и копируем координаты из файлов(убедитесь,
# что x и y находятся в разных столбцах) и строим точеные графики

# После этого уже распределяем звёзды по кластерам
# Как я распределил кластеры можно посмотреть на скриншотах,
# которые лежат на репозитории
with open("27_A_29979.txt") as a_file, \
        open("27_B_29979.txt") as b_file:
    for line in a_file:
        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        if y < 15:
            a_clusters[0].append(Star(x, y))
        else:
            a_clusters[1].append(Star(x, y))

    for line in b_file:
        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        if x > 25:
            b_clusters[0].append(Star(x, y))
        elif y < 25:
            b_clusters[1].append(Star(x, y))
        else:
            b_clusters[2].append(Star(x, y))

# Сортируем кластеры по кол-ву звёзд
a_clusters.sort(key=lambda cluster: len(cluster))
center_cluster_1 = find_center(a_clusters[0])
center_cluster_2 = find_center(a_clusters[1])

# A1 - в кластере с наименьшим количеством точек число точек,
# абсцисса которых не больше абсциссы центра этого кластера
a1 = len([star for star in a_clusters[0] if star.x <= center_cluster_1.x])

# А2 - расстояние между центрами кластеров.
a2 = dist((center_cluster_1.x, center_cluster_1.y), (center_cluster_2.x, center_cluster_2.y))

# Сортируем кластеры по кол-ву звёзд
b_clusters.sort(key=lambda cluster: len(cluster))

center_star = find_center(b_clusters[1])
b1_count = 0
for star in b_clusters[1]:
    if (center_star.x - 1 <= star.x <= center_star.x + 1) and \
            (center_star.y - 1 <= star.y <= center_star.y + 1):
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
b2 = abs(find_center(b_clusters[0]).y - find_center(b_clusters[-1]).y)

# Выводим ответ
print(a1, int(a2 * 10_000))
print(b1, int(b2 * 10_000))
