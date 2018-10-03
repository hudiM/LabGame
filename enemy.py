import common, level

enemies = []

class Monster:
    def __init__(self, health, y, x, facing):
        self.y = y
        self.x = x
        self.health = health
        self.facing = facing

def spawn(health, x, y, facing):
    monster_id = Monster(10 ,5, 5, 0)
    return monster_id

m = spawn(10, 5, 5, 0)
enemies.append(m)