from common import printDebug
from common import printErr
import level
import time
import keyboard
import enemy
import globalLogic
import echo

players = []


class Player:
    def __init__(self, x, y, facing, health):
        self.x = x
        self.y = y
        self.facing = facing
        self.health = health
        self.hearZone = {(x, y): 0}
        self.dfw = {0: [x, y-1], 2: [x, y+1], 1: [x+1, y], 3: [x-1, y]}
        self.dbw = {0: [x, y+1], 2: [x, y-1], 1: [x-1, y], 3: [x+1, y]}

    def updateCoords(self, direction):
        if direction == "dfw":
            self.dfw[0] = [self.x, self.y-1]
            self.dfw[1] = [self.x+1, self.y]
            self.dfw[2] = [self.x, self.y+1]
            self.dfw[3] = [self.x-1, self.y]
        if direction == "dbw":
            self.dbw[0] = [self.x, self.y+1]
            self.dbw[1] = [self.x-1, self.y]
            self.dbw[2] = [self.x, self.y-1]
            self.dbw[3] = [self.x+1, self.y]
        return

    def isPassable(self, coords):
        if level.world[coords[1]][coords[0]] == '#':
            return 0
        return 1

    def isExit(self):
        if level.world[self.y][self.x] == 'E':
            globalLogic.stop = 2
            return 1
        return 0

    def isMonster(self, coords):
        for monster in enemy.enemies:
            if coords[0] == monster.x and coords[1] == monster.y:
                return 1
        return 0

    def isTrigger(self, a, b):  # unused at the moment
        if level.world[b][a] in ['T', 'X', 'F']:
            return 1
        return 0

    def turn(self, direction):
        enemyAct = 0
        if type(direction) == str:
            if direction in ['left', 'bal', 'l']:
                if self.facing == 0:
                    self.facing = 3
                    enemyAct = 1
                    globalLogic.activeActor += 1
                else:
                    self.facing -= 1
                    enemyAct = 1
                    globalLogic.activeActor += 1
            if direction in ['right', 'jobb', 'r']:
                if self.facing == 3:
                    self.facing = 0
                    enemyAct = 1
                    globalLogic.activeActor += 1
                else:
                    self.facing += 1
                    enemyAct = 1
                    globalLogic.activeActor += 1
        else:
            self.facing = direction
        return enemyAct

    def attack(self):
        self.updateCoords("dfw")
        if self.isMonster(self.dfw[self.facing]):
            message = self.damageMonster(self.dfw[self.facing])
        return message

    def updateHearZone(self):
        self.hearZone = echo.read_zone([self.x, self.y], 8)
        return

    def damageMonster(self, coords):
        for monster in enemy.enemies:
            if coords[0] == monster.x and coords[1] == monster.y:
                monster.health -= 1
                if monster.health == 0:
                    message = 'Monster defeated!'
                    enemy.enemies.remove(monster)
                else:
                    message = (f'Monster\'s health: {monster.health}')
                globalLogic.activeActor += 1
                break
        return message

    def move(self, direction):  # enemies take action if you actually move
        enemyAct = 0
        if direction == "forward":
            self.updateCoords("dfw")
            if not self.isMonster(self.dfw[self.facing]):
                if self.isPassable(self.dfw[self.facing]):
                    self.directionMove('fw')
                    self.isExit()
                    if globalLogic.stop > 0:
                        return
                    self.updateHearZone()
                    enemyAct = 1
                    globalLogic.activeActor += 1
        elif direction == "backward":
            self.updateCoords("dbw")
            if not self.isMonster(self.dbw[self.facing]):
                if self.isPassable(self.dbw[self.facing]):
                    self.directionMove('bw')
                    self.isExit()
                    if globalLogic.stop > 0:
                        return
                    self.updateHearZone()
                    enemyAct = 1
                    globalLogic.activeActor += 1
        else:
            printErr('Something went wrong')
        return enemyAct

    def directionMove(self, direction):
        if direction == 'fw':
            if self.facing == 0:
                self.y -= 1
            if self.facing == 2:
                self.y += 1
            if self.facing == 1:
                self.x += 1
            if self.facing == 3:
                self.x -= 1
        elif direction == 'bw':
            if self.facing == 0:
                self.y += 1
            if self.facing == 2:
                self.y -= 1
            if self.facing == 1:
                self.x -= 1
            if self.facing == 3:
                self.x += 1
        return


def spawn(x, y, facing, health):
    player_id = Player(x, y, facing, health)
    player_id.updateHearZone()
    players.append(player_id)
    return
