import numpy as np


def takewhile_smaller(height, iterable):
    for x in iterable:
        if x < height:
            yield x
        elif x == height:
            yield x
            break
        else:
            break


def get_los(trees, i, j):
    height = trees[i, j]
    left = np.all(trees[i, :j] < height)
    right = np.all(trees[i, j+1:] < height)
    up = np.all(trees[:i, j] < height)
    down = np.all(trees[i+1:, j] < height)

    scenic_left = len(list(takewhile_smaller(height, reversed(trees[i, :j]))))
    scenic_right = len(list(takewhile_smaller(height, trees[i, j+1:])))
    scenic_up = len(list(takewhile_smaller(height, reversed(trees[:i, j]))))
    scenic_down = len(list(takewhile_smaller(height, trees[i+1:, j])))
    scenic = scenic_left * scenic_right * scenic_up * scenic_down
    return [(left or right or up or down), scenic]


lines = [[int(y) for y in x.strip("\n")] for x in open("input.txt")]
forest = np.array(lines)

count = 0
scores = []
# not too pythonic looping like this
for i in range(len(forest)):
    for j in range(len(forest[i])):
        los, scenic = get_los(forest, i, j)
        if los:
            count += 1
        scores.append(scenic)

print("Part 1: ", count)
print("Part 2: ", max(scores))
