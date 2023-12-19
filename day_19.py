from typing import List


def parse_instructions(f: str) -> tuple:
    workflows = {}
    machine_parts = []
    is_workflow = True
    with open(f) as ifile:
        for line in ifile:
            if line.strip() == "":
                is_workflow = False
                continue
            if is_workflow:
                wf_parts = line.strip().split("{")
                wf_name = wf_parts[0]
                # mb{x>643:R,x>308:cp,a>397:A,xck}
                rule_pipeline = []
                rules = wf_parts[1][:-1].split(",")
                for rule in rules:
                    rule_parts = rule.split(":")
                    if len(rule_parts) == 2:
                        rule_pipeline.append((rule_parts[0], rule_parts[1]))
                    elif len(rule_parts) == 1:
                        rule_pipeline.append((True, rule_parts[0]))
                    else:
                        raise RuntimeError
                workflows[wf_name] = rule_pipeline
            else:
                values = {}
                for pv in line.strip()[1:-1].split(","):
                    pv_parts = pv.split("=")
                    values[pv_parts[0]] = int(pv_parts[1])
                machine_parts.append(values)
    return workflows, machine_parts


def process_part(workflows: dict, machine_part: dict) -> bool:
    wf = "in"
    while True:
        pipeline = workflows[wf]
        for pp in pipeline:
            wf = pp[1]
            condition = False
            if type(pp[0]) is bool:
                condition = True
            else:
                key = pp[0][0]
                operator = pp[0][1]
                value = int(pp[0][2:])

                if operator == ">":
                    if machine_part[key] > value:
                        condition = True
                elif operator == "<":
                    if machine_part[key] < value:
                        condition = True
                else:
                    raise RuntimeError
            if condition:
                if wf == "A":
                    return True
                elif wf == "R":
                    return False
                else:
                    break


def get_parts_values(workflows: dict, machine_parts: List) -> int:
    s = 0
    for machine_part in machine_parts:
        if process_part(workflows, machine_part):
            for v in machine_part.values():
                s += v
    return s


workflows, machine_parts = parse_instructions("day_19.txt")
print(get_parts_values(workflows, machine_parts))
