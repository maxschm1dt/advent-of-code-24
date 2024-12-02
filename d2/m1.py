ls = []
n_safe = 0

with open("d2/d2") as file:
    for line in file:
        levels = [int(x) for x in line.split(' ')]
        ls.append([levels[i + 1] - x for i, x in enumerate(levels[:-1])])

for l in ls:
    abs_diffs = [abs(x) for x in l]
    is_in_bounds = max(abs_diffs) <= 3 and min(abs_diffs) > 0
    is_monotone = all([x >0 for x in l]) or all(x < 0 for x in l)
    n_safe += 1 if is_in_bounds and is_monotone else 0 

print(n_safe)