import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import islice
from pprint import pprint
import time


def batched(iterable, n):
   it = iter(iterable)
   while (batch := list(islice(it, n))):
       yield batch

class Seed:
    def __init__(self):
        pass


class ConversionMapItem:

    @classmethod
    def from_lines(cls, source, target, lines):
        map_entries = []

        name = f'{source}-to-{target}'

        recording = False
        for line in lines:
            if name in line:
                recording = True
                continue

            if recording and len(line) != 0:
                raw_splits = line.split(' ')
                tmp_map = []
                for rs in raw_splits:
                    tmp_map.append(int(rs.strip()))
                map_entries.append(tmp_map)

            if recording and len(line) == 0:
                break

        return ConversionMapItem(source, target, map_entries)

    def __init__(self, source, target, table):
        # print(f'making {source} -> {target}')
        self.source = source
        self.target = target
        self.table = table

        self.cache = []

    def lookup(self, number):
        ret = number

        if number in self.cache:
            print('I REMEMBER YOU !!!', number)
        else:
            self.cache.append(number)

        for dest, src, l in self.table:

            if number >= src and number <= src + l:
                idx = number - src

                src_e = src + idx
                dest_e = dest + idx

                ret = dest_e

                return ret

        return ret


    def __str__(self):
        return f'{self.source} -> {self.target} | {self.table}'

    def __repr__(self):
        return self.__str__()


class ConversionMap:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def __str__(self):
        return '\n'.join([str(x) for x in self.items])

    def __repr__(self):
        return self.__str__()

    def get_map_for(self, dest):
        for m in self.items:
            if m.target == dest:
                return m

        return None

    def soil(self, seed):
        # print('seed', seed)
        return self.get_map_for('soil').lookup(seed)

    def fertilizer(self, seed):
        soil = self.soil(seed)
        # print('soil', soil)
        return self.get_map_for('fertilizer').lookup(soil)

    def water(self, seed):
        fertilizer = self.fertilizer(seed)
        # print('fertilizer', fertilizer)
        return self.get_map_for('water').lookup(fertilizer)

    def light(self, seed):
        water = self.water(seed)
        # print('water', water)
        return self.get_map_for('light').lookup(water)

    def temperature(self, seed):
        return self.get_map_for('temperature').lookup(self.light(seed))

    def humidity(self, seed):
        return self.get_map_for('humidity').lookup(self.temperature(seed))

    def location(self, seed):
        return self.get_map_for('location').lookup(self.humidity(seed))


def extract_map(src_name, target_name, lines):
    map_entries = []

    name = f'{src_name}-to-{target_name}'

    recording = False
    for line in lines:
        if name in line:
            recording = True
            continue

        if recording and len(line) != 0:
            raw_splits = line.split(' ')
            tmp_map = []
            for rs in raw_splits:
                tmp_map.append(int(rs.strip()))
            # map_lines.append(line)
            map_entries.append(tmp_map)

        if recording and len(line) == 0:
            break

    return src_name, target_name, map_entries


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'start: {self.start:_}  end: {self.end:_} [{self.end - self.start:_}]'

    def __repr__(self):
        return self.__str__()

    def merge(self, another_range):
        if another_range.start > self.end or another_range.end < self.start:
            return False

        return True




if __name__ == '__main__':
    file_lines = []

    with open('input.txt', 'r') as fh:
    # with open('input-test.txt', 'r') as fh:
        for line in fh.readlines():
            file_lines.append(line.strip())

    seeds = []
    for line in file_lines:
        if 'seeds' in line:
            seeds_str = line.split(':')[-1].strip()
            for seed_n_str in seeds_str.split(' '):
                seeds.append(int(seed_n_str.strip()))

    print('seeds', seeds)

    almanac = ConversionMap()
    almanac.append(ConversionMapItem.from_lines('seed', 'soil', file_lines))
    almanac.append(ConversionMapItem.from_lines('soil', 'fertilizer', file_lines))
    almanac.append(ConversionMapItem.from_lines('fertilizer', 'water', file_lines))
    almanac.append(ConversionMapItem.from_lines('water', 'light', file_lines))
    almanac.append(ConversionMapItem.from_lines('light', 'temperature', file_lines))
    almanac.append(ConversionMapItem.from_lines('temperature', 'humidity', file_lines))
    almanac.append(ConversionMapItem.from_lines('humidity', 'location', file_lines))
    print(almanac)
    print('-----')

    total_mins = []

    ranges = [Range(start=x[0], end=x[0]+x[1]) for x in batched(seeds, 2)]


    def min_in_range(_range):
        print(_range)
        min_loc = None

        for s in range(_range.start, _range.end):

            loc = almanac.location(s)

            if min_loc is None:
                min_loc = loc

            if loc < min_loc:
                min_loc = loc

        return min_loc

    __start = time.time()
    min_in_range(ranges[0])
    __end = time.time()
    print('duration: ', __end - __start)

    # with ThreadPoolExecutor(max_workers=1) as executor:
    #     features = [executor.submit(min_in_range, x) for x in ranges]
    #
    #     for feature in as_completed(features):
    #         total_mins.append(feature.result())



    print('--')
    print(total_mins)
    print(min(total_mins))

    # print(almanac.location(70))
