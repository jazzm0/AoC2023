def hash(s: str) -> int:
    value = 0
    for i in range(len(s)):
        value += ord(s[i])
        value *= 17
        value %= 256
    return value


def process(sequence: str) -> int:
    result = 0
    for s in sequence.split(","):
        result += hash(s.strip())
    return result


print(hash("HASH"))
print(process("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"))

with open('day_15.txt') as ifile:
    for line in ifile:
        print(process(line))
