import common, level

x, y, health = 0, 0, 0

def spawn(type, x, y):
    if level.world[y][x] != ('X' | 'T' | 'F'):
        pass
    return