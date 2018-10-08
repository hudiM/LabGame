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

    def isMonster(self, newX, newY):
        for enemyEntity in enemies:
            if newX == enemyEntity.x and newY == enemyEntity.y:
                return 1
        return 0

    def isPassable(self, a, b):
        if level.world[b][a] in ['#', 'E']:
            return 0
        return 1

    def move(self):
        randomMove = random.randrange(0, 6)
        if randomMove < 5:
            if self.facing == 2:
                if self.isPassable(self.x, self.y+1):
                    if self.isMonster(self.x, self.y+1) == 0:
                        self.y += 1
                    else:
                        self.facing -= 1
                else:
                    self.facing -= 1
            elif self.facing == 0:
                if self.isPassable(self.x, self.y-1):
                    if self.isMonster(self.x, self.y-1) == 0:
                        self.y -= 1
                    else:
                        self.facing -= 1
                else:
                    self.facing -= 1
            elif self.facing == 1:
                if self.isPassable(self.x+1, self.y):
                    if self.isMonster(self.x+1, self.y) == 0:
                        self.x += 1
                    else:
                        self.facing -= 1
                else:
                    self.facing -= 1
            elif self.facing == 3:
                if self.isPassable(self.x-1, self.y):
                    if self.isMonster(self.x-1, self.y) == 0:
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
