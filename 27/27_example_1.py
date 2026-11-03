from dataclasses import dataclass, field
from math import sqrt

ROMAN_MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
MAX_R = 2.0
MAX_CLUSTER_COUNT = 4


@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    m: float
    special_characteristic: int
    kinetic_energy: float = field(init=False)

    def __post_init__(self):
        self.kinetic_energy = 0.5 * self.m * (self.vx ** 2 + self.vy ** 2)


def from_roman(roman_num: str) -> int:
    result = 0
    length = len(roman_num)

    for i in range(length):
        if i + 1 < length and ROMAN_MAP[roman_num[i]] < ROMAN_MAP[roman_num[i + 1]]:
            result -= ROMAN_MAP[roman_num[i]]
        else:
            result += ROMAN_MAP[roman_num[i]]

    return result


def find_min_dist(cluster: list[Particle]) -> float:
    center = None
    min_sum_diff = float('inf')

    for current_particle in cluster:
        sum_diff = sum(
            abs(current_particle.kinetic_energy - other_particle.kinetic_energy) for other_particle in cluster)
        if sum_diff < min_sum_diff:
            min_sum_diff = sum_diff
            center = current_particle
    return center.kinetic_energy


particles = []
with open("27_31521.txt") as file:
    for line in file.readlines():
        if not line.strip():
            continue

        parts = line.replace(",", ".").split()
        x = float(parts[0])
        y = float(parts[1])
        vx = float(parts[2])
        vy = float(parts[3])
        m = float(parts[4])
        roman_n = parts[5]
        particles.append(Particle(x, y, vx, vy, m, from_roman(roman_n)))

    particles.sort(key=lambda particle: particle.kinetic_energy)

clusters = []
current_cluster = [particles[0]]

for particle in particles[1:]:
    if particle.kinetic_energy - current_cluster[0].kinetic_energy > MAX_R:
        clusters.append(current_cluster)
        current_cluster = [particle]
        print(particle)
    else:
        current_cluster.append(particle)
clusters.append(current_cluster)

if len(clusters) != MAX_CLUSTER_COUNT:
    raise ValueError(f"Clusters count doesn't equal {MAX_CLUSTER_COUNT}")

centers_e = []
max_dist_sign2 = 0.0

for cluster in clusters:
    centers_e.append(find_min_dist(cluster))

    particles_special_characteristic_2 = [particle for particle in cluster if particle.special_characteristic == 2]

    for i in range(len(particles_special_characteristic_2)):
        for j in range(i + 1, len(particles_special_characteristic_2)):
            p1 = particles_special_characteristic_2[i]
            p2 = particles_special_characteristic_2[j]
            dist = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
            if dist > max_dist_sign2:
                max_dist_sign2 = dist

q1 = max_dist_sign2
q2 = max(centers_e)

print(int(q1 * 10000), int(q2 * 10000))
