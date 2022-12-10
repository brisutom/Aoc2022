def get_value(cycle):
    try:
        return registers[cycle]
    except KeyError:
        return registers[cycle-1]


lines = [x.strip("\n") for x in open("input.txt")]
cycle = 1
register = 1
registers = {1: 1}
for line in lines:
    if line == "noop":
        cycle += 1
    elif line[:4] == "addx":
        num = int(line.split(" ")[-1])
        register += num
        cycle += 2
    registers[cycle] = register

lines = ""
for i in range(1, 241):
    register = get_value(i)
    if register in ((i-2) % 40, (i-1) % 40, i % 40):
        lines += "#"
    else:
        lines += "."
    if i % 40 == 0:
        lines += "\n"

print(lines)
