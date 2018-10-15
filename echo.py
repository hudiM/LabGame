import level


def read_zone(source, hearDistance):
    world = level.world
    hearing_zone = {(source[0], source[1]): 0}
    hearing_directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    for step in range(1, hearDistance+1):
        temp_hearing_zone = {}
        for element in hearing_zone:
            if hearing_zone[element] == step - 1:
                for facing in range(0, 4):
                    x = element[0] + hearing_directions[facing][0]
                    y = element[1] + hearing_directions[facing][1]
                    if world[y][x] not in ["#", "E"] and (x, y) not in hearing_zone:
                        temp_hearing_zone[(x, y)] = step
        hearing_zone = {**hearing_zone, **temp_hearing_zone}
    return hearing_zone
