from math import lcm

instructions = None
nodes = {}
starts, ends = [], {}
with open('day_8.txt') as ifile:
    for line in ifile:
        if instructions is None:
            instructions = line.strip()
        elif line.strip() != "":
            parts = line.strip().split("=")
            key = parts[0].strip()
            if key[2] == "A":
                starts.append(key)
            node = parts[1].strip()[1:len(parts[1].strip()) - 1].split(",")
            nodes[key] = (node[0].strip(), node[1].strip())

steps = 0
next_node = "AAA"
found = False

while not found:
    for index in range(len(instructions)):
        if instructions[index] == "L":
            next_node = nodes[next_node][0]
        else:
            next_node = nodes[next_node][1]
        steps += 1
        if next_node == "ZZZ":
            found = True
            break

print(steps)

steps = 0
found = False
next_nodes = starts
multipliers = []

while not found:
    for instruction in instructions:
        new_next_nodes = []
        for node in next_nodes:
            if instruction == "L":
                next_node = nodes[node][0]
            else:
                next_node = nodes[node][1]
            new_next_nodes.append(next_node)
            if next_node[2] == "Z":
                if next_node not in ends:
                    multipliers.append(steps + 1)
                ends[next_node] = steps + 1

        next_nodes = new_next_nodes
        steps += 1
        if len(ends) == len(starts):
            print(ends)
            found = True
            break

print(lcm(*multipliers))
