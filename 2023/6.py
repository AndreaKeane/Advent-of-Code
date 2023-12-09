
test_races = [
    {
        "race_duration_ms": 7, 
        "record_distance_mm": 9
    }, 
    {
        "race_duration_ms": 15, 
        "record_distance_mm": 40
    }, 
    {
        "race_duration_ms": 30, 
        "record_distance_mm": 200
    }
]

test2_races = [
    {
        "race_duration_ms": 71530, 
        "record_distance_mm": 940200
    }
]

my_races = [
    {
        "race_duration_ms": 55, 
        "record_distance_mm": 401
    },
    {
        "race_duration_ms": 99, 
        "record_distance_mm": 1485
    },
    {
        "race_duration_ms": 97, 
        "record_distance_mm": 2274
    },
    {
        "race_duration_ms": 93, 
        "record_distance_mm": 1405
    }
]

my_races2 = [
    {
        "race_duration_ms": 55999793, 
        "record_distance_mm": 401148522741405
    }
]


def main(input): 

    product_of_ways_to_win = 1
    for race in input: 
        duration = race["race_duration_ms"]
        distance_record = race["record_distance_mm"]
        ways_to_win = 0
        for button_hold in range(1, duration):
            speed = button_hold
            time_moving = duration - button_hold
            distance = speed * time_moving
            if distance > distance_record: 
                ways_to_win += 1
        product_of_ways_to_win *= ways_to_win
    
    print(f"Part 1 Answer: {product_of_ways_to_win}")


if __name__ == "__main__":

    main(my_races2)