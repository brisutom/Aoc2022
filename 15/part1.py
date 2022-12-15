# yeah yeah I know, inefficient because you only need to know how many
# points there are, but it works

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def add_tuples(a, b, n=1):
    return (a[0] + n*b[0], a[1] + n*b[1])


def sgn(x):
    return tuple([int(y/abs(y)) if y != 0 else 0 for y in x])


def get_ranges(sensor, beacon):
    result = []
    dist = distance(sensor, beacon)
    top_point = add_tuples(sensor, (0, -1), dist)
    bot_point = add_tuples(sensor, (0, 1), dist)
    for i in range(dist+1):
        point1 = add_tuples(top_point, (-i, i))
        point2 = add_tuples(top_point, (i, i))
        result.append([point1, point2])
        point1 = add_tuples(bot_point, (i, -i))
        point2 = add_tuples(bot_point, (-i, -i))
        result.append([point1, point2])
    return result


def add_ranges(ranges, line):
    on_line = []
    for l, r in ranges:
        if l[1] != line:
            continue
        curr = l
        while curr != r:
            on_line.append(curr)
            diff = add_tuples(r, l, -1)
            step = sgn(diff)
            curr = add_tuples(curr, step)
        on_line.append(r)
    return on_line


lines = [x.strip("\n").split(" at ") for x in open("input.txt")]
lines = [[y.split(":")[0] for y in x if y[0] == "x"] for x in lines]
points = [[(int(z[0].split("=")[-1]), int(z[1].split("=")[-1])) for z in [y.split(",") for y in x]] for x in lines]
line = 2000000

on_line = []
beacons = []
sensors = []
for sensor, beacon in points:
    beacons.append(beacon)
    sensors.append(sensor)
    ran = get_ranges(sensor, beacon)
    on_line += add_ranges(ran, line)
    print(sensor, beacon)

on_line = set(on_line) - set(beacons) - set(sensors)
print("Part 1: ", len(on_line))
