
test_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

def parse_card(row): 
    id_txt, values_txt = row.split(":", 1)
    card_id = ''.join([c for c in id_txt.strip() if c.isdigit()])
    my_numbers_txt, winning_numbers_txt = values_txt.strip().split("|", 1)
    my_numbers_list = [n for n in my_numbers_txt.strip().split(" ") if n]
    winning_numbers_list = [n for n in winning_numbers_txt.strip().split(" ") if n]
    matches = [n for n in my_numbers_list if n in winning_numbers_list]
    score = ( 2 ** (len(matches)  - 1) ) if matches else 0
    # print(True if len(set(winning_numbers_list)) != 25 else False)
    print(my_numbers_list, True if len(set(my_numbers_list)) == 10 else False)

    return {"id": card_id, "my_numbers": my_numbers_list, "win_numbers": winning_numbers_list, "matches": matches, "score": score}


def main(input):
    cards = []
    score = 0
    for row in input: 
        card = parse_card(row)
        score += card["score"]
    print(score)


if __name__ == "__main__":

    input = []
    with open('4_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)