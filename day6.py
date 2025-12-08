import re

# Open day6.txt file
with open('./inputs/day6.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

example = '''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''.strip().splitlines()

# lines = example

# Part 1

numbers: list[list[str]] = []
# Remove duplicate spaces, split, and add number strings to a matrix
for line in lines:
    s = re.sub(r' +', ' ', line)
    numbers.append(s.split())

# Separate out final op row
ops = numbers.pop()

height = len(numbers)

width = len(numbers[0])

horizontal_total = 0

for i in range(width):
    column = []
    for j in range(height):
        column.append(numbers[j][i])
    # Join each line of number strings by their
    horizontal_total += eval(ops[i].join(column))

print(f'The horizontal left to right sum is\n{horizontal_total}')

# In part 1 I am parsing horizontal, so I can ignore the spaces
# In part 2 they mean the number's place and removing them changes the number's value
# I will parse it again, this time vertically

# We are now going char by char instead of token by token
# We must change the width from the number of tokens to the number of chars
width = len(lines[0])

column_number = 0
current_column = []
vertical_sum = 0

# For Each char wide
for x in range(width):
    column_string = ''
    # Append each char vertically
    for y in range(height):
        column_string += lines[y][x]

    all_spaces = column_string.isspace()

    # If not at the end of a line append it to the number we are building
    if not all_spaces:
        current_column.append(column_string)

    # If at the end of a line, construct the formula, sum, and reset
    if all_spaces or x == width - 1:
        result = eval(ops[column_number].join(current_column).replace(' ', ''))
        vertical_sum += result
        current_column = []
        column_number += 1

print(f'\nThe vertical top to bottom sum is\n{vertical_sum}')
