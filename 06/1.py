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
    # input = {
    #     7: 9,
    #     15: 40,
    #     30: 200
    # }
    input = [
        (59, 430),
        (70, 1218),
        (78, 1213),
        (78, 1276)
    ]

    acc = []
    for race_time, record_distance in input:
        n_ways = len(ways_to_beat_record(race_time, record_distance))
        acc.append(n_ways)

    print(acc)

    acc_n = 1
    for x in acc:
        acc_n *= x

    print(acc_n)
