# Open day4.txt file
with open('./inputs/day1.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

if len(lines) == 0:
    print('Unable to load day4.txt file')
    exit(1)

position = 50
size = 100

# DEBUG
# example = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
# lines = example

# left from 0 (so negatives) -> 99
# Right from 99 moves to 0

zeros = 0
crossed_zeros = 0

for command in lines:
    direction = command[0]
    distance = int(command[1:])
    sign = -1 if direction == 'L' else 1

    # direction is relative to the current arrow
    # left distance from zero = position
    # right distance from zero = size - position
    distance_from_zero = position if direction == 'L' else size - position

    if distance_from_zero == 0:
        distance_from_zero = 100

    if distance_from_zero <= distance:
        crossed_zeros += 1
        crossed_zeros += (distance - distance_from_zero) // size

    position += sign * distance
    position %= size

    if position == 0:
        zeros += 1

print(f'Final Position: {position}')
print(f'Landed on Zero: {zeros} times')
print(f'Crossed Zero: {crossed_zeros} times')
