def next_row(input_row):
    res = []
    for i in range(len(input_row) - 1):
        res.append(input_row[i+1] - input_row[i])

    return res

def predict(input_list):
    rows = [input_list]

    while set(rows[-1]) != set([0]):
        rows.append(next_row(rows[-1]))

    rows.reverse()

    [print(x) for x in rows]
    #
    print('-')

    for n, row in enumerate(rows):
        if n == 0:
            row.append(0)

        else:
            row_predicted = row[-1] + rows[n-1][-1]
            row.append(row_predicted)

        # print(row)

    [print(x) for x in rows]

    return rows[-1][-1]


if __name__ == '__main__':
    # print(predict([0,3,6,9,12,15]))
    # print(predict([1,3,6,10,15,21]))

    sum = 0

    with open('input.txt', 'r') as fh:
        for line in fh.readlines():
            line = line.strip()
            tokens = line.split(' ')

            int_list = []

            for t in tokens:
                t = t.strip()
                int_list.append(int(t))

            predicted = predict(int_list)
            sum += predicted

    print(sum)