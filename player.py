import common, level

x = 0
y = 0
facing = 0

def spawn(locX, locY):
    level.world[locY][locX] = 'P'
    return world

def isPassable(a, b):
    print(str(a)+'-'+str(b))
    if level.world[b][a] == '#':
        return 0
    return 1

def isTrigger(a, b):
    if level.world[b][a] == ('T' or 'X' or 'F'):
        return 1
    return 0

def turn(direction):
    if type(direction) == str:
        if direction in ['left', 'bal', 'l']:
            facing -= 1
        elif direction == ['right', 'jobb', 'r']:
            facing += 1
        else:
            return
    else:
        facing += direction
    facing %= 4
    return #debug text for test

def delPlayer():
    level.world[y][x] = ' '
    return

def move(direction):
    if direction == "forward":
        if facing == 0:
            if isPassable(x, y-1):
                delPlayer()
                level.world[y-1][x] = 'P'
        if facing == 1:
            if isPassable(x+1, y):
                level.world[y][x] = ' '
    return

# def move(direction, world): # change to x,y is global
#     if direction == 'up':
#         for y in range(len(world)):
#             for p in world[y]:
#                 if p == 'P':
#                     x = world[y].index('P')
#                     if isPassable(world, x, y-1) == 1:
#                         world[y][x] = ' '
#                         world[y-1][x] = 'P'
#                     return world
#         return world
#     if direction == 'down':
#         for y in range(len(world)):
#             for p in world[y]:
#                 if p == 'P':
#                     x = world[y].index('P')
#                     if isPassable(world, x, y+1) == 1:
#                         world[y][x] = ' '
#                         world[y+1][x] = 'P'
#                     return world
#         return world
#     if direction == 'left':
#         for y in range(len(world)):
#             for p in world[y]:
#                 if p == 'P':
#                     x = world[y].index('P')
#                     if isPassable(world, x-1, y) == 1:
#                         world[y][x] = ' '
#                         world[y][x-1] = 'P'
#                     return world
#         return world
#     if direction == 'right':
#         for y in range(len(world)):
#             for p in world[y]:
#                 if p == 'P':
#                     x = world[y].index('P')
#                     if isPassable(world, x+1, y) == 1:
#                         world[y][x] = ' '
#                         world[y][x+1] = 'P'
#                     return world
#         return world
#     common.printErr('Unknown movement error')
#     return world