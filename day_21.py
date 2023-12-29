from random import randint
from typing import List

from PIL import Image


def get_map(f: str) -> List[str]:
    map = []
    with open(f) as ifile:
        for line in ifile:
            map.append(line.strip())
    return map


def available_plots(map: List[str]) -> (int, int):
    m, n = len(map), len(map[0])
    available, rock = 0, 0
    for i in range(m):
        for j in range(n):
            if map[i][j] != "#":
                available += 1
            else:
                rock += 1
    return available, rock


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


def plot_map(map: List[str], filename: str):
    m, n = len(map), len(map[0])

    im = Image.new(mode="RGB", size=(m, n), color=(0, 0, 0))
    for i in range(m):
        for j in range(n):
            if map[i][j] != "#":
                im.putpixel(xy=(j, i), value=(255, 255, 255))

    im.save(filename)


def plot_plots(all_plots: List[set[tuple]], overdraw: bool, filename: str):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for plots in all_plots:
        for p in plots:
            min_x, min_y = min(p[1], min_x), min(p[0], min_y)
            max_x, max_y = max(p[1], max_x), max(p[0], max_y)
    n, m = abs(min_x) + max_x + 1, abs(min_y) + max_y + 1

    im = Image.new(mode="RGB", size=(m, n), color=(0, 0, 0))
    color = 50
    plotted = set()
    for plots in all_plots:
        r, g, b = randint(10, 255), randint(10, 255), randint(10, 255)
        if color > 255:
            color = 10
        for p in plots:
            point = (p[1] + abs(min_y), p[0] + abs(min_x))
            if point not in plotted:
                if not overdraw:
                    plotted.add(point)
                im.putpixel(xy=point, value=(r, g, b))

    im.save(filename)


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
    all_plots = [plots]
    for step in range(steps):
        plots = get_next_plots(map, m, n, plots)
        all_plots.append(plots)

    plot_plots(all_plots, False, "infinite.png")
    plot_plots(all_plots, True, "infinite-overdraw.png")
    return len(plots)


file_prefix = "day_21"
map = get_map(file_prefix + ".txt")
# plot_map(map, file_prefix + ".png")
available, rock = available_plots(map)
print(available)
for i in range(131, 525):
    print(f'i -> {i % 131} = ', count_plots(map, i) % available)

# 202300 * 131 + 65 == 26501365 == 2 x 2 x 5 x 5 x 7 x 17 x 17
# 65  -> 3802
# 130 -> 14893
# 131 -> 15123
# 260 -> 59161
# 262 -> 60063
# 263 -> 60502
