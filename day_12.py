import functools


# could not solve :(
# from https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

@functools.cache
def get_number_of_arrangement(record: str, groups: tuple) -> int:
    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that aren't in the groups
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound-sign "#"
    def pound():
        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return get_number_of_arrangement(record[next_group + 1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as dot "."
    def dot():
        return get_number_of_arrangement(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    # Help with debugging
    print(record, groups, "->", out)
    return out


def count_all_arrangements(record: str) -> int:
    parts = record.split(" ")
    groups = tuple([int(x) for x in parts[1].split(",")])
    return get_number_of_arrangement("?".join([parts[0].strip()] * 5), groups * 5)


result = 0
with open('day_12.txt') as ifile:
    for record in ifile:
        result += count_all_arrangements(record.strip())

print(result)
