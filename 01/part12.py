lines = [x for x in open("input.txt")]

calories = []
current_calories = 0
for line in lines:
    if line == "\n":
        calories.append(current_calories)
        current_calories = 0
        continue
    current_calories += int(line)

# part 1
print("Part 1: ", max(calories))
# part 2
print("Part 2: ", sum(sorted(calories)[-3:]))
