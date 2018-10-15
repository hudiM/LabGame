from common import printErr
from common import printDebug
from common import printWarning
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

    def isPlayerInHearingDistance(self):  # it works but why?!
        # https://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
        # https://python-textbok.readthedocs.io/en/1.0/Loop_Control_Statements.html#comprehensions
        # if (self.y, self.x) in [sublist for sublist in player.players[0]:
        # if (self.x, self.y) in player.players[0].hearZone:
        #     printDebug('Yes')
        #     return 1
        return 0

    def isPlayerAround(self):
        self.isPlayerInHearingDistance()
        if player.players[0].x == self.x and player.players[0].y == self.y-1:
            return 0
        elif player.players[0].x == self.x and player.players[0].y == self.y+1:
            return 2
        elif player.players[0].x == self.x+1 and player.players[0].y == self.y:
            return 1
        elif player.players[0].x == self.x-1 and player.players[0].y == self.y:
            return 3
        else:
            return -1

    def attackPlayer(self):
        player.players[0].health -= 1
        if player.players[0].health <= 0:
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

    def autoFacing(self):
        if self.isPassable(self.d[(self.facing-1) % 4]):
            self.facing -= 1
        else:
            if self.isPassable(self.d[(self.facing+1) % 4]):
                self.facing += 1
            else:
                self.facing += 2
        return

    def move(self):
        randomMove = random.randrange(0, 5)
        if randomMove < 4:
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
                    self.autoFacing()
            else:
                self.autoFacing()
        elif randomMove == 4:
            self.autoFacing()
        elif randomMove == 5:
            pass
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
        pass


def spawn(x, y, facing, health):
    monster_id = Monster(x, y, facing, health)
    enemies.append(monster_id)
    return
