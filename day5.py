# Open day5.txt file
with open('./inputs/day5.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

example = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32'''.strip().splitlines()

# lines = example

adding = True
available_fresh_count = 0
total_fresh_count = 0
ranges = []

def binary_search(value, l):
    count = len(l)
    middle = count // 2
    above_bottom = value >= l[middle][0]
    below_top = value <= l[middle][1]

    if above_bottom and below_top:
        return 1

    if count < 2:
        return 0

    if above_bottom:
        return binary_search(value, l[middle:])
    else: #elif below_top:
        return binary_search(value, l[:middle])

def merge_ranges(l):
    # If list is empty return zero
    if len(l) == 0:
        return []

    # Sort by the start of the ranges
    l.sort(key=lambda t: t[0])

    current_low, current_high = l[0]
    merged = []

    # Starting with the first range compare the next
    for low, high in l[1:]:
        # Don't overlap so append the current and compare next
        if current_high < low:
            merged.append((current_low, current_high))
            current_low, current_high = (low, high)
        # Overlap - Extend the range to the right -> Can only be larger since we sort
        else:
            current_high = max(current_high, high)

    # Add the last one
    merged.append((current_low, current_high))

    return merged

if __name__ == '__main__':
    for line in lines:

         # If switching to search remove the overlaps
        if line == '':
            adding = False
            ranges = merge_ranges(ranges)
            continue

        # Read from the file and add the raw ranges to the list
        if adding:
            starting, finishing = map(int, line.split('-'))
            ranges.append((starting, finishing))
        else:
            # Find id in list of ranges using binary search log n
            # If exists add 1, else add 0 (returned by binary_search
            identifier = int(line)
            available_fresh_count += binary_search(identifier, ranges)

    # Sum all ranges
    for r in ranges:
        total_fresh_count += r[1] - r[0] + 1

    print(f'{available_fresh_count} available IDs are fresh')
    print(f'{total_fresh_count} total IDs are fresh')
