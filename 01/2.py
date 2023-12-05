numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def my_find_all(input_string, pattern):
    indexes = [input_string.find(pattern)]

    if indexes[0] < 0:
        return indexes

    next_step_str = input_string[indexes[-1] + len(pattern):]
    while len(next_step_str) > 0:
        i = next_step_str.find(pattern)
        if i < 0:
            return indexes

        indexes.append(i)
        next_step_str = next_step_str[indexes[-1] + len(pattern):]

    return indexes


def parse_line(line):
    first_index = len(line)
    first_word = ''

    last_index = 0
    last_word = ''

    for word, digit in numbers.items():

        # forward
        index = line.find(word)
        if index >= 0 and index < first_index:
            first_index = index
            first_word = word

        reverse_word = word[::-1]
        reverse_line = line[::-1]

        # backward
        reverse_index = reverse_line.find(reverse_word)
        if reverse_index >= 0:
            real_index = len(line) - reverse_index - len(word)
            if real_index > last_index:
                last_word = word
                last_index = real_index

    if len(first_word) > 1:
        l1 = line.replace(first_word, numbers[first_word], 1)
    else:
        l1 = line

    if len(last_word) > 1:
        l1_reverse = l1[::-1]
        last_word_reverse = last_word[::-1]
        _replaced = l1_reverse.replace(last_word_reverse, numbers[last_word], 1)

        # l2 = l1.replace(last_word, numbers[last_word])
        l2 = _replaced[::-1]
    else:
        l2 = l1

    only_numbers = [x for x in l2 if x.isnumeric()]
    int_repr = int(''.join([only_numbers[0], only_numbers[-1]]))

    print(line, only_numbers, int_repr)

    return int_repr


def parse_line2(line):
    first_index = len(line)
    first_word = ''

    last_index = 0
    last_word = ''

    for word, digit in numbers.items():

        # forward
        index = line.find(word)
        if index >= 0 and index < first_index:
            first_index = index
            first_word = word

        reverse_word = word[::-1]
        reverse_line = line[::-1]

        # backward
        reverse_index = reverse_line.find(reverse_word)
        if reverse_index >= 0:
            real_index = len(line) - reverse_index - len(word)
            if real_index > last_index:
                last_word = word
                last_index = real_index

    if len(first_word) > 0:
        l1 = line.replace(first_word, numbers[first_word])
    else:
        l1 = line

    n1 = None
    for x in l1:
        if x.isnumeric():
            n1 = x
            break

    if len(last_word) > 0:
        l2 = line[::-1].replace(last_word[::-1], numbers[last_word])
    else:
        l2 = line[::-1]

    n2 = None
    for xx in l2:
        if xx.isnumeric():
            n2 = xx
            break

    return int(f'{n1}{n2}')


if __name__ == '__main__':
    pairs = []

    # with open('test-input.txt', 'r') as fh:
    with open('input1.txt', 'r') as fh:
        for line in fh.readlines():
            pairs.append(parse_line2(line.strip()))

    print(pairs)
    print(sum(pairs))

# 54714
# 54714

# 54719
