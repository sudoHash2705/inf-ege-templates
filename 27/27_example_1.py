# Источник: kompege.ru
# id задачи: 31521
# В этом примере рассматривается 27 задание из демоверсии 2027 ЕГЭ
# по информатике

# Импортируем нужные библиотеки
# Дата-класс
from dataclasses import dataclass
# Евклидово расстояние между 2 точками
from math import dist

# Задаём константы из условия задачи
# Тут представлены все разряды римских цифр, но на экзамене(скорее всего)
# будет достаточно от I до X
# ROMAN_MAP = {"I": 1, "V": 5, "X": 10}
ROMAN_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# Максимальный модуль разности кинетических энергий любых двух частиц
MAX_R = 2.0
# Кол-во кластеров
CLUSTERS_COUNT = 4


# Делаем дата-класс звезды
@dataclass
class Star:
    x: float
    y: float
    vx: float
    vy: float
    m: float
    special_characteristic: int

    def get_kinetic_energy(self) -> float:
        return 0.5 * self.m * (self.vx ** 2 + self.vy ** 2)


# Алгоритм перевода из римского числа в десятичное
def from_roman(roman_num: str) -> int:
    result = 0
    length = len(roman_num)

    for i in range(length):
        if i + 1 < length and ROMAN_MAP[roman_num[i]] < ROMAN_MAP[roman_num[i + 1]]:
            result -= ROMAN_MAP[roman_num[i]]
        else:
            result += ROMAN_MAP[roman_num[i]]

    return result


# Алгоритм нахождения центра
def find_center(cluster: list[Star]) -> Star:
    center = None
    min_sum_diff = float('inf')

    for current_star in cluster:
        # "Будем называть центром кластера такую его частицу,
        # для которой сумма модулей разности кинетических
        # энергий со всеми остальными частицами этого кластера минимальна."
        sum_diff = sum(
            abs(current_star.get_kinetic_energy() - other_star.get_kinetic_energy()) for other_star in cluster)
        if sum_diff < min_sum_diff:
            min_sum_diff = sum_diff
            center = current_star
    return center


stars = []
# Открываем файл
with open("27_31521.txt") as file:
    for line in file:
        if not line.strip():
            continue

        # Обязательно заменяем , на .
        # Иначе будет ошибка
        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        vx = float(parts[2])
        vy = float(parts[3])
        m = float(parts[4])
        roman_n = parts[5]
        stars.append(Star(x, y, vx, vy, m, from_roman(roman_n)))

    # Сортируем звёзды в порядке возрастания их кинетической энергии
    stars.sort(key=lambda star: star.get_kinetic_energy())

clusters = []
current_cluster = [stars[0]]

# Далее раскидываем звёзды по кластерам
for star in stars[1:]:
    # Если разность кинетических энергий > R, то начинается новый кластер
    if star.get_kinetic_energy() - current_cluster[0].get_kinetic_energy() > MAX_R:
        clusters.append(current_cluster)
        current_cluster = [star]
    else:
        current_cluster.append(star)
clusters.append(current_cluster)

# Если число кластеров не равно числу, указанного в задаче, то выкидываем исключение,
# чтобы себя проверить
if len(clusters) != CLUSTERS_COUNT:
    raise ValueError(f"Clusters count doesn't equal {CLUSTERS_COUNT}")

# Центры кластеров
centers_e = []
# Максимальное расстояние между 2 звёздами, которые имеют признак II(2)
max_dist_sign2 = 0.0

for cluster in clusters:
    centers_e.append(find_center(cluster).get_kinetic_energy())

    stars_special_characteristic_2 = [particle for particle in cluster if particle.special_characteristic == 2]

    for i in range(len(stars_special_characteristic_2)):
        for j in range(i + 1, len(stars_special_characteristic_2)):
            star1 = stars_special_characteristic_2[i]
            star2 = stars_special_characteristic_2[j]
            distance = dist((star1.x, star1.y), (star2.x, star2.y))
            max_dist_sign2 = max(distance, max_dist_sign2)
            
# Q1 – наибольшее евклидово расстояние между частицами одного кластера, имеющими признак II
q1 = max_dist_sign2
# Q2 – максимальное значение кинетической энергии для центра кластера.
q2 = max(centers_e)

# Выводим ответ
print(int(q1 * 10000), int(q2 * 10000))
