

test_input = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#....."
]


def dist(pos1, pos2):
    y1, z1 = pos1
    y2, x2 = pos2
    return abs(x2 - x1) + abs(y2 - y1)


def main(input):

    # Double the empty rows 
    # TODO: Double the empty columns
    expanded = []
    for row in input: 
        if row == len(row) * row[0]: 
            expanded.append(row)
        expanded.append(row)
    
    # for row in expanded: 
    #     print(row)

    # Find the positions  
    positions = []
    for row_idx, row in enumerate(expanded): 
        for col_idx, char in enumerate(row): 
            if char == "#": 
                positions.append((row_idx, col_idx))
    # print(positions)

    # Calculate the shortest path  
    sum_of_distances = 0
    for pos_idx, pos1 in enumerate(positions): 
        for pos2 in positions[pos_idx + 1:]: 
            dist = dist(pos1, pos2)
    sum_of_distances += dist
    print("Part 1 Answer: {sum_of_distances}")


if __name__ == "__main__":

    input = []
    with open('11_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(test_input)
    