import re
data, sum = open("d3/d3").readline(), 0

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

for match in matches:
    x,y = re.findall(r"\d{1,3}", match)
    sum += int(x) * int(y)

print(sum)