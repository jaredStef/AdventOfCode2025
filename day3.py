# Open day4.txt file
with open('./inputs/day3.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]


examples = '''
987654321111111
811111111111119
234234234234278
818181911112111'''.lstrip().split('\n')

# lines = examples
size = 2

def process_bank(bank):
    total = 0
    bank_size = len(bank)
    # Current digits
    larges = [-1] * size

    # If there are enough digits remaining to allow changing this digit
    def has_more(current_position, remaining_digits):
        return current_position < (bank_size - remaining_digits + 1)

    # For Each Cell
    for j in range(bank_size):
        cell = int(bank[j])

        # Check whether to update each of our values
        for k in range(size):
            # If the value is larger than our existing one
            # or our existing one is blank and hasn't been set yet
            # and there are enough digits left to allow us to replace the rest

            if (cell > larges[k] or larges[k] == -1) and has_more(j, size-k):
                # Change the digit
                larges[k] = cell
                # Set the rest to blank
                for l in range(k+1, size):
                    larges[l] = -1
                break

    # Sum each digit by raising it to a power of 10
    # Ex: 1, 3, 3, 4 = 1000 + 300 + 30 + 4
    for j in range(len(larges)):
        number = larges[j] * (10 ** (size - j - 1))
        total += number

    return total

if __name__ == '__main__':
    # Process each line containing a power bank
    amount = sum([process_bank(bank) for bank in lines])

    print(f'Joltages sum to: {amount}')
