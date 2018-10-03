import level, os, common, player, time, sys, keyboard, echo, copy, color, enemy

def main(dev=0):
    level.load_level(sys.path[0]+'/maps/devMap')
    level.paint_vision()
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
            player.attack()
        if key == '0':
            break
        if dev == 0:    # def mode 0
            level.paint_vision()
        else:           # dev mode 1
            if player.x == enemy.m.x & player.y == enemy.m.y:
                print('KABUUUMM')
                enemy.m = ''
            devMap = copy.deepcopy(level.world)
            devMap[player.y][player.x] = (color.green+'T'+color.white)
            devMap[enemy.m.y][enemy.m.x] = (color.red+'E'+color.white)
            for i in devMap:
                print(''.join(i))
            print(f'Player Health: {player.health}')
            print(f'Enemy Health: {enemy.enemies[0].health}')
            print(f'Facing: {player.facing}')
    print(str(player.x) + '-' + str(player.y))
    return 1