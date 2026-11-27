# 31505
from itertools import product


letters = sorted(set("АКЦЕНТ"))
for index, comb in enumerate(product(letters, repeat=5), start=1):
    if index % 2 != 0:
        continue

    if comb[0] == "А" or comb[0] == "Е" or comb[0] == "К":
        continue

    if comb.count("Т") < 1:
        continue

    print(index)
    break
