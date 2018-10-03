import level, os, common, player, time, sys, keyboard, echo

def main(dev=0):
    level.load_level(sys.path[0]+'/maps/devMap')
    # for i in level.world:
    #     print(i)
    # time.sleep(0.5)
    # os.system('clear')
    level.paint_vision()
    value, zone = echo.read_zone([player.x,player.y] , 8)
    print(value)
    print(zone)
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
        level.paint_vision()
    print(str(player.x) + '-' + str(player.y))
    return 1