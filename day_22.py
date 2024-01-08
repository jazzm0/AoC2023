import unittest
from typing import List


def orientation(p1: tuple, p2: tuple, p3: tuple) -> int:
    s = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    return s // abs(s) if s != 0 else 0


def on_segment(p1: tuple, p2: tuple, p3: tuple) -> bool:
    return (max(p1[0], p3[0]) >= p2[0] >= min(p1[0], p3[0]) and
            max(p1[1], p3[1]) >= p2[1] >= min(p1[1], p3[1]))


def intersect_2d(p1: tuple, q1: tuple, p2: tuple, q2: tuple) -> bool:
    a = orientation(p1, q1, p2)
    b = orientation(p1, q1, q2)
    c = orientation(p2, q2, p1)
    d = orientation(p2, q2, q1)
    if a != b and c != d:
        return True

    if (
            (a == 0 and on_segment(p1, p2, q1)) or
            (b == 0 and on_segment(p1, q2, q1)) or
            (c == 0 and on_segment(p2, p1, q2)) or
            (d == 0 and on_segment(p2, q1, q2))
    ):
        return True
    return False


def convert(brick: List[str]) -> tuple:
    return int(brick[0]), int(brick[1]), int(brick[2])


def get_bricks(f: str) -> List[tuple]:
    bricks = []
    with open(f) as ifile:
        for line in ifile:
            parts = line.strip().split("~")
            first = parts[0].split(",")
            second = parts[1].split(",")
            bricks.append((convert(first), convert(second)))
    return bricks


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(False, intersect_2d((1, 1), (10, 1), (1, 2), (10, 2)))

    def test_b(self):
        self.assertEqual(True, intersect_2d((10, 1), (0, 10), (0, 0), (10, 10)))

    def test_c(self):
        self.assertEqual(False, intersect_2d((-5, -5), (0, 0), (1, 1), (10, 10)))

    def test_d(self):
        self.assertEqual(True, intersect_2d((1, 0), (1, 2), (0, 0), (2, 0)))

    def test_e(self):
        self.assertEqual(False, intersect_2d((0, 0), (2, 0), (0, 2), (2, 2)))
