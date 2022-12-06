line = open("input.txt").read()


def extract(n):
    segments = [line[i:i+n] for i in range(0, len(line)-n)]
    for i, seg in enumerate(segments):
        if len(set(seg)) == n:
            return i+n


print("Part 1: ", extract(4))
print("Part 2: ", extract(14))
