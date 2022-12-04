lines = [x.strip("\n") for x in open("input.txt")]
count1 = 0
count2 = 0
for line in lines:
    first, second = line.split(",")
    first = [int(x) for x in first.split("-")]
    second = [int(x) for x in second.split("-")]
    first = set(range(first[0], first[1]+1))
    second = set(range(second[0], second[1]+1))
    if first.issubset(second) or second.issubset(first):
        count1 += 1
    if len(first.intersection(second)):
        count2 += 1

print("Part 1: ", count1)
print("Part 2: ", count2)
