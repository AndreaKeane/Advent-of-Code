

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


def main(raw_matrix):

    final_sum = 0

    for idx_row, line in enumerate(raw_matrix): 
        
        number = ""
        adjacent_to_special_chars = False
        for idx_col, char in enumerate(line): 
            if char.isdigit(): 
                number = f"{number}{char}"
                # Check for neighboring special characters
                if not adjacent_to_special_chars: 
                    adjacent_to_special_chars = check_adjacent_chars(raw_matrix, idx_col, idx_row)

            else: # Sum up results and then reset variables 
                if number: 
                    # print(f"{number} - {adjacent_to_special_chars} - {final_sum}")
                    if adjacent_to_special_chars: 
                        final_sum += int(number)
                number = ""
                adjacent_to_special_chars = False
        
        if number: 
            # print(f"{number} - {adjacent_to_special_chars} - {final_sum}")
            if adjacent_to_special_chars: 
                final_sum += int(number)
            number = ""
            adjacent_to_special_chars = False
    
    print("Part 1 Answer: ", final_sum)


if __name__ == "__main__":

    input = []
    with open('3_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row.strip())

    main(input)