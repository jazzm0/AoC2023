import unittest


def shrink(record: str) -> str:
    shrunk = False
    while not shrunk:
        shrunk = True
        if record[0] == ".":
            record = record[1:]
            shrunk = False
        if record[-1] == ".":
            record = record[:-1]
            shrunk = False
    result = ""
    for i in range(len(record)):
        if (i == len(record) - 1) or not record[i] == record[i + 1] == ".":
            result += record[i]
    return result


def get_number_of_arrangement(operational_days: int, group: str) -> int:
    if len(group) == operational_days:
        return 1
    wildcard_counts = 1
    for i in range(len(group)):
        if group[i] == "?" and (i + operational_days < len(group)):
            wildcard_counts += 1
        else:
            break
    return wildcard_counts


def count_all_arrangements(record: str) -> int:
    parts = record.split(" ")
    operational_groups = shrink(parts[0]).split(".")
    operational_days = [int(x) for x in parts[1].split(",")]
    print(operational_groups, operational_days)


with open('day_12.txt') as ifile:
    for record in ifile:
        count_all_arrangements(record.strip())


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(3, get_number_of_arrangement(8, "??##???#???"))

    def test_b(self):
        self.assertEqual(4, get_number_of_arrangement(8, "???#???#???"))

    def test_c(self):
        self.assertEqual(4, get_number_of_arrangement(8, "???????????"))

    def test_d(self):
        self.assertEqual(4, count_arrangements("??.?.??##?##?? 1,1,8"))

    def test_e(self):
        self.assertEqual(4, count_arrangements("????.######..#####. 1,6,5"))

    def test_f(self):
        self.assertEqual(4, count_arrangements("??.#..????? 1,1,2"))


def test_g(self):
    self.assertEqual(10, count_all_arrangements("?###???????? 3,2,1"))
