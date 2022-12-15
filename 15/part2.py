# pypy really speeds this one up
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


lines = [x.strip("\n").split(" at ") for x in open("input.txt")]
lines = [[y.split(":")[0] for y in x if y[0] == "x"] for x in lines]
points = [[(int(z[0].split("=")[-1]), int(z[1].split("=")[-1])) for z in [y.split(",") for y in x]] for x in lines]

max_coord = 4000000
x = 0
y = 0
found = False
while y <= max_coord and not found:
    while x <= max_coord:
        for sensor, beacon in points:
            dist = distance(sensor, beacon)
            p2s = distance(sensor, (x, y))
            y_diff = abs(sensor[1] - y)
            if p2s <= dist:
                x = sensor[0] + dist - y_diff
                break
        else:
            print("Part 2: ", x * 4000000 + y)
            found = True
        x += 1
    x = 0
    y += 1
