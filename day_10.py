import unittest
from typing import List


def check_right(map: List[str], position: tuple, visited: set) -> tuple:
    n = len(map[0])
    if position[1] < n - 1:
        right_index = (position[0], position[1] + 1)
        right = map[right_index[0]][right_index[1]]
        if (right == "-" or right == "7" or right == "J") and right_index not in visited:
            return right_index
    return None


def check_left(map: List[str], position: tuple, visited: set) -> tuple:
    if position[1] > 0:
        left_index = (position[0], position[1] - 1)
        left = map[left_index[0]][left_index[1]]
        if (left == "-" or left == "F" or left == "L") and left_index not in visited:
            return left_index
    return None


def check_up(map: List[str], position: tuple, visited: set) -> tuple:
    if position[0] > 0:
        up_index = (position[0] - 1, position[1])
        up = map[up_index[0]][up_index[1]]
        if (up == "|" or up == "F" or up == "7") and up_index not in visited:
            return up_index
    return None


def check_down(map: List[str], position: tuple, visited: set) -> tuple:
    if position[0] < len(map) - 1:
        down_index = (position[0] + 1, position[1])
        down = map[down_index[0]][down_index[1]]
        if (down == "|" or down == "L" or down == "J") and down_index not in visited:
            return down_index
    return None


def find_next_position(map: List[str], position: tuple, visited: set) -> tuple:
    visited.add(position)
    actual_pipe = map[position[0]][position[1]]
    up = check_up(map, position, visited)
    down = check_down(map, position, visited)
    left = check_left(map, position, visited)
    right = check_right(map, position, visited)

    if actual_pipe == "|":
        return up if up is not None else down
    elif actual_pipe == "-":
        return left if left is not None else right
    elif actual_pipe == "L":
        return up if up is not None else right
    elif actual_pipe == "J":
        return up if up is not None else left
    elif actual_pipe == "7":
        return down if down is not None else left
    elif actual_pipe == "F":
        return down if down is not None else right

    return None


def find_farthest_distance(map: List[str]) -> int:
    start = None
    visited = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "S":
                start = (i, j)
                break
    visited.add(start)
    next_left, next_right = (find_next_position(map, (start[0], start[1] + 1), visited),
                             find_next_position(map, (start[0], start[1] - 1), visited))
    one_route, another_route = [next_left], [next_right]
    while next_left != next_right:
        next_left, next_right = (find_next_position(map, next_left, visited),
                                 find_next_position(map, next_right, visited))
        one_route.append(next_left)
        another_route.append(next_right)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) in visited:
                print('I', end="")
            else:
                print('0', end="")
        print()
    return max(len(one_route), len(another_route)) + 1


map = []
with open('day_10.txt') as ifile:
    for line in ifile:
        map.append(line.strip())

print(find_farthest_distance(map))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual((2, 1), find_next_position([
            ".....",
            ".F-7.",
            ".|.|.",
            ".L-J.",
            "....."], (1, 1), {(1, 2)}))

    def test_b(self):
        self.assertEqual((2, 3), find_next_position([
            ".....",
            ".F-7.",
            ".|.|.",
            ".L-J.",
            "....."], (1, 3), {(1, 2)}))
