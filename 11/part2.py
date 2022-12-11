from math import prod


class Monkey:
    monkeys = None

    def __init__(self, mid, items, oper, n, if_true, if_false):
        self.mid = mid
        self.items = items
        self.oper = oper
        self.n = n
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def __repr__(self):
        return "Monkey {}: {}, inspected {}".format(self.mid, self.items, self.inspected)

    def test(self, x):
        return x % self.n == 0

    def operation(self, old):
        return eval(self.oper)

    def send(self, dest, x):
        self.monkeys[dest].items.append(x)

    def inspect(self):
        processed = []
        for i, worry in enumerate(self.items):
            self.inspected += 1
            processed.append(i)
            worry = self.operation(worry)
            worry = worry % modulus
            if self.test(worry):
                self.send(self.if_true, worry)
            else:
                self.send(self.if_false, worry)
        self.items = [self.items[i] for i in range(len(self.items)) if i not in processed]


lines = [x.strip("\n") for x in open("input.txt")]
monkeys_raw = [lines[i: i+7] for i in range(0, len(lines), 7)]
monkeys = []
for monkey in monkeys_raw:
    mid = int(monkey[0].split(" ")[-1][:-1])
    items = [int(x) for x in monkey[1][18:].split(", ")]
    oper = monkey[2].split(" = ")[-1]
    n = int(monkey[3].split(" ")[-1])
    if_true = int(monkey[4].split(" ")[-1])
    if_false = int(monkey[5].split(" ")[-1])
    monkeys.append(Monkey(mid, items, oper, n, if_true, if_false))

modulus = prod([m.n for m in monkeys])
Monkey.monkeys = monkeys
for _ in range(10000):
    for monkey in Monkey.monkeys:
        monkey.inspect()

result = sorted([m.inspected for m in Monkey.monkeys])[-2:]
print("Part 2: ", result[0]*result[1])
