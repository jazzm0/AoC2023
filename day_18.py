from typing import List

from PIL import Image, ImageDraw

directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
new_directions = {"2": (0, -1), "0": (0, 1), "3": (-1, 0), "1": (1, 0)}


def parse_instructions(f: str) -> List[tuple]:
    instructions = []
    with open(f) as ifile:
        for line in ifile:
            parts = line.strip().split()
            direction = directions[parts[0]]
            instructions.append((direction, int(parts[1])))
    return instructions


def parse_instructions_new(f: str) -> List[tuple]:
    instructions = []
    with open(f) as ifile:
        for line in ifile:
            parts = line.strip().split()
            direction = new_directions[parts[2][-2]]
            instructions.append((direction, int(parts[2][2:7], 16)))
    return instructions


def dig(instructions: List[tuple]):
    position = (0, 0)
    plan = [position]
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1]
        for i in range(steps):
            position = (position[0] + direction[0], position[1] + direction[1])
            min_x = min(min_x, position[0])
            max_x = max(max_x, position[0])
            min_y = min(min_y, position[1])
            max_y = max(max_y, position[1])
            plan.append(position)
    m, n = max_x - min_x + 1, max_y - min_y + 1

    im = Image.new(mode="RGB", size=(m, n), color=(0, 0, 0))
    for i in range(len(plan)):
        im.putpixel(xy=(plan[i][0] + abs(min_x), plan[i][1] + abs(min_y)), value=(255, 255, 255))

    ImageDraw.floodfill(im, (150, 150), value=(255, 255, 255))
    im.save("map.png")
    result = 0
    for pixel in im.getdata():
        if pixel == (255, 255, 255):
            result += 1

    return result


instructions = parse_instructions("day_18.txt")
print(dig(instructions))
# instructions = parse_instructions_new("day_18_small.txt")
# print(dig(instructions))
