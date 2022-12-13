import numpy as np
from collections import defaultdict


def get_neighbours(i, j, i_max, j_max):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < i_max:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < j_max:
        neighbours.append((i, j+1))
    return neighbours


def get_shortest(graph, start, end):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    return new_path
            visited.append(node)


lines = [list(x.strip("\n")) for x in open("input.txt")]
lines = np.array(lines)
start = tuple(np.argwhere(lines == "S")[0])
end = tuple(np.argwhere(lines == "E")[0])
lines[start] = "a"
lines[end] = "z"
to_code = np.vectorize(ord)
elevation = to_code(lines) - 97
graph = defaultdict(list)
for row in range(elevation.shape[0]):
    for col in range(elevation.shape[1]):
        neighbours = get_neighbours(row, col, elevation.shape[0]-1, elevation.shape[1]-1)
        for neighbour in neighbours:
            if elevation[neighbour] - elevation[row, col] <= 1:
                graph[(row, col)].append(neighbour)

print("Part 1: ", len(get_shortest(graph, start, end))-1)

# part 2
starts = np.argwhere(elevation == 0)
lengths = []
for i, start in enumerate(starts):
    if i % 10 == 0:
        print(i, "/", len(starts))
    start = tuple(start)
    shortest = get_shortest(graph, start, end)
    if shortest is not None:
        lengths.append(len(shortest)-1)

print("Part 2: ", min(lengths))
