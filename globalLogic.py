import level, os, common, player, time, sys, keyboard, echo, copy, color, enemy

def main(dev=0):
    dev = 0
    level.load_level(sys.path[0]+'/maps/devMap')
    level.paint_vision()
    enemy.spawn(3,3,0,5)
    while(1):
        key = keyboard.getch()
        os.system('clear')
        if key == 'w':
            print('Debug: W')
            player.move("forward")
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
            level.paint_level()
            print(f'Facing: {player.facing}')
            print(f'Player Health: {player.health}')
        else:           # dev mode 1
            devMap = copy.deepcopy(level.world)
            devMap[player.y][player.x] = (color.green+'T'+color.white)
            for monster in enemy.enemies:
                devMap[monster.y][monster.x] = (color.red+'E'+color.white)
            for i in devMap:
                print(''.join(i))
    print(str(player.x) + '-' + str(player.y))
    return 1