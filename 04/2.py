all_cards_matches = []

def find_all_cards_for(card_number):
    # print(f'-- {card_number}')
    number_of_matches_for_card = all_cards_matches[card_number]
    copies_for_current_card = list(range(len(all_cards_matches)))[
                              card_number + 1:card_number + 1 + number_of_matches_for_card]

    return copies_for_current_card


def expand_range(input_list):
    expanded = False

    ret = []
    for x in input_list:
        matches = find_all_cards_for(x)
        if len(matches) == 0:
            ret.append(x)
        else:
            expanded = True
            ret.extend(matches)

    return ret, expanded


class Card:
    def __init__(self, card_number, parent=None):
        self.count = 1
        self.parent = parent

        self.card_number = card_number
        self.wins = all_cards_matches[card_number]
        self.copies = [Card(x, parent=self) for x in find_all_cards_for(card_number)]


        if self.parent:
            self.parent.bump()

    def bump(self):
        if self.parent:
            self.parent.bump()
        else:
            self.count += 1

    def __str__(self):
        return f'''[{self.card_number+1}|{self.count}]'''# w{self.wins} c{self.copies}'''

    def __repr__(self):
        return self.__str__()


def main(input):
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

        card_matches = []
        for my_num in my_numbers:
            if my_num in winners_numbers:
                card_matches.append(my_num)

        all_cards_matches.append(len(card_matches))

    total = 0

    for x in range(len(all_cards_matches)):
        c = Card(x)
        print(c)
        total += c.count

    print(total)

if __name__ == '__main__':
    input = []
    # with open('input-test.txt', 'r') as fh:
    with open('input.txt', 'r') as fh:
        for line in fh.readlines():
            input.append(line.strip())
    main(input)
