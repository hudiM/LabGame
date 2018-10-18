from common import printErr
from common import printDebug
from common import printDebugS
from common import printDebugE
from common import printWarning
import globalLogic
import player
import random
import level

enemies = []


class Monster:
    def __init__(self, x, y, facing, health, hearingStr, ap=0):
        self.y = y
        self.x = x
        self.health = health
        self.facing = facing
        self.hearingStr = hearingStr
        self.ap = ap
        self.ai = 0  # 0 = searching (0.5 ap) | 1 = hearing (1 ap) | 2 = seeing (2 ap)
        self.d = {0: (x, y-1), 2: (x, y+1), 1: (x+1, y), 3: (x-1, y)}

    def updateCoords(self):
        self.d[0] = (self.x, self.y-1)
        self.d[1] = (self.x+1, self.y)
        self.d[2] = (self.x, self.y+1)
        self.d[3] = (self.x-1, self.y)

    def isPlayerInHearingDistance(self):
        for pid in player.players:
            if (self.x, self.y) in pid.hearZone.keys():
                if pid.hearZone.get((self.x, self.y)) <= self.hearingStr:
                    return 1
        return 0

    def isPlayerAround(self):
        for pid in player.players:
            if pid.x == self.x and pid.y == self.y-1:
                return 0
            elif pid.x == self.x and pid.y == self.y+1:
                return 2
            elif pid.x == self.x+1 and pid.y == self.y:
                return 1
            elif pid.x == self.x-1 and pid.y == self.y:
                return 3
        return -1

    def isMonster(self, coords):
        for enemyEntity in enemies:
            if coords[0] == enemyEntity.x and coords[1] == enemyEntity.y:
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

    def lookupPlayerInHearingDistance(self):
        closestPlayer = 0
        playerDist = 99
        for pid in player.players:
            if (self.x, self.y) in pid.hearZone.keys():
                if pid.hearZone.get((self.x, self.y)) <= self.hearingStr:
                    if playerDist > pid.hearZone.get((self.x, self.y)):
                        playerDist = pid.hearZone.get((self.x, self.y))
                        closestplayer = pid
        return closestplayer

    def findClosestPlayerLocation(self):
        closestDistance = 99
        closestLoc = 0
        pid = self.lookupPlayerInHearingDistance()
        closestDistance = pid.hearZone.get((self.x, self.y))
        for i in range(4):
            if self.d[i] in pid.hearZone.keys():
                if closestDistance > pid.hearZone.get(self.d[i]):
                    closestLoc = self.d[i]
        return closestLoc

    def isPlayer(self, loc):
        for pid in player.players:
            if pid.x == loc[0] and pid.y == loc[1]:
                return 1
        return 0

    def attackPlayer(self, loc):
        for pid in player.players:
            if pid.x == loc[0] and pid.y == loc[1]:
                pid.health -= 1
                if pid.health <= 0 and len(player.players) == 1:
                    globalLogic.stop = 1
                elif pid.health <= 0 and len(player.players) > 1:
                    player.players.remove(pid)
                    try:
                        if pid == player.players[0]:
                            globalLogic.keys.pop('w')
                            globalLogic.keys.pop('a')
                            globalLogic.keys.pop('s')
                            globalLogic.keys.pop('d')
                            globalLogic.keys.pop('f')
                        if pid == player.players[1]:
                            globalLogic.keys.pop('A')
                            globalLogic.keys.pop('B')
                            globalLogic.keys.pop('C')
                            globalLogic.keys.pop('D')
                            globalLogic.keys.pop('í')
                    except:
                        pass
        return

    def moveTowardsPlayer(self, loc):
        if self.d[self.facing] == loc:
            if not self.isMonster(loc):
                if self.isPlayer(loc):
                    self.attackPlayer(loc)
                else:
                    self.x = self.d[self.facing][0]
                    self.y = self.d[self.facing][1]
        else:
            for i in range(4):
                if self.d[i] == loc:
                    self.facing = i
        return

    def chasePlayer(self):
        nextLoc = self.findClosestPlayerLocation()
        self.moveTowardsPlayer(nextLoc)
        return

    def setStates(self):
        if False:
            self.ap += 2
            self.ai = 2
        elif self.isPlayerInHearingDistance():
            self.ap += 1
            self.ai = 1
        else:
            self.ap += 0.5
            self.ai = 0
        return

    def action(self):
        self.setStates()
        self.updateCoords()
        while(self.ap >= 1):
            if self.ai <= 0:
                self.move()
            elif self.ai > 0:
                self.chasePlayer()
            self.ap -= 1
        return


def enemyAction():
    for monster in enemies:
        monster.action()
        pass


def spawn(x, y, facing, health, hearingStr, ap=0):
    monster_id = Monster(x, y, facing, health, hearingStr, ap)
    enemies.append(monster_id)
    return
