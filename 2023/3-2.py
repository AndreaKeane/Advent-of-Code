

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

asterisks = set()
numbers = {}


class Number: 
    number_str = ""
    adjacent_to_special_chars = False

    def __repr__(self):
        return f'{self.number_str}'
    
    def __str__(self):
        return f'{self.number_str}'


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


def check_adjacent_numbers(y, x): 

    adjacent_positions = [
        [x-1, y-1], [x, y-1], [x+1, y-1], # Above Row
        [x-1, y], [x+1, y],  # Same Row Left/Right
        [x-1, y+1], [x, y+1], [x+1, y+1]  # Below Row
    ]

    adjacent_numbers = set()

    for pos in adjacent_positions: 
        col, row = pos
        if (col < 0) or (row < 0): 
            continue
        try: 
            key = f"{row}, {col}"
            print(key)
            if key in numbers.keys():
                adjacent_numbers.add(numbers[key])
        except IndexError:  # Tried to access an Out of Bound position
            continue
    
    print(adjacent_numbers)
    if len(adjacent_numbers) == 2: 
        num1, num2 = adjacent_numbers
        return int(num1.number_str) * int(num2.number_str)
    return 0


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
                numbers[f"{idx_row}, {idx_col}"] = number
                if not number.adjacent_to_special_chars: 
                    number.adjacent_to_special_chars = check_adjacent_chars(raw_matrix, idx_col, idx_row)
            else: # Sum up results and then reset variables 
                final_sum, number = number_reset(final_sum, number)
                if char == "*": 
                    asterisks.add((idx_row, idx_col))

        final_sum, number = number_reset(final_sum, number)
    
    print("Part 1 Answer: ", final_sum)

    print(numbers)
    sum_of_powers = 0
    for a in asterisks: 
        print(a)
        sum_of_powers += check_adjacent_numbers(*a)
        
    print(sum_of_powers)


if __name__ == "__main__":

    input = []
    with open('3_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row.strip())

    main(input)