import common
import level
import random
import player
import globalLogic

enemies = []


class Monster:
    import player

    def __init__(self, x, y, facing, health):
        self.y = y
        self.x = x
        self.health = health
        self.facing = facing
        self.d = {0: [x, y-1], 2: [x, y+1], 1: [x+1, y], 3: [x-1, y]}

    def updateCoords(self):
        self.d[0] = [self.x, self.y-1]
        self.d[1] = [self.x+1, self.y]
        self.d[2] = [self.x, self.y+1]
        self.d[3] = [self.x-1, self.y]
        return

    def isPlayer(self):
        if self.facing == 0:
            if player.x == self.x and player.y == self.y+1:
                return 1
        return 0

    def isPlayerAround(self):
        if player.x == self.x and player.y == self.y-1:
            return 0
        elif player.x == self.x and player.y == self.y+1:
            return 2
        elif player.x == self.x+1 and player.y == self.y:
            return 1
        elif player.x == self.x-1 and player.y == self.y:
            return 3
        else:
            return -1

    def attackPlayer(self):
        player.health -= 1
        if player.health <= 0:
            globalLogic.stop = 1

    def isMonster(self, coords):
        for enemyEntity in enemies:
            if coords[1] == enemyEntity.x and coords[0] == enemyEntity.y:
                return 1
        return 0

    def isPassable(self, coords):
        if level.world[coords[1]][coords[0]] in ['#', 'E']:
            return 0
        return 1

    def move(self):
        randomMove = random.randrange(0, 6)
        if randomMove < 5:
            self.updateCoords()
            if self.isPassable(self.d[self.facing]):
                if self.isMonster(self.d[self.facing]) == 0:
                    if self.facing == 0:
                        self.y -= 1
                    elif self.facing == 1:
                        self.x += 1
                    elif self.facing == 2:
                        self.y += 1
                    elif self.facing == 3:
                        self.x -= 1
                else:
                    self.facing -= 1
            else:
                self.facing -= 1
        elif randomMove == 6:
            self.facing += 1
        elif randomMove == 5:
            self.facing -= 1
        else:
            common.printErr(f'monster movement error {randomMove} is out of range (0-6)')
        self.facing %= 4

    def lookForPlayer(self):
        if self.isPlayerAround() == -1:
            self.move()
        elif self.isPlayerAround() == 0:
            if self.facing == 0:
                self.attackPlayer()
            else:
                self.facing = 0
        elif self.isPlayerAround() == 1:
            if self.facing == 1:
                self.attackPlayer()
            else:
                self.facing = 1
        elif self.isPlayerAround() == 2:
            if self.facing == 2:
                self.attackPlayer()
            else:
                self.facing = 2
        elif self.isPlayerAround() == 3:
            if self.facing == 3:
                self.attackPlayer()
            else:
                self.facing = 3


def enemyAction():
    for monster in enemies:
        monster.lookForPlayer()


def spawn(x, y, facing, health):
    monster_id = Monster(x, y, facing, health)
    enemies.append(monster_id)
    return
