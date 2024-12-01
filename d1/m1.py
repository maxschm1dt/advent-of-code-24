f = []
a = []
b = []
d = []

with open("d1/d1") as file:
    f = file.readlines()

for l in f:
    a.append(int(l.split('   ')[0]))
    b.append(int (l.split('   ')[1][:-1]))

a.sort()
b.sort()

for i, na in enumerate(a):
    d.append(abs( na - b[i]))

print(sum(d))