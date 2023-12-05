limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_line(line):
    print('--')
    print(line)

    x = line.split(': ')
    game = x[0]
    rest = x[1]
    # print(game)
    # print(rest)

    game_n_s = game.split('Game ')[-1]
    game_n = int(game_n_s)
    # print(game_n)
    subgames = []

    game_sets = rest.split(';')
    for gs in game_sets:
        gs = gs.strip()
        # print(gs)

        cubes = gs.split(',')
        cubes_d = {}
        for cube in cubes:
            cube = cube.strip()
            # print(cube)
            cube_split = cube.split(' ')
            n_str = cube_split[0].strip()
            color_str = cube_split[1].strip()

            # print(f'{n_str} => {color_str}')
            cubes_d[color_str] = int(n_str)

        subgames.append(cubes_d)
    print(subgames)
    return subgames


def is_game_possible(game):
    for subgame in game:
        for color, digit in subgame.items():
            if digit > limits[color]:
                return False

    return True



if __name__ == '__main__':
    # with open('input-test.txt', 'r') as fh:
    with open('input.txt', 'r') as fh:
        lines = fh.readlines()

        possible_games = []

        r = []
        for line in lines:
            r.append(parse_line(line.strip()))

        for n, l in enumerate(r):
            print(n+1, is_game_possible(l))
            if is_game_possible(l):
                possible_games.append(n+1)

        print(possible_games)
        print(sum(possible_games))

