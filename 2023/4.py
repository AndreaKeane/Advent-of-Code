from collections import OrderedDict

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

    return {"id": card_id, "my_numbers": my_numbers_list, "win_numbers": winning_numbers_list, "matches": matches, "score": score}


def update_copies_counter(copies_counter, id):
    if id in copies_counter.keys(): 
        copies_counter[id] += 1
    else: 
        copies_counter[id] = 1
    return copies_counter


def generate_copies(copies_counter, card): 
    for idx, match in enumerate(card["matches"]):
        copy_card_id = int(card["id"]) + idx + 1
        copies_counter = update_copies_counter(copies_counter, f"{copy_card_id}")
    return copies_counter


def main(input):

    score = 0  # Part 1 
    cards = {}
    copies_counter = {}  # Part 2

    for row in input: 
        card = parse_card(row)
        score += card["score"]
        # Store information for part 2
        copies_counter = update_copies_counter(copies_counter, card["id"])
        cards[card["id"]] = card
    print(f"Part 1 Answer: {score}")

    card_id_list = [int(id) for id in cards.keys()]
    card_id_list.sort()

    for card_id in card_id_list: 
        card_id = str(card_id)
        card = cards[card_id]
        copy_count = copies_counter[card_id]
        # print(card_id, copy_count)
        for i in range(copy_count): 
            copies_counter = generate_copies(copies_counter, card)
    
    copy_count = 0
    for card_id, count in copies_counter.items(): 
        copy_count += count
    print(f"Part 2 Answer: {copy_count}")


if __name__ == "__main__":

    input = []
    with open('4_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)