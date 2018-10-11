from common import printDebug
from common import printErr
import level
import time
import keyboard
import enemy
import globalLogic

x, y, facing, health = 0, 0, 0, 10
hearZone = [[]]  # [distance, x, y]
dfw = {0: [x, y-1], 2: [x, y+1], 1: [x+1, y], 3: [x-1, y]}
dbw = {0: [x, y+1], 2: [x, y-1], 1: [x-1, y], 3: [x+1, y]}


def updateCoords(direction):
    global x, y
    if direction == "dfw":
        dfw[0] = [x, y-1]
        dfw[1] = [x+1, y]
        dfw[2] = [x, y+1]
        dfw[3] = [x-1, y]
    if direction == "dbw":
        dbw[0] = [x, y+1]
        dbw[1] = [x-1, y]
        dbw[2] = [x, y-1]
        dbw[3] = [x+1, y]
    return


def isPassable(coords):
    if level.world[coords[1]][coords[0]] == '#':
        return 0
    return 1


def isExit():
    global x, y
    if level.world[y][x] == 'E':
        globalLogic.stop = 2
        return 1
    return 0


def isMonster(coords):
    for monster in enemy.enemies:
        if coords[0] == monster.x and coords[1] == monster.y:
            return 1
    return 0


def isTrigger(a, b):  # unused at the moment
    if level.world[b][a] in ['T', 'X', 'F']:
        return 1
    return 0


def turn(direction):
    global facing
    if type(direction) == str:
        if direction in ['left', 'bal', 'l']:
            if facing == 0:
                facing = 3
                enemy.enemyAction()
            else:
                facing -= 1
                enemy.enemyAction()
        if direction in ['right', 'jobb', 'r']:
            if facing == 3:
                facing = 0
                enemy.enemyAction()
            else:
                facing += 1
                enemy.enemyAction()
    else:
        facing = direction
    return


def attack():
    updateCoords("dfw")
    if isMonster(dfw[facing]):
        damageMonster(dfw[facing])
    return


def damageMonster(coords):
    enemy.enemyAction()
    for monster in enemy.enemies:
        if coords[0] == monster.x and coords[1] == monster.y:
            monster.health -= 1
            if monster.health == 0:
                print('Monster defeated!')
                enemy.enemies.remove(monster)
            else:
                print(f'Enemy\'s health: {monster.health}')
            break
    return


def move(direction):  # enemies take action if you actually move
    global x, y
    if direction == "forward":
        updateCoords("dfw")
        if not isMonster(dfw[facing]):
            if isPassable(dfw[facing]):
                if facing == 0:
                    y -= 1
                if facing == 2:
                    y += 1
                if facing == 1:
                    x += 1
                if facing == 3:
                    x -= 1
                enemy.enemyAction()
        else:
            printErr('Something went wrong')
    if direction == "backward":
        updateCoords("dbw")
        if not isMonster(dbw[facing]):
            if isPassable(dbw[facing]):
                if facing == 0:
                    y += 1
                if facing == 2:
                    y -= 1
                if facing == 1:
                    x -= 1
                if facing == 3:
                    x += 1
                enemy.enemyAction()
        else:
            printErr('Something went wrong')
    return
