from math import sqrt
from dataclasses import dataclass


@dataclass
class Star:
    cords: tuple[float, float]


def find_dist(p1: tuple, p2: tuple) -> float:
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def find_center(cluster: list[Star]) -> tuple[float, float]:
    min_sum = float("inf")
    center = cluster[0].cords

    for current_star in cluster:
        current_sum = sum(find_dist(current_star.cords, other_star.cords) for other_star in cluster)
        if current_sum < min_sum:
            min_sum = current_sum
            center = current_star

    return center.cords


a_clusters = [[], []]
b_clusters = [[], [], []]
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

a_clusters.sort(key=lambda cluster: len(cluster))
center_cluster_1 = find_center(a_clusters[0])
center_cluster_2 = find_center(a_clusters[1])
a1 = len([star for star in a_clusters[0] if star.cords[0] <= center_cluster_1[0]])
a2 = find_dist(center_cluster_1, center_cluster_2)

b_clusters.sort(key=lambda cluster: len(cluster))

xc, yc = find_center(b_clusters[1])
b1_count = 0
for star in b_clusters[1]:
    x, y = star.cords
    if xc - 1 <= x <= xc + 1 and yc - 1 <= y <= yc + 1:
        b1_count += 1
b1 = b1_count
b2 = abs(find_center(b_clusters[0])[1] - find_center(b_clusters[-1])[1])

print(a1, int(a2 * 10_000))
print(b1, int(b2 * 10_000))
