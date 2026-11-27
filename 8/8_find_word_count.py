# 31216
from itertools import product

letters = sorted(set("ЦВЕТОК"))
count = 0
for index, comb in enumerate(product(letters, repeat=6), start=1):
    if index % 2 == 0:
        continue

    if comb.count("Т") != 2:
        continue

    if comb.count("Ц") != 1:
        continue

    if comb.count("В") != 0 or comb.count("Е") != 0 or \
            comb.count("К") != 0:
        continue

    count += 1

print(count)
