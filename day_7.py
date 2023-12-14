from functools import cmp_to_key

card_values = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2,
               "2": 1}
new_card_values = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                   "J": 1}
kinds = {"5K": [], "4K": [], "FH": [], "3K": [], "2P": [], "1P": [], "HK": []}
new_kinds = {"5K": [], "4K": [], "FH": [], "3K": [], "2P": [], "1P": [], "HK": []}
value_map = {}


def compare_card(left_card: str, right_card: str, card_values: dict) -> int:
    left, right = card_values[left_card], card_values[right_card]
    if left > right:
        return -1
    elif left < right:
        return 1
    else:
        return 0


def compare(left_hand: str, right_hand: str) -> int:
    for index in range(len(left_hand)):
        if left_hand[index] != right_hand[index]:
            return compare_card(left_hand[index], right_hand[index], card_values)


def compare2(left_hand: str, right_hand: str) -> int:
    for index in range(len(left_hand)):
        if left_hand[index] != right_hand[index]:
            return compare_card(left_hand[index], right_hand[index], new_card_values)


def count_ones(counts: dict) -> int:
    ones = 0
    for v in counts.values():
        if v == 1:
            ones += 1
    return ones


def get_kind(hand: str) -> str:
    counts = {}
    for i in range(len(hand)):
        counts[hand[i]] = counts.get(hand[i], 0) + 1
    if len(counts) == 1:
        return "5K"
    if len(counts) == 2:
        # 4,1
        # 3,2
        if count_ones(counts) == 1:
            return "4K"
        else:
            return "FH"
    if len(counts) == 3:
        # 2,2,1
        # 3,1,1
        if count_ones(counts) == 2:
            return "3K"
        else:
            return "2P"
    if len(counts) == 4:
        return "1P"
    if len(counts) == 5:
        return "HK"


def get_new_kind(old_kind: str, hand: str) -> str:
    jokers = 0
    for i in range(len(hand)):
        if hand[i] == "J":
            jokers += 1

    if jokers == 0:
        return old_kind
    if old_kind == "5K" or old_kind == "4K":
        return "5K"
    if old_kind == "FH":
        return "5K"
    if old_kind == "3K":
        return "4K"
    if old_kind == "2P":
        if jokers == 1:
            return "FH"
        else:
            return "4K"
    if old_kind == "1P":
        return "3K"
    if old_kind == "HK":
        return "1P"


with open('day_7.txt') as ifile:
    for line in ifile:
        parts = line.split()
        hand = parts[0].strip()
        value = int(parts[1].strip())
        value_map[hand] = value
        kinds[get_kind(hand)].append(hand)

for kind, hands in kinds.items():
    kinds[kind] = sorted(hands, key=cmp_to_key(compare))
    for hand in hands:
        new_kinds[get_new_kind(kind, hand)].append(hand)

for kind, hands in new_kinds.items():
    new_kinds[kind] = sorted(hands, key=cmp_to_key(compare2))

rank = len(value_map)
winnings = 0
for hands in kinds.values():
    for hand in hands:
        winnings += rank * value_map[hand]
        rank -= 1

print(winnings)

rank = len(value_map)
winnings = 0
for hands in new_kinds.values():
    for hand in hands:
        winnings += rank * value_map[hand]
        rank -= 1

print(winnings)
