instructions = None
nodes = {}

with open('day_8.txt') as ifile:
    for line in ifile:
        if instructions is None:
            instructions = line.strip()
        elif line.strip() != "":
            parts = line.strip().split("=")
            key = parts[0].strip()
            node = parts[1].strip()[1:len(parts[1].strip()) - 1].split(",")
            nodes[key] = (node[0].strip(), node[1].strip())

steps = 0
next_node = "AAA"
found = False

while not found:
    for index in range(len(instructions)):
        if instructions[index] == "L":
            next_node = nodes[next_node][0]
        elif instructions[index] == "R":
            next_node = nodes[next_node][1]
        steps += 1
        if next_node == "ZZZ":
            found = True
            break

print(steps)
