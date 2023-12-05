def main(input):
    # 0 - winners
    # 1 - my numbers
    all_cards = []

    for line in input:
        cards = line.split(':')[-1].strip()
        winners_str = cards.split('|')[0].strip()
        my_numbers_str = cards.split('|')[1].strip()

        winners_numbers = []
        for wns in winners_str.split(' '):
            if len(wns.strip()) > 0:
                winners_numbers.append(int(wns.strip()))

        my_numbers = []
        for mns in my_numbers_str.split(' '):
            if len(mns.strip()) > 0:
                my_numbers.append(int(mns.strip()))

        all_cards.append([winners_numbers, my_numbers])

    cards_sums = []

    for winners, my_numbers in all_cards:
        card_sum = 0
        for my_number in my_numbers:
            if my_number in winners:
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum *= 2
        cards_sums.append(card_sum)

    for n, i in enumerate(cards_sums):
        print(n + 1, i)

    print(sum(cards_sums))


if __name__ == '__main__':
    input = []
    # with open('input-test.txt', 'r') as fh:
    with open('input.txt', 'r') as fh:
        for line in fh.readlines():
            input.append(line.strip())
    main(input)
