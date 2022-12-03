import string
conversion = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
lines = [x.strip("\n") for x in open("input.txt")]
result = []
for line in lines:
    half_len = len(line)//2
    half1, half2 = set(line[:half_len]), set(line[half_len:])
    both = list(half1.intersection(half2))[0]
    result.append(conversion[both])

print("Part 1: ", sum(result))
