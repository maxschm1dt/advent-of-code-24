a, b, d = [], [], []
sum = 0

with open("d1/d1") as file:
    for line in file:
        left, right = line.split('   ')
        a.append(int(left))
        b.append(int(right))
    
a.sort()
b.sort()

for i, na in enumerate(a):
    sum += abs(na - b[i])

print(sum)