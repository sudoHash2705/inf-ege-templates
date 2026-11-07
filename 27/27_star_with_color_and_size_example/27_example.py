from math import sqrt
from dataclasses import dataclass
from fnmatch import fnmatch


@dataclass
class Star:
    cords: tuple[float, float]
    special_characteristics: str


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
a1 = find_dist(center_cluster_1, center_cluster_2)

blue_stars_cluster_1 = [star for star in a_clusters[0] if fnmatch(star.special_characteristics, "O?VI")]
blue_stars_cluster_2 = [star for star in a_clusters[1] if fnmatch(star.special_characteristics, "O?VI")]

min_dist = float("inf")
for star_1 in blue_stars_cluster_1:
    for star_2 in blue_stars_cluster_2:
        dist = find_dist(star_1.cords, star_2.cords)
        if dist < min_dist:
            min_dist = dist

a2 = min_dist

closest_cluster = b_clusters[0]
closest_dist = find_dist((0, 0), find_center(closest_cluster))
for cluster in b_clusters[1:]:
    dist = find_dist((0, 0), find_center(cluster))
    if dist < closest_dist:
        closest_dist = dist
        closest_cluster = cluster

farthest_cluster = b_clusters[0]
farthest_dist = find_dist((0, 0), find_center(closest_cluster))
for cluster in b_clusters[1:]:
    dist = find_dist((0, 0), find_center(cluster))
    if dist > farthest_dist:
        farthest_dist = dist
        farthest_cluster = cluster
farthest_center = find_center(farthest_cluster)

b1 = len([star for star in closest_cluster if fnmatch(star.special_characteristics, "O?VI")])
b2 = len([star for star in farthest_cluster if fnmatch(star.special_characteristics, "O?VI") and
          find_dist(star.cords, farthest_center) <= 0.9])

print(int(a1 * 10_000), int(a2 * 10_000))
print(b1, b2)
