import level, os, common, player, time, sys

def main(dev=0):
    level.load_level(sys.path[0]+'/maps/devMap.txt')
    for i in level.world:
        print(i)
    time.sleep(0.5)
    os.system('clear')
    for i in level.world:
        print(i)
    while(1):
        key = common.keyInput()
        if key == 'up':
            player.move('forward')
        if key == 'down':
            player.move('backward')
        if key == 'left':
            player.move('left')
        if key == 'right':
            player.move('right')
        if key == 'esc':
            break
        time.sleep(2)
        os.system('clear')
        for i in level.world:
            print(i)
    print(str(player.x) + '-' + str(player.y))
    return 1