import unittest
from typing import List


def compare_row(index: int, row: str) -> bool:
    left = row[0:index + 1]
    right = row[index + 1:]
    cmp = min(len(left), len(right))
    return left[-cmp:][::-1] == right[0:cmp]


def get_pattern_value(pattern: List[str]) -> int:
    m, n = len(pattern), len(pattern[0])
    for j in range(n):
        if compare_row(j, pattern[0]):
            all_symmetric = True
            for i in range(1, m):
                if not compare_row(j, pattern[i]):
                    all_symmetric = False
                    break
            if all_symmetric:
                return j + 1

    for i in range(m):
        all_symmetric = True
        for k in range(0, i + 1):
            if i >= k and i + k + 1 < m and pattern[i - k] != pattern[i + k + 1]:
                all_symmetric = False
                break
        if all_symmetric:
            return (i + 1) * 100


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


def mirror(pat):
    for i in range(1, len(pat[0])):
        if sum(sum(x != y for x, y in zip(l[:i][::-1], l[i:])) for l in pat) == 1:
            return i
    return 0


with open("day_13.txt") as f:
    patterns = [line.splitlines() for line in f.read().split('\n\n')]

first, second = 0, 0
for pat in patterns:
    first += get_pattern_value(pat)
    second += mirror(pat) + 100 * mirror(list(zip(*pat)))

print(first)
print(second)
