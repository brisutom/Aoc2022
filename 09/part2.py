from matplotlib import pyplot as plt


def add_tuples(a, b, n=1):
    return (a[0] + n*b[0], a[1] + n*b[1])


def is_touching(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


def sgn(x):
    return [y/abs(y) if y != 0 else 0 for y in x]


def move_point(point, previous):
    if not is_touching(previous, point):
        drift = sgn(add_tuples(previous, point, -1))
        point = add_tuples(point, drift)
    return point


dirs = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}
lines = [x.strip("\n").split(" ") for x in open("input.txt")]
lines = [(x[0], int(x[1])) for x in lines]
visited_h = []
visited_t = []
points = [(0, 0)]*10
for d, n in lines:
    for i in range(n):
        visited_h.append(points[0])
        visited_t.append(points[-1])
        for j, point in enumerate(points):
            if j == 0:
                # move head
                points[0] = add_tuples(points[0], dirs[d])
                continue
            points[j] = move_point(points[j], points[j-1])

img = plt.plot(*zip(*visited_h), color="blue")
plt.scatter(*zip(*visited_t), color="orange")
plt.show()

print(len(set(visited_t)))
