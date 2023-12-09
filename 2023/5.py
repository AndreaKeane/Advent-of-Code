
test_input = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4", 
    ""
]


def parse_ranges(line):
    split = [val for val in line.strip().split(" ") if val]
    v = {
        "dest_range_start": int(split[0].strip()),
        "src_range_start": int(split[1].strip()),
        "range_length": int(split[2].strip())
    }
    return v


def parse_maps(input): 
    try: 
        maps = {}
        for line in input: 
            if "seeds:" in line: 
                key = "seeds"
                values = line.replace("seeds: ", "").split(" ")
            elif ":" in line: 
                key = line.replace(" map:", "").strip()
                values = []
            elif line.strip() == "": 
                maps[key] = values
                key, values = ("", [])
            else: 
                values.append(parse_ranges(line))
        maps[key] = values
    except Exception as e: 
        print(line, e)
        exit()
    return maps


def get_seed_story(maps, seed_int): 
    soil = get_destination_value(maps["seed-to-soil"], seed_int)
    fertilizer = get_destination_value(maps["soil-to-fertilizer"], soil)
    water = get_destination_value(maps["fertilizer-to-water"], fertilizer)
    light = get_destination_value(maps["water-to-light"], water)
    temperature = get_destination_value(maps["light-to-temperature"], light)
    humidity = get_destination_value(maps["temperature-to-humidity"], temperature)
    location = get_destination_value(maps["humidity-to-location"], humidity)
    # print(f"{seed_int} --> {soil} --> {location}")
    return location


def get_destination_value(transition_map, source_id): 
    source_id = int(source_id)
    for line in transition_map: 
        if line["src_range_start"] <= source_id <= line["src_range_start"] + line["range_length"] - 1:
            delta = source_id - line["src_range_start"]
            return line["dest_range_start"] + delta
    return source_id


def main1(input): 
    maps = parse_maps(input)
    print(maps.keys())
    seeds = maps["seeds"]
    min_location_id = max([int(s) for s in seeds])
    for seed in seeds: 
        location_id = get_seed_story(maps, seed)
        min_location_id = min(min_location_id, location_id)
    print(f"Part 1 Answer: {min_location_id}")


def main2(input): 
    maps = parse_maps(input)
    m = maps["humidity-to-location"]
    for line in m: 
        min_line = line if line["dest_range_start"] == 0 else None
    
    print(min_line)


if __name__ == "__main__":

    input = []
    with open('5_input.txt', 'r') as input_file:
        for row in input_file:
            input.append(row)

    # main1(test_input)
    main2(test_input)