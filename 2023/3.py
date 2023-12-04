import re

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


class Position:

    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
        self.adjacent_positions = [
            [x-1, y-1], [x, y-1], [x+1, y-1], # Above Row
            [x-1, y], [x+1, y], 
            [x-1, y+1], [x, y+1], [x+1, y+1]  # Below Row
            ]


def is_symbol(char):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    
    if(regex.search(char) == None):
        return False
    else:
        return True


def index_the_matrix(raw_matrix):
    symbol_positions = []
    matrix_dict = {}
    for row_idx, row in enumerate(raw_matrix): 
        for col_idx, char in enumerate(row): 
            matrix_dict[row_idx] = row
            if is_symbol(char): 
                symbol_pos = Position(row_idx, col_idx)
                symbol_positions.append(symbol_pos)

    return matrix_dict, symbol_positions


def check_adjacent_digits(matrix_dict, position): 
    
    adjacent_digits = []

    for adj in position.adjacent_positions:
        x_adj, y_adj = adj
        char = matrix_dict[y_adj][x_adj]
        if char.isdigit(): 
            adjacent_digits.append(adj)
    return adjacent_digits


def main(raw_matrix):

    matrix_dict, symbol_positions = index_the_matrix(raw_matrix)

    for pos in symbol_positions:
        adjacent_digits = check_adjacent_digits(matrix_dict, pos)
        print(adjacent_digits)


if __name__ == "__main__":

    input = []
    with open('3_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(test_input)