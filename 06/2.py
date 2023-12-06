def calculate_distance_mm(stay_ms, total_time_ms):
    speed = stay_ms
    remaining_time = total_time_ms - stay_ms
    distance = remaining_time * speed

    return distance


def ways_to_beat_record(time_ms, record_distance_mm):
    res = []
    for x in range(time_ms + 1):
        d = calculate_distance_mm(x, time_ms)
        if d > record_distance_mm:
            res.append(x)

    return res


if __name__ == '__main__':
    # race_time = 71530
    # record_distance = 940200

    race_time = 59707878
    record_distance = 430121812131276


    w = ways_to_beat_record(race_time, record_distance)

    print(w)
    print(len(w))

