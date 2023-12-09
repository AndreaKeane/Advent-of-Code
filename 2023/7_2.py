from collections import Counter


test_input = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

sort_priority = {
    "A": "a",
    "K": "b",
    "Q": "c",
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m", 
    "J": "n",
}


def categorize_list_of_hands(list_of_hands): 

    queue = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }

    for h in list_of_hands: 
        hand, bid = h.split(" ")
        category = categorize_hand(hand)
        priority = ''.join([sort_priority[i] for i in hand])
        queue[category].append(f"{priority} {h}")
    
    return queue


def categorize_hand(hand): 
    cards = [c for c in optimize_j(hand)]
    counter = Counter(cards)
    category = None

    keys = counter.keys()
    values = counter.values()

    if len(keys) == 1: 
        category = "five_of_a_kind"
    elif len(keys) == 2: 
        if max(values) == 4: 
            category = "four_of_a_kind"
        else: 
            category = "full_house"
    elif len(keys) == 3: 
        if max(values) == 3: 
            category = "three_of_a_kind"
        else: 
            category = "two_pair"
    elif len(keys) == 4: 
        category = "one_pair"
    else: 
        category = "high_card"
    
    return category


def optimize_j(hand_in): 
    cards = [c for c in hand_in]
    counter = Counter(cards)

    hand_out = str(hand_in)
    if "J" in counter.keys() and len(counter.keys()) > 1: 
        most_common = [c[0] for c in counter.most_common() if c[0] != "J"][0]
        hand_out = hand_out.replace("J", most_common)
    
    # print(f"{hand_in}, {hand_out}")
    return hand_out


def main(input): 

    queue = categorize_list_of_hands(input)
    
    # Sort the cards 
    final_list = []
    for category, hands in queue.items():
        hands = sorted(hands)
        for h in hands: 
            final_list.append(h)
    # print(final_list)

    # Score the cards
    part_1_score = 0
    for idx, hand in enumerate(reversed(final_list)): 
        sort_priority, cards, bid = hand.split(" ")
        part_1_score += (int(bid) * (idx + 1))
    print(f"Part 7 Answer: {part_1_score}")


if __name__ == "__main__":

    input = []
    with open('7_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    main(input)
