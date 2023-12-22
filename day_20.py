def parse_configuration(f: str) -> (dict, dict, dict, dict):
    flip_flops, conjunctions, inputs, outputs, states = set(), set(), {}, {}, {}
    with open(f) as ifile:
        for line in ifile:
            parts = line.strip().split("->")
            module = parts[0].strip()
            if module != "broadcaster":
                module_name = module[1:]
                if module[0] == "%":
                    flip_flops.add(module_name)
                else:
                    conjunctions.add(module_name)
            else:
                module_name = module
            states[module_name] = 0
            conn = []
            for m in parts[1].split(","):
                conn.append(m.strip())
            outputs[module_name] = conn

    for conjunction in conjunctions:
        input = {}
        for module, output in outputs.items():
            if conjunction in output:
                input[module] = 0
        inputs[conjunction] = input
    return flip_flops, conjunctions, inputs, outputs, states


def process(flip_flops: set, conjunctions: set, inputs: dict, outputs: dict, states: dict, counts: dict):
    pulses = []
    counts["low"] += 1
    for module in outputs["broadcaster"]:
        pulses.append(("broadcaster", module, 0))

    while len(pulses) != 0:
        new_pulses = []
        for pulse in pulses:
            src, dst, signal = pulse[0], pulse[1], pulse[2]
            if signal == 0:
                counts["low"] += 1
            else:
                counts["high"] += 1

            if dst in flip_flops:
                if signal == 0:
                    new_signal = 1 if states[dst] == 0 else 0
                    states[dst] = new_signal
                    for next_module in outputs[dst]:
                        new_pulses.append((dst, next_module, new_signal))
            elif dst in conjunctions:
                inputs[dst][src] = signal
                states[dst] = signal
                new_signal = 0
                for state in inputs[dst].values():
                    if state == 0:
                        new_signal = 1
                        break
                for next_module in outputs[dst]:
                    new_pulses.append((dst, next_module, new_signal))
            else:
                states[dst] = signal
        pulses = new_pulses


flip_flops, conjunctions, inputs, outputs, states = parse_configuration("day_20.txt")
counts = {"high": 0, "low": 0}

for _ in range(1000):
    process(flip_flops, conjunctions, inputs, outputs, states, counts)

print(counts["low"] * counts["high"])
