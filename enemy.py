import common, level, random, player

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
            if player.x == self.x & player.y == self.y+1:
                return 1
        return 0

    def isPlayerAround(self):
        if player.x == self.x & player.y == self.y+1:
            return 2
        elif player.x == self.x & player.y == self.y-1:
            return 0
        elif player.x == self.x+1 & player.y == self.y:
            return 1
        elif player.x == self.x-1 & player.y == self.y:
            return 3
        else:
            return -1

    def attackPlayer(self):
        print('Player damaged!')
        player.health -= 1

    def move(self):
        randomMove = random.randrange(0,6)
        if randomMove < 5:
            if self.facing == 2:
                if player.isPassable(self.x,self.y+1):
                    self.y += 1
                else:
                    self.facing -= 1
            elif self.facing == 0:
                if player.isPassable(self.x,self.y-1):
                    self.y -= 1
                else:
                    self.facing -= 1
            elif self.facing == 1:
                if player.isPassable(self.x+1,self.y):
                    self.x += 1
                else:
                    self.facing -= 1
            elif self.facing == 3:
                if player.isPassable(self.x-1,self.y):
                    self.x -= 1
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
            if self.facing == 3:
                self.attackPlayer()
            else:
                self.facing = 3
        elif self.isPlayerAround() == 2:
            if self.facing == 2:
                self.attackPlayer()
            else:
                self.facing = 2
        elif self.isPlayerAround() == 3:
            if self.facing == 1:
                self.attackPlayer()
            else:
                self.facing = 1

def enemyAction():
    for monster in enemies:
        monster.lookForPlayer()

def spawn(x, y, facing, health):
    monster_id = Monster(x, y, facing, health)
    enemies.append(monster_id)
    return