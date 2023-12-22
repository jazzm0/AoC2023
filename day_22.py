from typing import List


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


bricks = get_bricks("day_22.txt")
