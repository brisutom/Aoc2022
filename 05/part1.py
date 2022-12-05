lines = [x.strip("\n") for x in open("input.txt")]
split_line = lines.index("")
crates = [x.replace("    ", " [] ").replace("  ", " ").strip(" ").split(" ") for x in lines[:split_line-1]]
crates = [[y.replace("[", "").replace("]", "") for y in reversed(x) if y != "[]"] for x in zip(*crates)]
moves = lines[split_line+1:]

for move in moves:
    _, n, _, source, _, dest = move.split(" ")
    n = int(n) + 1
    source = int(source)-1
    dest = int(dest)-1
    for i in range(1, n):
        crates[dest].append(crates[source].pop())

print("Part 1: ", "".join([x[-1] for x in crates]))
