import unittest
from typing import List


def tilt_column(dish: List[List[str]], column: int):
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


def tilt_dish_calc_load(dish: List[List[str]]) -> int:
    for column in range(len(dish[0])):
        tilt_column(dish, column)
    result = 0
    for row in range(len(dish)):
        count = 0
        for column in range(len(dish[0])):
            if dish[row][column] == "O":
                count += 1
        result += count * (len(dish) - row)
    return result


dish = []

with open('day_14.txt') as ifile:
    for line in ifile:
        dish.append([c for c in line.strip()])

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
        for i in input:
            dish.append([c for c in i.strip()])
        self.assertEqual(136, tilt_dish_calc_load(dish))
