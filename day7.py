# Open day7.txt file
from functools import lru_cache
from typing import Any

with open('./inputs/day7.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

example = '''
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''.strip().splitlines()

# Enable example
# lines = example

# Process first line to ge the initial beam location
beam_indexes = {lines[0].index('S')}
splits = 0

def process_line(line, indexes) -> tuple[int, set[Any]]:
    new_indexes = set()
    new_splits = 0

    for index in indexes:
        if line[index] == '^':
            new_indexes.add(index-1)
            new_splits += 1
            new_indexes.add(index + 1)
        else:
            new_indexes.add(index)

    return new_splits, new_indexes

for line in lines[1:]:
    current_splits, current_indexes = process_line(line, beam_indexes)
    splits += current_splits
    beam_indexes = current_indexes

print(f'The beam splits off at {splits} points')

# Part 2

line_count = len(lines)

# Memoization
@lru_cache(maxsize=None)
def process_quantum_line(line_number=0, beam_position=None) -> int:

    if line_number == line_count - 1:
        return 1

    # Find the first beam
    if line_number == 0:
        position = lines[0].index('S')
        return process_quantum_line(1, position)

    split_positions = [i for i, ch in enumerate(lines[line_number]) if ch == '^']

    if beam_position in split_positions:
        return process_quantum_line(line_number + 1, beam_position - 1) + process_quantum_line(line_number + 1, beam_position + 1)
    else:
        return process_quantum_line(line_number + 1, beam_position)


print(f'The quantum beam exists on {process_quantum_line()} timelines')