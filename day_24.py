from typing import List


def get_paths(f: str) -> List[tuple]:
    paths = []
    with open(f) as ifile:
        for line in ifile:
            pv = line.strip().split("@")
            p = pv[0].strip().split(",")
            v = pv[1].strip().split(",")
            position = (int(p[0].strip()), int(p[1].strip()), int(p[2].strip()))
            velocity = (int(v[0].strip()), int(v[1].strip()), int(v[2].strip()))
            paths.append((position, velocity))
    return paths


# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def get_det(a: tuple, b: tuple, c: tuple, d: tuple) -> tuple:
    div = (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])
    if div == 0:
        return None
    return (a[0] * b[1] - a[1] * b[0]) * (c[0] - d[0]) - (a[0] - b[0]) * (c[0] * d[1] - c[1] * d[0]) / div, (
            a[0] * b[1] - a[1] * b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] * d[1] - c[1] * d[0]) / div


def add(point: tuple, velocity: tuple) -> tuple:
    return point[0] + velocity[0], point[1] + velocity[1], point[2] + velocity[2]


def get_collision(a: tuple, b: tuple) -> tuple:
    point_a = a[0]
    velocity_a = a[1]
    point_b = b[0]
    velocity_b = b[1]
    return get_det(point_a, add(point_a, velocity_a), point_b, add(point_b, velocity_b))


def get_collisions(paths: List[tuple]):
    n = len(paths)
    for i in range(n):
        for j in range(i + 1, n):
            c = get_collision(paths[i], paths[j])
            if c is not None:
                print(c)


print(get_collisions(get_paths("day_24_small.txt")))
