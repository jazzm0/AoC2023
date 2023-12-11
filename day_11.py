import unittest
from typing import List


def count_distances(map: List[str]) -> int:
    empty_rows, empty_columns, galaxies = [], [], []
    for i in range(len(map)):
        is_row_empty = True
        for j in range(len(map[0])):
            if map[i][j] == "#":
                is_row_empty = False
                break
        if is_row_empty:
            empty_rows.append(i)

    for j in range(len(map[0])):
        is_column_empty = True
        for i in range(len(map)):
            if map[i][j] == "#":
                is_column_empty = False
                break
        if is_column_empty:
            empty_columns.append(j)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                galaxies.append((i, j))

    offset = 0
    multiplier = (10 ** 6) - 1
    for row in empty_rows:
        for index in range(len(galaxies)):
            if galaxies[index][0] > row + offset:
                galaxies[index] = (galaxies[index][0] + multiplier, galaxies[index][1])
        offset += multiplier

    offset = 0
    for column in empty_columns:
        for index in range(len(galaxies)):
            if galaxies[index][1] > column + offset:
                galaxies[index] = (galaxies[index][0], galaxies[index][1] + multiplier)
        offset += multiplier

    sum_min_distances = 0

    for start in galaxies:
        for end in galaxies:
            if start != end:
                sum_min_distances += abs(start[0] - end[0]) + abs(start[1] - end[1])
    return sum_min_distances // 2


map = []
with open('day_11.txt') as ifile:
    for line in ifile:
        map.append(line.strip())

print(count_distances(map))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        map = []
        with open('day_11_small.txt') as ifile:
            for line in ifile:
                map.append(line.strip())

        self.assertEqual(82000210, count_distances(map))
