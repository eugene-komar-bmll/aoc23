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
    # print(subgames)
    return subgames


def fewest(game):  # list of maps
    res = {}
    for subgame in game:
        for color, n in subgame.items():
            if color in res.keys():
                if res[color] < n:
                    res[color] = n
            else:
                res[color] = n

    return res


if __name__ == '__main__':
    # with open('input-test.txt', 'r') as fh:
    with open('input.txt', 'r') as fh:
        lines = fh.readlines()

        games_powers = []

        r = []
        for line in lines:
            _i = parse_line(line.strip())
            print(_i)
            r.append(_i)
            print(fewest(_i))
            game_power_list = fewest(_i).values()
            print(game_power_list)

            gpp = 1

            for gp in game_power_list:
                gpp = gpp * gp

            print(gpp)
            games_powers.append(gpp)

        print(games_powers)
        print(sum(games_powers))
