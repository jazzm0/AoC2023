import unittest
from typing import List


def tilt(dish: List[List[str]], column: int):
    n = len(dish)
    start = 0
    while start < n:
        if dish[start][column] == "#" or dish[start][column] == "O":
            start += 1
            continue
        for next in range(start + 1, n):
            if dish[next][column] == "O":
                tmp = dish[start][column]
                dish[start][column] = dish[next][column]
                dish[next][column] = tmp
                break
            elif dish[next][column] == "#":
                start = next
                break
        start += 1


def rotate(dish: List[List[str]]) -> List[List[str]]:
    n = len(dish)
    result = [["0" for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = dish[i][j]
    return result


def calculate_load(dish: List[List[str]]) -> int:
    n = len(dish)
    result = 0
    for row in range(n):
        count = 0
        for column in range(n):
            if dish[row][column] == "O":
                count += 1
        result += count * (n - row)
    return result


def cycle(dish: List[List[str]]) -> List[List[str]]:
    n = len(dish)
    for _ in range(4):
        for column in range(n):
            tilt(dish, column)
        dish = rotate(dish)
    return dish


def tilt_dish_calc_load(dish: List[List[str]]) -> int:
    for _ in range(1000):
        dish = cycle(dish)
    return calculate_load(dish)


dish = []

with open('day_14.txt') as ifile:
    for line in ifile:
        dish.append(list(line.strip()))

print(tilt_dish_calc_load(dish))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        dish = []
        input = ["O....#....",
                 "O.OO#....#",
                 ".....##...",
                 "OO.#O....O",
                 ".O.....O#.",
                 "O.#..O.#.#",
                 "..O..#O..O",
                 ".......O..",
                 "#....###..",
                 "#OO..#...."]
        for line in input:
            dish.append(list(line.strip()))
        self.assertEqual(64, tilt_dish_calc_load(dish))

    def test_b(self):
        dish = []
        input = ["abc",
                 "def",
                 "ghi"]
        for line in input:
            dish.append(list(line.strip()))
        self.assertEqual(
            [['g', 'd', 'a'],
             ['h', 'e', 'b'],
             ['i', 'f', 'c']], rotate(dish))
