# ended up rewriting the tail movement for part2, but keeping part1 as it was
from matplotlib import pyplot as plt


def add_tuples(a, b, n=1):
    return (a[0] + n*b[0], a[1] + n*b[1])


def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])


dirs = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}
lines = [x.strip("\n").split(" ") for x in open("input.txt")]
lines = [(x[0], int(x[1])) for x in lines]
visited_h = []
visited_t = []
head = (0, 0)
tail = (0, 0)
for d, n in lines:
    for i in range(n):
        visited_h.append(head)
        visited_t.append(tail)
        head_old = head
        # move head
        head = add_tuples(head, dirs[d])
        # move tail
        if distance(head, tail) == 2 and (head[0] == tail[0] or
                                          head[1] == tail[1]):
            tail = add_tuples(tail, dirs[d])
        elif distance(head, tail) > 2:
            drift = add_tuples(head_old, tail, -1)
            tail = add_tuples(tail, drift)

img = plt.plot(*zip(*visited_h), color="blue")
plt.scatter(*zip(*visited_t), color="orange")
plt.show()

print(len(set(visited_t)))
