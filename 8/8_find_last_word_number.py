# 27620
from itertools import product


def contains_two_same_neighbours(seq: tuple) -> bool:
    for i in range(len(seq) - 1):
        if seq[i] == "Ц" and seq[i + 1] == "Ц":
            return True

    return False


last_index = -1
letters = sorted(set("ЦИТРУС"))
for index, comb in enumerate(product(letters, repeat=5), start=1):
    if comb.count("И") != 2:
        continue

    if contains_two_same_neighbours(comb):
        continue

    last_index = index

print(last_index)
