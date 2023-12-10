from typing import List

map = []

pipes = {"|", "-", "L", "J", "7", "F", ".", "S"}


def find_next_positions(map: List[str], position: tuple) -> List[tuple]:
    next_positions = []
    if position[0] > 0:
        map[position[0] - 1][position[1]]

    return next_positions


def find_farthest_distance(map: List[str]) -> int:
    start = None
    steps = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start = (i, j)
                break
    return 0


with open('day_10.txt') as ifile:
    for line in ifile:
        map.append(line.strip())

find_farthest_distance(map)
