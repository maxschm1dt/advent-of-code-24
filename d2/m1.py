first_degree_safe, second_degree_safe, ls = 0, 0, []

def is_safe(l: list) -> bool:
    diffs = [x - l[i + 1] for i, x in enumerate(l[:-1])]
    abs_diffs = [abs(x) for x in diffs]
    is_in_bounds = max(abs_diffs) <= 3 and min(abs_diffs) > 0
    is_monotone = all(x > 0 for x in diffs) or all(x < 0 for x in diffs)

    return is_in_bounds and is_monotone

with open("d2/d2") as file:
    for line in file:
        ls.append([int(x) for x in line.split()])

for i, l in enumerate(ls):
    first_degree_safe += 1 if is_safe(l) else 0
    second_degree_safe += 1 if any(is_safe(x) for x in [l[:i] + l[i+1:] for i in range(len(l))]) else 0

print("star1: ", first_degree_safe)
print("star2: ",second_degree_safe)