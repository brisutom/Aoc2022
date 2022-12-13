from functools import cmp_to_key


def compare(left, right):
    # print("Comparing {} and {}".format(left, right))
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif type(left) == list and type(right) == list:
        results = []
        for i in range(max(len(left), len(right))):
            try:
                result = compare(left[i], right[i])
                if result is not None:
                    results.append(result)
                    break
            except IndexError:
                results.append(len(left) <= len(right))
        return results[-1]
    elif type(left) == list and type(right) == int:
        right = [right]
        return compare(left, right)
    elif type(left) == int and type(right) == list:
        left = [left]
        return compare(left, right)


def cmp(left, right):
    # just a wrapper needed for cmp_to_key
    if compare(left, right):
        return -1
    else:
        return 1


lines = [x.strip("\n") for x in open("input.txt")]
lines = [x for x in lines if x != ""]
lines = [lines[i:i+2] for i in range(0, len(lines), 2)]

right_order = []
for i, (left, right) in enumerate(lines):
    left = eval(left)
    right = eval(right)
    if compare(left, right):
        right_order.append(i+1)

print("Part 1: ", sum(right_order))

lines = [x.strip("\n") for x in open("input.txt")]
lines = [eval(x) for x in lines if x != ""]
lines.append([[2]])
lines.append([[6]])

sorted_lines = sorted(lines, key=cmp_to_key(cmp))
print("Part 2: ", (sorted_lines.index([[2]])+1)*(sorted_lines.index([[6]])+1))
