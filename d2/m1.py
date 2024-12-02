ls = []

with open("d2/d2") as file:
    for line in file:
        levels = [int(x) for x in line.split(' ')]
        diffs = [levels[i + 1] - x for i, x in enumerate(levels[:-1])]
        ls.append(diffs)

for l in ls:
