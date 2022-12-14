from collections import defaultdict
from matplotlib import pyplot as plt


DOWN = (0, 1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)


def add_tuples(a, b, n=1):
    return (a[0] + n*b[0], a[1] + n*b[1])


def sgn(x):
    return tuple([int(y/abs(y)) if y != 0 else 0 for y in x])


def add_line(d, start, end):
    current = start
    diff = add_tuples(end, start, -1)
    step = sgn(diff)
    while current != end:
        d[current] = 1
        current = add_tuples(current, step)
    d[end] = 1


def simulate_sand(d):
    sand = (500, 0)
    while True:
        if sand[1] == max_depth + 1:
            return sand
        if d[add_tuples(sand, DOWN)] == 0:
            sand = add_tuples(sand, DOWN)
        elif d[add_tuples(sand, DOWN_LEFT)] == 0:
            sand = add_tuples(sand, DOWN_LEFT)
        elif d[add_tuples(sand, DOWN_RIGHT)] == 0:
            sand = add_tuples(sand, DOWN_RIGHT)
        else:
            return sand


lines = [x.strip("\n").split(" -> ") for x in open("input.txt")]
lines = [[tuple(map(int, y.split(","))) for y in x] for x in lines]
scan = defaultdict(int)
max_depth = 0
for line in lines:
    for start, end in zip(line, line[1:]):
        if max(start[1], end[1]) > max_depth:
            max_depth = max(start[1], end[1])
        add_line(scan, start, end)

scan_rock = scan.copy()
result = 0
while True:
    if scan[(500, 0)] == 2:
        break
    sand = simulate_sand(scan)
    scan[sand] = 2
    result += 1

print("Part 2: ", result)

plt.gca().invert_yaxis()
img = plt.scatter(*zip(*scan), color="yellow")
plt.scatter(*zip(*scan_rock), color="black")
plt.show()
