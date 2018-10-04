import level, os, common, player, time, sys, keyboard, echo, copy, color, enemy

def main(dev=0):
    dev = 1
    level.load_level(sys.path[0]+'/maps/devMap')
    level.paint_vision()
    enemy.spawn(1,3,0,5) # debug enemy
    enemy.spawn(5,3,0,5) # debug enemy
    while(1):
        key = keyboard.getch()
        os.system('clear')
        print(f'Player Health: {player.health}')
        if key == 'w':
            print('Debug: W')
            player.move("forward")
        if key == 's':
            print('Debug: S')
            player.move("backward")
        if key == "a":
            print('Debug: A')
            player.turn("left")
        if key == "d":
            print('Debug: D')
            player.turn("right")
        if key == "f":
            print('Debug: F')
            player.attack()
        if key == "r":
            enemy.enemyAction()
        if key == '0':
            break
        if dev == 0:    # def mode 0
            level.paint_vision()
        elif dev == 1:
            level.paint_level()
        elif dev == 2:           # dev mode 2
            devMap = copy.deepcopy(level.world)
            devMap[player.y][player.x] = (color.green+'T'+color.white)
            for monster in enemy.enemies:
                devMap[monster.y][monster.x] = (color.red+'E'+color.white)
            for i in devMap:
                print(''.join(i))
            print(f'Facing: {player.facing}')
    return 1