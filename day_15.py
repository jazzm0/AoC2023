def h(s: str) -> int:
    value = 0
    for i in range(len(s)):
        value += ord(s[i])
        value *= 17
        value %= 256
    return value


def check_hash_sum(sequence: str) -> int:
    result = 0
    for s in sequence.split(","):
        result += h(s.strip())
    return result


def sum_focusing_power(sequence: str) -> int:
    boxes = {}
    for k in range(256):
        boxes[k] = []
    lens = None
    for s in sequence.split(","):
        if s[-1] == "-":
            label = s[:-1]
            operation = "-"
        else:
            lens = int(s[-1])
            label = s[:-2]
            operation = "="

        key = h(label)
        box = boxes[key]
        found = False
        index = 0
        for index in range(len(box)):
            if box[index][0] == label:
                found = True
                break

        if operation == "=":
            if found:
                box[index] = (label, lens)
            else:
                box.append((label, lens))
        elif operation == "-" and found:
            del box[index]

        boxes[key] = box

    result = 0
    for k, v in boxes.items():
        box_value = 0
        for index in range(len(v)):
            box_value += (k + 1) * (index + 1) * (v[index][1])
        result += box_value
    return result


print(h("HASH"))
print(check_hash_sum("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"))
print(sum_focusing_power("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"))

with open('day_15.txt') as ifile:
    for line in ifile:
        print(sum_focusing_power(line.strip()))
