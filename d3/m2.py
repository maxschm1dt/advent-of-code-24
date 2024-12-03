import re
data, sum, enabled = open("d3/d3").readline(), 0, True

matches = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\))|(?:don't\(\))|(?:do\(\))", data)

for match in matches:
    if match.startswith("do()"):
        enabled = True
    elif match.startswith("don't()"):
        enabled = False
    elif enabled:
        x,y = re.findall(r"\d{1,3}", match, flags=0)
        sum += int(x) * int(y)

print(sum)