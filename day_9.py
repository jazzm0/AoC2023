from typing import List


def generate_next_sequence(sequence: List[int]) -> (List[int], bool):
    new_sequence = []
    all_zeroes = True
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        new_sequence.append(diff)
        if all_zeroes and diff != 0:
            all_zeroes = False
    return new_sequence, all_zeroes


sequences = []
with open('day_9.txt') as ifile:
    for line in ifile:
        sequence = []
        for n in line.strip().split(" "):
            if n != "":
                sequence.append(int(n))
        sequences.append(sequence)

result, previous_sum = 0, 0
for sequence in sequences:
    all_zeroes = False
    extrapolated_values = []
    while not all_zeroes:
        extrapolated_values.append(sequence)
        result += sequence[- 1]
        sequence, all_zeroes = generate_next_sequence(sequence)
    previous = 0
    for i in range(len(extrapolated_values) - 1, -1, -1):
        previous = extrapolated_values[i][0] - previous
    previous_sum += previous

print(result)
print(previous_sum)
