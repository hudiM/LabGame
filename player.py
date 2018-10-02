import common, level

x = 0
y = 0
facing = 0

def spawn(locX, locY):
    level.world[locY][locX] = 'P'
    return world

def isPassable(a, b):
    if level.world[b][a] == '#':
        return 0
    return 1

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
            print('DEBUG: right')
            if facing == 3:
                facing = 0
            else:
                facing += 1
    else:
        facing = direction
    return

def delPlayer():
    level.world[y][x] = ' '
    return

def move(direction):
    global x
    global y
    if direction == "forward":
        if facing == 0:
            if isPassable(x, y-1):
                delPlayer()
                level.world[y-1][x] = 'P'
                y-=1
        elif facing == 1:
            if isPassable(x+1, y):
                delPlayer()
                level.world[y][x+1] = 'P'
                x+=1
        elif facing == 2:
            if isPassable(x, y+1):
                delPlayer()
                level.world[y+1][x] = 'P'
                y+=1
        elif facing == 3:
            if isPassable(x-1, y):
                delPlayer()
                level.world[y][x-1] = 'P'
                x-=1
        else:
            common.printErr('Wrong facing')
    return