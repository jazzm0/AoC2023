from typing import List

sequences = []


def generate_next_sequence(sequence: List[int]) -> (List[int], bool):
    new_sequence = []
    all_zeroes = True
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        new_sequence.append(diff)
        if all_zeroes and diff != 0:
            all_zeroes = False
    return new_sequence, all_zeroes


with open('day_9.txt') as ifile:
    for line in ifile:
        sequence = []
        for n in line.strip().split(" "):
            if n != "":
                sequence.append(int(n))
        sequences.append(sequence)
result = 0
for sequence in sequences:
    all_zeroes = False
    extrapolated_values = []
    while not all_zeroes:
        extrapolated_values.append(sequence)
        result += sequence[- 1]
        sequence, all_zeroes = generate_next_sequence(sequence)

print(result)
