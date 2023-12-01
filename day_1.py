import unittest


def get_digit(s: str) -> int:
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    lengths = [3 + 1, 4 + 1, 5 + 1]
    first, last = None, None

    for i in range(len(s)):
        if first is None:
            if s[i].isdigit():
                first = int(s[i]) * 10
            else:
                for length in lengths:
                    possible_word = s[i:i + length - 1]
                    if possible_word in words:
                        first = words[possible_word] * 10
                        break

        if last is None:
            if s[-(i + 1)].isdigit():
                last = int(s[-(i + 1)])
            else:
                for length in lengths:
                    if i == 0:
                        possible_word = s[-(i + length):]
                    else:
                        possible_word = s[-(i + length - 1):-i]
                    if possible_word in words:
                        last = words[possible_word]
                        break

        if first is not None and last is not None:
            return first + last


with open('day_1.txt') as ifile:
    sum = 0
    for line in ifile:
        sum += get_digit(line)

print(sum)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(29, get_digit("two1nine"))
        self.assertEqual(83, get_digit("eightwothree"))
        self.assertEqual(13, get_digit("abcone2threexyz"))
