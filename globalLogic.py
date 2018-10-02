import level, os, common, player, time, sys, keyboard

def main(dev=0):
    level.load_level(sys.path[0]+'/maps/devMap.txt')
    for i in level.world:
        print(i)
    time.sleep(0.5)
    os.system('clear')
    for i in level.world:
        print(i)
    while(1):
        key = keyboard.getch()
        print(key)
        if key == 'w':
            print('Debug: W')
            player.move("forward")
        if key == "a":
            print('Debug: A')
            player.turn("left")
        if key == "d":
            print('Debug: D')
            player.turn("right")
        if key == "e":
            print(player.facing)
        if key == '0':
            break
        os.system('clear')
        for i in level.world:
            print(i)
        print(player.facing)
    print(str(player.x) + '-' + str(player.y))
    return 1