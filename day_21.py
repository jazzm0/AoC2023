from typing import List


def get_map(f: str) -> List[str]:
    map = []
    with open(f) as ifile:
        for line in ifile:
            map.append(line.strip())
    return map


def index(current_index: int, boundary: int) -> int:
    return current_index % boundary


def get_next_plots(map: List[str], m: int, n: int, plots: set[tuple]) -> set[tuple]:
    next_plots = set()
    for plot in plots:
        if map[index(plot[0] - 1, m)][index(plot[1], n)] != "#":
            next_plots.add((plot[0] - 1, plot[1]))
        if map[index(plot[0] + 1, m)][index(plot[1], n)] != "#":
            next_plots.add((plot[0] + 1, plot[1]))
        if map[index(plot[0], m)][index(plot[1] - 1, n)] != "#":
            next_plots.add((plot[0], plot[1] - 1))
        if map[index(plot[0], m)][index(plot[1] + 1, n)] != "#":
            next_plots.add((plot[0], plot[1] + 1))

    return next_plots


def count_plots(map: List[str], steps: int) -> int:
    start = None
    m, n = len(map), len(map[0])
    for i in range(m):
        for j in range(n):
            if map[i][j] == "S":
                start = (i, j)
                break
        if start is not None:
            break

    plots = {start}
    for step in range(steps):
        plots = get_next_plots(map, m, n, plots)

    return len(plots)


print(count_plots(get_map("day_21_small.txt"), 500))
