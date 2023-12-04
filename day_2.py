def is_game_valid(s: str, color: str, limit: int) -> bool:
    if s.find(color) > 0:
        amount = int(s.replace(color, "").strip())
        if amount > limit:
            return False
    return True


def get_min_amount(s: str, color: str) -> int:
    if s.find(color) > 0:
        return int(s.replace(color, "").strip())
    return 0


def is_possible(s: str) -> int:
    s = s.split(":")
    game_id = int(s[0].replace("Game", "").strip())
    sets = s[1].split(";")
    for sub_set in sets:
        colors = sub_set.split(",")
        for color in colors:
            if not is_game_valid(color, "red", 12):
                return 0

            if not is_game_valid(color, "green", 13):
                return 0

            if not is_game_valid(color, "blue", 14):
                return 0

    return game_id


def get_min_cube_count(s: str) -> int:
    red, green, blue = 1, 1, 1
    sets = s.split(":")[1].split(";")
    for sub_set in sets:
        colors = sub_set.split(",")
        for color in colors:

            min_red = get_min_amount(color, "red")
            if min_red > red:
                red = min_red

            min_green = get_min_amount(color, "green")
            if min_green > green:
                green = min_green

            min_blue = get_min_amount(color, "blue")
            if min_blue > blue:
                blue = min_blue

    return red * green * blue


with open('day_2.txt') as ifile:
    sum, min_amount_factor = 0, 0
    for line in ifile:
        sum += is_possible(line)
        min_amount_factor += get_min_cube_count(line)

print(sum)
print(min_amount_factor)
