from typing import List

times, distances = [], []


def convert(s: str) -> List[int]:
    return [int(x) for x in s.split(":")[1].split(" ") if x.strip() != ""]


with open('day_6.txt') as ifile:
    for line in ifile:
        if line.find("Time:") >= 0:
            times = convert(line)
        elif line.find("Distance:") >= 0:
            distances = convert(line)
ways = 1

for i in range(len(times)):
    wins = 0
    for t in range(times[i]):
        speed = t
        if (times[i] - t) * speed > distances[i]:
            wins += 1
    ways *= wins

print(ways)
