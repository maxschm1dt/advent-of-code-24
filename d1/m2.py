a, b  = [], []
sum = 0

with open("d1/d1") as file:
    for line in file:
        left, right = line.split('   ')
        a.append(int(left))
        b.append(int(right))

for na in a:
    sum += b.count(na) * na

print(sum)