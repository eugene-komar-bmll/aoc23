if __name__ == '__main__':
    sum = 0

    with open('input1.txt', 'r') as fh:
        for line in fh.readlines():
            only_numbers = [x for x in line if x.isnumeric()]
            int_repr = int(''.join([only_numbers[0], only_numbers[-1]]))
            print(only_numbers, int_repr)
            sum += int_repr

    print(sum)
