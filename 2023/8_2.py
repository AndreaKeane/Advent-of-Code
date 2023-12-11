from math import gcd

instructions_string = "LLLRRRLLRLRLLRRRLRLRRLRRLRRRLRRLLLRLRRLLRLRRRLRRRLLLRLLLLRLRRLLLRRRLRRRLRLRRRLLLLRLRLLRRLLRRRLRRLRLRRRLRRRLLLRLRRRLRRRLRRLLRRLRRRLLRLRLRLRLRLRRRLRLRRLRLRLRLRRLRRLRLRLRRLLRRLRRRLRRLRRLRRRLRRLRLLRLRLLRRLRRRLRLRLRRLLRRLRRRLRRLRRRLRLRRRLRRLRLRRLRLRRLLLRRLRRLRRRLRLRRLRRRLRLRLRRLRLLRRRR"
instructions = [c for c in instructions_string]

test_input = [
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)"
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


def check_for_z(positions_list):
    last_chars_bools = [True if p[-1] == "Z" else False for p in positions_list ]
    all_end_with_z = all(last_chars_bools)
    # print(f"{positions_list} {all_end_with_z}")
    return all_end_with_z


def main_brute_force_soln(input): 

    map = parse_raw_map(input)

    current_positions = [p for p in map.keys() if p[-1] == "A"]
    
    step_count = 0
    temp_positions = []
    while not check_for_z(current_positions):
    # for i in range(10):
    #     i += 1
        direction = get_next_direction(map, step_count)
        for position in current_positions: 
            next_pos = map[position][direction]
            temp_positions.append(next_pos)
            if step_count % 10000 == 0: 
                print(f"{step_count} {direction} {current_positions} {temp_positions}")
        step_count += 1
        current_positions = temp_positions
        temp_positions = []
    print(f"Part 2 Answer: {step_count}")


def calc_lcm(list_of_ints):
    lcm = 1
    for i in list_of_ints:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


def main(input):

    map = parse_raw_map(input)

    initial_positions = {p: None for p in map.keys() if p[-1] == "A"}

    for ip in initial_positions.keys():
        step_count = 0
        step = ip
        while step[-1] != "Z":
            next_direction = get_next_direction(map, step_count)
            step = map[step][next_direction]
            step_count += 1
        initial_positions[ip] = int(step_count)
    
    print(initial_positions)
    
    lcm = calc_lcm(initial_positions.values())
    print(f"Part 2 Answer: {lcm}")


if __name__ == "__main__":

    input = []
    with open('8_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)
    