test_input = [
    "test",
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def replace_str_with_digit(str):

    for spelling, digit in valid_digits.items(): 
        replacement = spelling[0] + digit + spelling [-1]
        str = str.replace(spelling, replacement)
    
    return str


def get_summed_digits(line) -> int: 
    
    digitized_line = replace_str_with_digit(line.lower()) # Example: "one" --> "1"
    only_digits = [char for char in digitized_line if char.isdigit()]  # Example: "t2o1n9e" --> [2, 1, 9]
    if not only_digits: return 0  # Assumption to handle string without digits
    
    summed_digits = f"{only_digits[0]}{only_digits[-1]}"
    # print(line, " -- ", digitized_line, " -- ", summed_digits)
    return int(summed_digits)


def main(input_list): 
    
    sum = 0 # Becomes final answer, incremented for each input string
    for line in input_list: 
        sum += get_summed_digits(line)
        
    print("Final Answer: ", sum)


if __name__ == "__main__":

    input = []
    with open('input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)
    
