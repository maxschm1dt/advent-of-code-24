f = []
a = set()
b = []

n_as_in_b = []

with open("d1/d1") as file:
    f = file.readlines()

for l in f:
    a.add(int(l.split('   ')[0]))
    b.append(int (l.split('   ')[1][:-1]))

for na in a:
    n_as_in_b.append(b.count(na) * na)

print(sum(n_as_in_b))