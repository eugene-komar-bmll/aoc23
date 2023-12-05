from collections import defaultdict


def main(input_lines):
    width = len(input_lines[0])
    hight = len(input_lines)
    print(f'{width}x{hight}')

    buffs = []

    for y, line in enumerate(input_lines):
        buff = [(), [], []]  # [(x, y), ['1','2','3'], [()...]]
        for x, cell in enumerate(line):
            # print(cell, x, y)
            if cell.isnumeric():
                # last digit or eol
                if width == x + 1 or not line[x + 1].isnumeric():
                    # print(y)
                    buff[1].append(cell)

                    # ok, number formed. checking area for symbols

                    # attempt to generalise start_x and end_x
                    start_x = x - len(buff[1])
                    if start_x - 1 < 0:
                        start_x = 0
                    end_x = x + 1
                    if end_x >= width:
                        end_x = width - 1

                    # check current line
                    if line[start_x] == '*':
                        buff[2].append((start_x, y))

                    if line[end_x] == '*':
                        buff[2].append((end_x, y))

                    # check on previous line
                    if y > 0:
                        lookup_range = input_lines[y - 1][start_x:end_x + 1]
                        for symbol_x, symbol in enumerate(lookup_range):
                            if symbol == '*':
                                buff[2].append((start_x + symbol_x, y - 1))

                    # check next line
                    if y < hight - 1:
                        lookup_range = input_lines[y + 1][start_x:end_x + 1]
                        for symbol_x, symbol in enumerate(lookup_range):
                            if symbol == '*':
                                buff[2].append((start_x + symbol_x, y + 1))

                    buffs.append(buff)
                    buff = [(), [], []]

                # N-th digit of number
                elif x > 0 and line[x - 1].isnumeric():
                    buff[1].append(cell)

                # first digit
                elif line[x + 1].isnumeric():
                    buff[0] = (x, y)
                    buff[1].append(cell)

    asterics_coord_to_numbers = defaultdict(list)

    for num_correds, num_str_list, asterics_coords_list in buffs:
        if len(asterics_coords_list) > 0:
            for ac in asterics_coords_list:
                asterics_coord_to_numbers[ac].append(int(''.join(num_str_list)))

    sum = 0
    for v in asterics_coord_to_numbers.values():
        if len(v) == 2:
            tmp = v[0] * v[1]
            sum += tmp

    print(sum)


if __name__ == '__main__':
    input_lines = []

    # with open('input-test.txt', 'r') as fh:
    with open('input1.txt', 'r') as fh:
        for line in fh.readlines():
            input_lines.append(line.strip())

    main(input_lines)
