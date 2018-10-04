import common, level, time, keyboard, enemy, globalLogic
x, y, facing, health = 0, 0, 0, 10
hearZone = [[]]#[distance, x, y]

def isPassable(a, b):
    if level.world[b][a] == '#':
        return 0
    return 1

def isExit():
    global x,y
    if level.world[y][x] == 'E':
        globalLogic.stop = 2
        return 1
    return 0

def isMonster(newX, newY):
    for monster in enemy.enemies:
        if newX == monster.x and newY == monster.y:
            return 1
    return 0

def isTrigger(a, b):
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
    if facing == 0:
        if isMonster(x, y-1):
            damageMonster(x,y-1)
    elif facing == 1:
        if isMonster(x+1, y):
            damageMonster(x+1,y)
    elif facing == 2:
        if isMonster(x, y+1):
            damageMonster(x,y+1)
    elif facing == 3:
        if isMonster(x-1, y):
            damageMonster(x-1,y)

def damageMonster(newX, newY):
    enemy.enemyAction()
    for monster in enemy.enemies:
        if newX == monster.x and newY == monster.y:
            monster.health -= 1
            if monster.health == 0:
                print('Monster defeated!')
                enemy.enemies.remove(monster)
            else:
                print(f'Enemy\'s health: {monster.health}')
            break
    return

def move(direction): # enemies take action if you actually move ( no action input is unhandled )
    global x,y
    if direction == "forward":
        if facing == 0:
            if not isMonster(x, y-1):
                if isPassable(x, y-1):
                    y-=1
                    enemy.enemyAction()
        elif facing == 1:
            if not isMonster(x+1, y):
                if isPassable(x+1, y):
                    x+=1
                    enemy.enemyAction()
        elif facing == 2:
            if not isMonster(x, y+1):
                if isPassable(x, y+1):
                    y+=1
                    enemy.enemyAction()
        elif facing == 3:
            if not isMonster(x-1, y):
                if isPassable(x-1, y):
                    x-=1
                    enemy.enemyAction()
        else:
            common.printErr('Wrong facing')
    if direction == "backward":
        if facing == 0:
            if not isMonster(x, y+1):
                if isPassable(x, y+1):
                    y+=1
                    enemy.enemyAction()
        elif facing == 1:
            if not isMonster(x-1, y):
                if isPassable(x-1, y):
                    x-=1
                    enemy.enemyAction()
        elif facing == 2:
            if not isMonster(x, y-1):
                if isPassable(x, y-1):
                    y-=1
                    enemy.enemyAction()
        elif facing == 3:
            if not isMonster(x+1, y):
                if isPassable(x+1, y):
                    x+=1
                    enemy.enemyAction()
        else:
            common.printErr('Wrong facing')
    return