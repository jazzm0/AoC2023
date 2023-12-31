result = 0
card_matches = {}
card_instances = {}


def get_card_value(s: str) -> int:
    s = s.strip().split(":")
    card_number = int(s[0].replace("Card", "").strip())
    numbers = s[1].split("|")
    winning_numbers, matches = set(), 0
    for winning_number in numbers[0].split():
        if winning_number != "":
            winning_numbers.add(winning_number.strip())
    for number in numbers[1].split():
        if number.strip() in winning_numbers:
            matches += 1
    card_matches[card_number] = matches
    card_instances[card_number] = 1
    if matches > 0:
        return 2 ** (matches - 1)
    else:
        return 0


with open('day_4.txt') as ifile:
    for line in ifile:
        result += get_card_value(line)

# for line in ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#              "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#              "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#              "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#              "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#              "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]:
#     result += get_card_value(line)

for card in range(1, len(card_instances) + 1):
    for next_card in range(card_matches[card]):
        card_instances[next_card + card + 1] += card_instances[card]

card_counts = 0
for card_count in card_instances.values():
    card_counts += card_count

print(result)
print(card_counts)
