def get_value(cycle):
    try:
        return registers[cycle]
    except KeyError:
        return registers[cycle-1]


lines = [x.strip("\n") for x in open("input.txt")]
interesting = [20, 60, 100, 140, 180, 220]
cycle = 1
register = 1
result = 0
registers = {}
for line in lines:
    if line == "noop":
        cycle += 1
    elif line[:4] == "addx":
        num = int(line.split(" ")[-1])
        register += num
        cycle += 2
    registers[cycle] = register

result = sum([x * get_value(x) for x in interesting])
print("Part 1: ", result)
