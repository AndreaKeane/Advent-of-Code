
bag_max = {
    "blue": 14,
    "red": 12,
    "green": 13
}

test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]


def parse_game_id(game_id_str): 
    # Get digits only 
    digits = [d for d in game_id_str if d.isdigit()]
    
    # Concat digits back into a string
    digits_str = ''.join(digits)

    # Convert string to int 
    return int(digits_str)


def get_color_number(color_str): 
    count = parse_game_id(color_str)
    color = ''.join([c for c in color_str if c.isalpha()])
    return color, count


def main(list_of_games): 

    invalid_round_sum = 0

    for game in list_of_games:
        possible_game = True
        game_id_str, results = game.split(":", 1)
        game_id_int = parse_game_id(game_id_str)
        
        rounds = results.split(";")

        print(game_id_int, rounds)
        for round in rounds: 
            sep_list = round.split(",")
            for sep in sep_list: 
                color, count = get_color_number(sep)
                if (count > bag_max[color]): 
                    possible_game = False
        
        if possible_game: 
            invalid_round_sum += game_id_int


    print(f"Answer: {invalid_round_sum}")


if __name__ == "__main__":

    input = []
    with open('2_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)
    
