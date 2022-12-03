import string
conversion = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
lines = [set(x.strip("\n")) for x in open("input.txt")]
groups = [lines[i: i+3] for i in range(0, len(lines), 3)]
result = []
for group in groups:
    every = list(group[0].intersection(group[1]).intersection(group[2]))[0]
    result.append(conversion[every])

print("Part 2: ", sum(result))
