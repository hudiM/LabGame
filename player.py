import common, level, time, keyboard, enemy

x, y, facing, health = 0, 0, 0, 10
hearZone = [[]]#[distance, x, y]

def isPassable(a, b):
    if level.world[b][a] == '#':
        return 0
    return 1

def isMonster(newX, newY):
    for monster in enemy.enemies:
        if newX == monster.x and newY == monster.y:
            return 1
    return 0

def isTrigger(a, b):
    if level.world[b][a] == ('T' or 'X' or 'F'):
        return 1
    return 0

def turn(direction):
    global facing
    if type(direction) == str:
        if direction in ['left', 'bal', 'l']:
            if facing == 0:
                facing = 3
            else:
                facing -= 1
        if direction in ['right', 'jobb', 'r']:
            if facing == 3:
                facing = 0
            else:
                facing += 1
    else:
        facing = direction
    return

def attack():
    pass

def move(direction):
    global x,y
    if direction == "forward":
        if facing == 0:
            if not isMonster(x, y-1):
                if isPassable(x, y-1):
                    y-=1
        elif facing == 1:
            if not isMonster(x+1, y):
                if isPassable(x+1, y):
                    x+=1
        elif facing == 2:
            if not isMonster(x, y+1):
                if isPassable(x, y+1):
                    y+=1
        elif facing == 3:
            if not isMonster(x-1, y):
                if isPassable(x-1, y):
                    x-=1
        else:
            common.printErr('Wrong facing')
    return