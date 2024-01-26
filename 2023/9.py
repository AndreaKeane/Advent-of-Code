
test_input = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def check_all_zeros(row):
    return all(n == 0 for n in row)


def get_differences(row): 
    diff_row = []
    for i in range(1, len(row)):
        diff_row.append(int(row[i]) - int(row[i-1]))
    
    return diff_row


def main(input):

    sum_of_next_values = 0
    for row in input: 
        # Split string into numbers 
        row = [int(n) for n in row.split(" ")]

        # Work it down to zeros 
        row_builder = [row]
        while not check_all_zeros(row_builder[-1]): 
            diffs = get_differences(row_builder[-1])
            row_builder.append(diffs)

        # Add back up to the next value 
        new_value = 0
        row_builder.reverse()
        row_builder[0].append(0)
        for i in range(1, len(row_builder)): 
            new_value = row_builder[i][-1] + row_builder[i-1][-1]
            row_builder[i].append(new_value)

        # Store the next value 
        sum_of_next_values += new_value

    print(f"Part 1 Answer: {sum_of_next_values}")


if __name__ == "__main__":

    input = []
    with open('9_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)