def main(input_lines):
    width = len(input_lines[0])
    hight = len(input_lines)
    print(f'{width}x{hight}')

    symbols = []
    for line in input_lines:
        for cell in line:
            if not cell.isnumeric() and cell != '.' and cell not in symbols:
                symbols.append(cell)
    print(f'symbols: {symbols}')

    buffs = []

    for y, line in enumerate(input_lines):
        buff = [(),[],False]  # [(x, y), ['1','2','3'], True|False]
        for x, cell in enumerate(line):
            # print(cell, x, y)
            if cell.isnumeric():
                # last digit or eol
                if width == x + 1 or not line[x + 1].isnumeric():
                    # print(y)
                    buff[1].append(cell)
                    buff[2] = False

                    # ok, number formed. checking area for symbols

                    # attempt to generalise start_x and end_x
                    start_x = x - len(buff[1])
                    if start_x - 1 < 0:
                        start_x = 0
                    end_x = x + 1
                    if end_x >= width:
                        end_x = width-1

                    # check current line. actually just start_x and end_x
                    # print(buff)
                    # print(start_x, end_x)
                    # print(x)
                    if line[start_x] in symbols or line[end_x] in symbols:
                        buff[2] = True

                    # check on previous line
                    if y > 0:
                        lookup_range = input_lines[y - 1][start_x:end_x+1]
                        for symbol in symbols:
                            if symbol in lookup_range:
                                buff[2] = True

                    # check next line
                    if y < hight - 1:
                        lookup_range = input_lines[y + 1][start_x:end_x + 1]
                        for symbol in symbols:
                            if symbol in lookup_range:
                                buff[2] = True

                    buffs.append(buff)
                    buff = [(),[],False]

                # N-th digit of number
                elif x > 0 and line[x - 1].isnumeric():
                    buff[1].append(cell)

                # first digit
                elif line[x + 1].isnumeric():
                    buff[0] = (x, y)
                    buff[1].append(cell)

    # sum of all True buffer
    sum = 0
    for b in buffs:
        if b[2] == True:
            int_num = int(''.join(b[1]))
            sum += int_num

    print(sum)


if __name__ == '__main__':
    input_lines = []

    # with open('input-test.txt', 'r') as fh:
    with open('input1.txt', 'r') as fh:
        for line in fh.readlines():
            input_lines.append(line.strip())

    main(input_lines)
