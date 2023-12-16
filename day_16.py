import unittest
from typing import List

left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)


def parse_tiles(f: str) -> List[str]:
    tiles = []
    with open(f) as ifile:
        for line in ifile:
            tiles.append(line.strip())
    return tiles


def get_left(tile: tuple) -> tuple:
    if tile[1] > 0:
        return tile[0], tile[1] - 1
    return ()


def get_right(tile: tuple, n: int) -> tuple:
    if tile[1] < n - 1:
        return tile[0], tile[1] + 1
    return ()


def get_up(tile: tuple) -> tuple:
    if tile[0] > 0:
        return tile[0] - 1, tile[1]
    return ()


def get_down(tile: tuple, m) -> tuple:
    if tile[0] < m - 1:
        return tile[0] + 1, tile[1]
    return ()


def get_next_tiles(tiles: List[str], current_tile: tuple, direction: tuple) -> List[tuple]:
    m, n = len(tiles), len((tiles[0]))
    element = tiles[current_tile[0]][current_tile[1]]
    if element == ".":
        if direction == up:
            return [get_up(current_tile)]
        elif direction == down:
            return [get_down(current_tile, m)]
        elif direction == left:
            return [get_left(current_tile)]
        elif direction == right:
            return [get_right(current_tile, n)]
    elif element == "-":
        if direction == left:
            return [get_left(current_tile)]
        elif direction == right:
            return [get_right(current_tile, n)]
        elif direction == up or direction == down:
            return [get_right(current_tile, n), get_left(current_tile)]
    elif element == "|":
        if direction == left or direction == right:
            return [get_up(current_tile), get_down(current_tile, m)]
        elif direction == up:
            return [get_up(current_tile)]
        elif direction == down:
            return [get_down(current_tile, m)]
    elif element == "/":
        if direction == left:
            return [get_down(current_tile, m)]
        elif direction == right:
            return [get_up(current_tile)]
        elif direction == up:
            return [get_right(current_tile, n)]
        elif direction == down:
            return [get_left(current_tile)]
    elif element == "\\":
        if direction == left:
            return [get_up(current_tile)]
        elif direction == right:
            return [get_down(current_tile, m)]
        elif direction == up:
            return [get_left(current_tile)]
        elif direction == down:
            return [get_right(current_tile, n)]


def count_energized_tiles(tiles: List[str]) -> int:
    tiles_energized = {(0, 0): get_next_tiles(tiles, (0, 0), (0, 1))}
    seen = set()
    done = False
    while not done:
        done = True
        new_tiles_energized = tiles_energized.copy()
        for start, targets in tiles_energized.items():
            for t in targets:
                if t == ():
                    continue
                direction = (t[0] - start[0], t[1] - start[1])
                if (start, direction) in seen:
                    continue
                seen.add((start, direction))
                new_tiles_energized[t] = get_next_tiles(tiles, t, direction)
                done = False
        tiles_energized = new_tiles_energized

    return len(tiles_energized)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([(1, 5), (3, 5)], get_next_tiles(parse_tiles("day_16_small.txt"), (2, 5), right))

    def test_b(self):
        self.assertEqual([(1, 5)], get_next_tiles(parse_tiles("day_16_small.txt"), (2, 5), up))

    def test_c(self):
        self.assertEqual([(0, 4)], get_next_tiles(parse_tiles("day_16_small.txt"), (0, 5), up))

    def test_d(self):
        self.assertEqual([(0, 6)], get_next_tiles(parse_tiles("day_16_small.txt"), (0, 5), down))

    def test_e(self):
        self.assertEqual([()], get_next_tiles(parse_tiles("day_16_small.txt"), (9, 5), down))

    def test_h(self):
        self.assertEqual(7623, count_energized_tiles(parse_tiles("day_16.txt")))
