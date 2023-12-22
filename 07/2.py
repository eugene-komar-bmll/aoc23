class Hand:
    def __init__(self, input, bid):
        self.input = input
        self.bid = bid

        if len(input) != 5:
            raise Exception('Wrong input')

        self.values = []
        for char in input:
            try:
                self.values.append(int(char))
            except:
                if char == 'T':
                    self.values.append(10)
                elif char == 'J':
                    self.values.append(1)
                elif char == 'Q':
                    self.values.append(12)
                elif char == 'K':
                    self.values.append(13)
                elif char == 'A':
                    self.values.append(14)

        self.values_original = self.values.copy()

        self.type_kind = None
        self.type_name = None
        self.set_type()

        # J count
        self.j_count = self.values_original.count(1)
        if self.j_count > 0:
            if self.j_count == 5:  # J -> A
                self.values = [14 for x in self.values]

            if self.j_count in [4, 3]:  # make five/four of a kind
                self.values = []
                for x in self.values_original:
                    if x == 1:
                        self.values.append(max(self.values_original))
                    else:
                        self.values.append(x)

    def __str__(self):
        return f'''<{str(self.values)} {self.type_name} ({self.type_kind})>'''

    def __repr__(self):
        return self.__str__()

    def set_type(self):
        _s = set(self.values)
        _sl = list(_s)

        if len(_sl) == 1:
            self.type_name = 'Five of a kind'
            self.type_kind = 7  # five of a kind

        elif len(_sl) == 2:  # four of a kind OR full house

            # four of a kind
            if self.values.count(_sl[0]) == 4 or self.values.count(_sl[1]) == 4:
                self.type_name = 'Four of a kind'
                self.type_kind = 6

            # full house
            else:
                self.type_name = 'Full house'
                self.type_kind = 5

        elif len(_sl) == 3:  # three of a kind OR two pair
            _max_count = max([self.values.count(x) for x in _sl])

            # three of a kind
            if _max_count == 3:
                self.type_name = 'Three of a kind'
                self.type_kind = 4

            # two pair
            else:
                self.type_name = 'Two pair'
                self.type_kind = 3

        elif len(_sl) == 4:  # one pair
            self.type_name = 'One pair'
            self.type_kind = 2

        else:
            self.type_name = 'High card'
            self.type_kind = 1

    def __lt__(self, other, index=0):
        if self.type_kind == other.type_kind:
            if index == len(self.values):
                return False

            if self.values_original[index] == other.values_original[index]:
                return self.__lt__(other, index=index + 1)

            else:
                return self.values_original[index] < other.values_original[index]

        else:
            return self.type_kind < other.type_kind


if __name__ == '__main__':
    h = []
    with open('test-input.txt', 'r') as fh:
        # with open('input.txt', 'r') as fh:
        for l in fh.readlines():
            l = l.strip()
            hh, bb = l.split(' ')
            h.append(Hand(hh, int(bb)))

    h.sort()

    total = 0

    for n, h_i in enumerate(h):
        rank = n + 1
        total_winnings = rank * h_i.bid
        total += total_winnings

    print(total)
