

test_input = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

class Number: 
    number_str = ""
    adjacent_to_special_chars = False


def is_symbol(char):
    
    if char == "." or char.isdigit():
        return False
    else:
        return True


def check_adjacent_chars(raw_matrix, x, y): 

    adjacent_positions = [
        [x-1, y-1], [x, y-1], [x+1, y-1], # Above Row
        [x-1, y], [x+1, y],  # Same Row Left/Right
        [x-1, y+1], [x, y+1], [x+1, y+1]  # Below Row
    ]

    for pos in adjacent_positions: 
        col, row = pos
        if (col < 0) or (row < 0): 
            continue
        try: 
            char = raw_matrix[row][col]
            if is_symbol(char): 
                # print(f"{row+1}, {col+1}, {char}")
                return True
        except IndexError:  # Tried to access an Out of Bound position
            continue
    return False


def number_reset(final_sum, number):
    if number.number_str: 
        # print(f"{number} - {adjacent_to_special_chars} - {final_sum}")
        if number.adjacent_to_special_chars: 
            final_sum += int(number.number_str)
    return final_sum, Number()


def main(raw_matrix):

    final_sum = 0
    number = Number()

    for idx_row, line in enumerate(raw_matrix): 
        for idx_col, char in enumerate(line): 
            if char.isdigit():
                number.number_str += str(char)
                if not number.adjacent_to_special_chars: 
                    number.adjacent_to_special_chars = check_adjacent_chars(raw_matrix, idx_col, idx_row)
            else: # Sum up results and then reset variables 
                final_sum, number = number_reset(final_sum, number)

        final_sum, number = number_reset(final_sum, number)
    
    print("Part 1 Answer: ", final_sum)


if __name__ == "__main__":

    input = []
    with open('3_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row.strip())

    main(input)