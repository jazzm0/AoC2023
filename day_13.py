import unittest
from typing import List


def check_pattern(pattern: List[str]) -> int:
    m, n = len(pattern), len(pattern[0])
    for i in range(m - 1):
        all_symmetric = True
        for k in range(0, i + 1):
            if i >= k and i + k + 1 < m and pattern[i - k] != pattern[i + k + 1]:
                all_symmetric = False
                break
        if all_symmetric:
            return i + 1
    return 0


def get_pattern_value(pattern: List[str]) -> int:
    value = check_pattern(pattern)
    if value != 0:
        return value * 100
    return check_pattern([*zip(*pattern)])


def mirror(pat):
    for i in range(1, len(pat[0])):
        if sum(sum(x != y for x, y in zip(l[:i][::-1], l[i:])) for l in pat) == 1:
            return i
    return 0


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(5, get_pattern_value([
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
        ]))

    def test_b(self):
        self.assertEqual(400, get_pattern_value([
            "#...##..#",
            "#....#..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]))

    def test_c(self):
        self.assertEqual(300, get_pattern_value([
            "..##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#."
        ]))

    def test_d(self):
        self.assertEqual(100, get_pattern_value([
            "#...##..#",
            "#...##..#",
            "..##..###",
            "#####.##.",
            "#####.##.",
            "..##..###",
            "#....#..#"
        ]))


with open("day_13.txt") as f:
    patterns = [line.splitlines() for line in f.read().split('\n\n')]

first, second = 0, 0
for pattern in patterns:
    first += get_pattern_value(pattern)
    second += mirror(pattern) + 100 * mirror(list(zip(*pattern)))

print(first)
print(second)
