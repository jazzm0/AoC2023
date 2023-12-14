from typing import List

times, distances = [], []
total_time, total_distance = 0, 0


def convert(s: str) -> List[int]:
    return [int(x) for x in s.split(":")[1].split() if x.strip() != ""]


def convert2(s: str) -> int:
    r = ""
    for part in [x for x in s.split(":")[1].split() if x.strip() != ""]:
        r += part
    return int(r)


def count(time: int, distance: int) -> int:
    wins = 0
    for t in range(time):
        if (time - t) * t > distance:
            wins += 1
    return wins


with open('day_6.txt') as ifile:
    for line in ifile:
        if line.find("Time:") >= 0:
            times = convert(line)
            total_time = convert2(line)
        elif line.find("Distance:") >= 0:
            distances = convert(line)
            total_distance = convert2(line)
ways = 1

for i in range(len(times)):
    ways *= count(times[i], distances[i])

print(ways)

print(count(total_time, total_distance))
