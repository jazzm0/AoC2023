from typing import List

slopes = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def get_map(f: str) -> List[str]:
    map = []
    with open(f) as ifile:
        for line in ifile:
            map.append(line.strip())
    return map


def get_next_positions(map: List[str], actual_position: tuple, seen: dict) -> List[tuple]:
    m, n = len(map), len(map[0])
    current_tile = map[actual_position[0]][actual_position[1]]
    if current_tile in slopes:
        return [(actual_position[0] + slopes[current_tile][0], actual_position[1] + slopes[current_tile][1])]

    next_positions = []
    if actual_position[0] > 0:
        up = (actual_position[0] - 1, actual_position[1])
        if up not in seen and map[up[0]][up[1]] != '#' and map[up[0]][up[1]] != 'v':
            next_positions.append(up)

    if actual_position[0] < m - 1:
        down = (actual_position[0] + 1, actual_position[1])
        if down not in seen and map[down[0]][down[1]] != '#' and map[down[0]][down[1]] != '^':
            next_positions.append(down)

    if actual_position[1] > 0:
        left = (actual_position[0], actual_position[1] - 1)
        if left not in seen and map[left[0]][left[1]] != '#' and map[left[0]][left[1]] != '>':
            next_positions.append(left)

    if actual_position[1] < n - 1:
        right = (actual_position[0], actual_position[1] + 1)
        if right not in seen and map[right[0]][right[1]] != '#' and map[right[0]][right[1]] != '<':
            next_positions.append(right)

    return next_positions


def get_next_positions_new(map: List[str], actual_position: tuple, visited: dict) -> List[tuple]:
    m, n = len(map), len(map[0])
    next_positions = []
    if actual_position[0] > 0:
        up = (actual_position[0] - 1, actual_position[1])
        if up not in visited and map[up[0]][up[1]] != '#':
            next_positions.append(up)

    if actual_position[0] < m - 1:
        down = (actual_position[0] + 1, actual_position[1])
        if down not in visited and map[down[0]][down[1]] != '#':
            next_positions.append(down)

    if actual_position[1] > 0:
        left = (actual_position[0], actual_position[1] - 1)
        if left not in visited and map[left[0]][left[1]] != '#':
            next_positions.append(left)

    if actual_position[1] < n - 1:
        right = (actual_position[0], actual_position[1] + 1)
        if right not in visited and map[right[0]][right[1]] != '#':
            next_positions.append(right)

    return next_positions


def build_graph(map: List[str], np) -> (tuple, dict):
    start = None
    graph = {}
    for i in range(len(map[0])):
        if map[0][i] == ".":
            start = (0, i)
            break

    next_positions = np(map, start, graph)
    graph[start] = next_positions
    while len(next_positions) != 0:
        new_next_positions = set()
        for position in next_positions:
            if position in graph:
                continue
            next_positions_from_actual = np(map, position, graph)
            graph[position] = next_positions_from_actual
            for p in next_positions_from_actual:
                new_next_positions.add(p)
        next_positions = new_next_positions
    return start, graph


def get_longest_path(map: List[str]) -> int:
    start, graph = build_graph(map, get_next_positions)
    longest = 0
    finished = False
    while not finished:
        actual = start
        path = [actual]
        finished = True
        last = None
        steps = 0
        next_position = graph[actual]
        while len(next_position) != 0:
            steps += 1
            if len(next_position) > 1:
                finished = False
                last = actual
            actual = next_position[0]
            path.append(actual)
            next_position = graph[actual]
        longest = max(longest, steps)
        if last is not None:
            del graph[last][0]
    return longest


print(get_longest_path(get_map("day_23.txt")))
