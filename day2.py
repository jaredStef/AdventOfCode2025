# Open day4.txt file
with open('./inputs/day2.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]

ranges = [line.split('-') for line in lines[0].split(',')]
count = 0

for r in ranges:
    left = int(r[0])
    right = int(r[1])

    for i in range(left, right + 1):
        num_str = str(i)
        str_length = len(num_str)
        # Uncomment for part 1
        # is_even_length = str_length % 2 == 0

        # WONTFIX: You could optimize this to skip ahead for part 1
        # If we are at 100, we know 101, 102, 103... won't be an even count so we
        # can skip to the next order of magnitude

        # if not is_even_length:
        #     continue

        # Start part 2
        sequence = ''
        invalid = False

        for c in num_str:
            occurrences = num_str.count(sequence)
            if occurrences * len(sequence) == str_length:
                invalid = True
                break
            sequence += c

        if invalid:
            count += i
        # end part 2

        # Uncomment for part 1
        # middle = int(str_length / 2)
        # first_half = num_str[:middle]
        # second_half = num_str[middle:]
        #
        # if first_half == second_half:
        #     count += i

print(f'Sum of Invalid IDs: {count}')

