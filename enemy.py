import common, level

class Monster:
    def __init__(self, health, y, x):
        self.y = y
        self.x = x
        self.health = health

m1 = Monster("John", 5, 5)


def spawn(type, x, y):
    if level.world[y][x] != ('X' | 'T' | 'F'):
        pass
    return

def turn():

    return
def move():
    
    return