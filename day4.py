# Open day4.txt file
from typing import List, Tuple

with open('./inputs/day4.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

example = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''.lstrip().splitlines()

# Run Example
lines = example

# Convert str to list of char for assignment
lines = [list(row) for row in lines]

total_removed = 0
width = len(lines[0])
height = len(lines)

rolls_to_remove: List[Tuple[int, int]] = []

def safe_access(row, col) -> int:
    if col < 0 or col >= width or row < 0 or row >= height:
        return 0
    else:
        return is_roll(lines[row][col])

def is_roll(s) -> int:
    return 1 if s == "@" else 0

def safe_adjacent_sum(row, col) -> int:
    neighbors = 0
    combinations = [(a, b) for a in (1, 0, -1) for b in (1, 0, -1)]

    for a, b in combinations:
        if a == 0 and b == 0:
            continue
        neighbors += safe_access(row + a, col + b)

    return neighbors

while True:
    for row_num in range(height):
        for col_num in range(width):
            node = lines[row_num][col_num]
            if node == '.':
                continue

            rolls = safe_adjacent_sum(row_num, col_num)

            if rolls < 4:
                rolls_to_remove.append((row_num, col_num))

    for roll in rolls_to_remove:
        lines[roll[0]][roll[1]] = '.'
    number_removed = len(rolls_to_remove)
    total_removed += number_removed

    if number_removed == 0:
        break

    rolls_to_remove = []
    print(f'{number_removed} removed')

print('-------')
print(f'Total is {total_removed}')
