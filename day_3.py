import unittest
from typing import List

matrix = []

with open('day_3.txt') as ifile:
    for line in ifile:
        matrix.append(line.strip())


def find_and_sum_parts(matrix: List[str]) -> int:
    result = 0
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        j = 0
        while j < n:
            k = j
            if matrix[i][j].isdigit():
                is_adjacent = False
                for k in range(j, n):
                    if not matrix[i][k].isdigit():
                        break
                    if i > 0:
                        above = matrix[i - 1][k]
                        if not above.isdigit() and above != ".":
                            is_adjacent = True

                    if i < m - 1:
                        below = matrix[i + 1][k]
                        if not below.isdigit() and below != ".":
                            is_adjacent = True

                if not is_adjacent:
                    if j > 0:
                        if i > 0:
                            top_left = matrix[i - 1][j - 1]
                            if not top_left.isdigit() and top_left != ".":
                                is_adjacent = True
                        if i < m - 1:
                            bottom_left = matrix[i + 1][j - 1]
                            if not bottom_left.isdigit() and bottom_left != ".":
                                is_adjacent = True
                        left = matrix[i][j - 1]
                        if not left.isdigit() and left != ".":
                            is_adjacent = True
                    if k < n - 1:
                        right = matrix[i][k]
                        if not right.isdigit() and right != ".":
                            is_adjacent = True
                        if i > 0:
                            top_right = matrix[i - 1][k]
                            if not top_right.isdigit() and top_right != ".":
                                is_adjacent = True
                        if i < m - 1:
                            bottom_right = matrix[i + 1][k]
                            if not bottom_right.isdigit() and bottom_right != ".":
                                is_adjacent = True

                if is_adjacent:
                    if matrix[i][k].isdigit():
                        number = int(matrix[i][j:k + 1])
                    else:
                        number = int(matrix[i][j:k])
                    result += number
                j = k - 1
                if k == n - 1:
                    break
            j += 1
    return result


def extract_number(row: str, column: int) -> int:
    start, end = column, column
    while start > 0:
        if row[start - 1].isdigit():
            start -= 1
        else:
            break
    while end < len(row) - 1:
        if row[end + 1].isdigit():
            end += 1
        else:
            break
    return int(row[start:end + 1])


def find_and_sum_gears(matrix: List[str]) -> int:
    result = 0
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "*":
                part_number_neighbours = []
                if i > 0:
                    if matrix[i - 1][j].isdigit():  # top
                        part_number_neighbours.append(extract_number(matrix[i - 1], j))
                    else:
                        if j > 0 and matrix[i - 1][j - 1].isdigit():  # top left
                            part_number_neighbours.append(extract_number(matrix[i - 1], j - 1))
                        if j < n - 1 and matrix[i - 1][j + 1].isdigit():  # top right
                            part_number_neighbours.append(extract_number(matrix[i - 1], j + 1))

                if j > 0 and matrix[i][j - 1].isdigit():  # left
                    part_number_neighbours.append(extract_number(matrix[i], j - 1))
                if j < n - 1 and matrix[i][j + 1].isdigit():  # right
                    part_number_neighbours.append(extract_number(matrix[i], j + 1))

                if i < m - 1:
                    if matrix[i + 1][j].isdigit():  # bottom
                        part_number_neighbours.append(extract_number(matrix[i + 1], j))
                    else:
                        if j > 0 and matrix[i + 1][j - 1].isdigit():  # bottom left
                            part_number_neighbours.append(extract_number(matrix[i + 1], j - 1))
                        if j < n - 1 and matrix[i + 1][j + 1].isdigit():  # bottom right
                            part_number_neighbours.append(extract_number(matrix[i + 1], j + 1))

                if len(part_number_neighbours) == 2:
                    result += part_number_neighbours[0] * part_number_neighbours[1]

    return result


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(4361, find_and_sum_parts([
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]))

    def test_b(self):
        self.assertEqual(633, find_and_sum_parts([
            "467...114..",
            "....*......",
            ".35....633.",
            "......#....",
            "617........",
            "......+.58.",
            "..592......",
            "......755..",
            "...$.......",
            ".....664.59"
        ]))

    def test_c(self):
        self.assertEqual(489, extract_number(matrix[0], 5))
        self.assertEqual(239, extract_number(matrix[0], 128))
        self.assertEqual(489, extract_number(matrix[40], 139))
        self.assertEqual(489, extract_number(matrix[40], 138))
        self.assertEqual(489, extract_number(matrix[40], 137))
        self.assertEqual(229, extract_number(matrix[63], 0))


print(find_and_sum_parts(matrix))
print(find_and_sum_gears(matrix))
