class Node:
    def __init__(self, name, parent, children, files):
        self.name = name
        self.parent = parent
        self.children = children
        self.files = files

    def __repr__(self, level=0):
        files = [x[1] for x in self.files]
        ret = "\t"*level + self.name + ": " + ",".join(files) + "\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

    def get_size(self):
        global sizes
        size_files = sum([x[0] for x in self.files])
        size_children = 0
        for child in self.children:
            size_children += child.get_size()
        result = size_files + size_children
        sizes.append(result)
        return result


lines = [x.strip("\n") for x in open("input.txt")][1:]
root = Node("/", None, [], [])
current = root
for line in lines:
    if line[0] == "$":
        # command
        com = line.split(" ")[1]
        if com == "cd":
            dest = line.split(" ")[2]
            if dest == "..":
                current = current.parent
            else:
                for child in current.children:
                    if child.name == dest:
                        current = child
    elif line[0] == "d":
        # dir
        name = line.split(" ")[1]
        child = Node(name, current, [], [])
        current.children.append(child)
    else:
        # file
        size, name = line.split(" ")
        current.files.append((int(size), name))

sizes = []
root.get_size()
print("Part 1: ", sum([x for x in sizes if x <= 100000]))
biggest = max(sizes)
to_delete = 30000000-(70000000-biggest)
print("Part 2: ", min([x for x in sizes if x >= to_delete]))
