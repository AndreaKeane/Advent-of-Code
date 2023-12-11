
instructions_string = "LLLRRRLLRLRLLRRRLRLRRLRRLRRRLRRLLLRLRRLLRLRRRLRRRLLLRLLLLRLRRLLLRRRLRRRLRLRRRLLLLRLRLLRRLLRRRLRRLRLRRRLRRRLLLRLRRRLRRRLRRLLRRLRRRLLRLRLRLRLRLRRRLRLRRLRLRLRLRRLRRLRLRLRRLLRRLRRRLRRLRRLRRRLRRLRLLRLRLLRRLRRRLRLRLRRLLRRLRRRLRRLRRRLRLRRRLRRLRLRRLRLRRLLLRRLRRLRRRLRLRRLRRRLRLRLRRLRLLRRRR"

instructions = [c for c in instructions_string]
test_input = [
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]


def get_next_direction(map, step_count): 
    direction_index = step_count % len(instructions)
    direction_char = instructions[direction_index]
    direction_bool = 0 if direction_char == "L" else 1
    return direction_bool


def parse_raw_map(input): 
    map = {}
    for row in input: 
        key, values = row.strip().split(" = ")
        values = values.replace("(", "").replace(")", "")
        left, right = values.split(", ")
        map[key] = (left, right)
    return map


def main(input): 

    map =  parse_raw_map(input)
    
    step = "AAA"
    step_count = 0
    while step != "ZZZ":
        direction = get_next_direction(map, step_count)
        step = map[step][direction]
        if step_count % 10 == 0: print(f"step {step_count}")
        step_count += 1

    print(f"Part 1 Answer: {step_count}")


if __name__ == "__main__":


    input = []
    with open('8_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)
    
