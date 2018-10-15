import level
import os
import common
import player
import time
import sys
import keyboard
import echo
import copy
import color
import enemy
import developerConsole

stop = 0
dev = 1


def main():
    global stop, dev
    level.load_level(sys.path[0]+'/maps/level1')
    player.spawn(2, 2, 0, 50)
    print(f'Player Health: {player.players[0].health}')
    # level.paint_vision()
    while(1):
        #  --------------- dev mode 0 ----------------------
        if dev == 0:
            level.paint_vision()
        #  --------------- dev mode 1 ----------------------
        elif dev == 1:
            level.paint_level()
        #  --------------- dev mode 2 ----------------------
        elif dev == 2:
            player.players[0].hearZone = echo.read_zone([player.players[0].x, player.players[0].y], 8)
            devMap = copy.deepcopy(level.world)
            for item in list(player.players[0].hearZone.items()):
                devMap[item[0][1]][item[0][0]] = color.lightblue+str(item[1])+color.reset
                # devMap[i[1][1]][i[1][0]] = (color.blue+str(i[0])+color.reset)
            devMap[player.players[0].y][player.players[0].x] = (color.green+'P'+color.reset)
            for monster in enemy.enemies:
                devMap[monster.y][monster.x] = (color.red+'E'+color.reset)
            for i in devMap:
                print(''.join(i))
            print(f'Facing: {player.players[0].facing}')
        #  -------------------------------------------------
        key = keyboard.getch()
        os.system('clear')
        print(f'Player Health: {player.players[0].health}')
        if key == 'w':
            player.players[0].move("forward")
        if key == 's':
            player.players[0].move("backward")
        if key == "a":
            player.players[0].turn("left")
        if key == "d":
            player.players[0].turn("right")
        if key == "f":
            player.players[0].attack()
        if key == "r":
            enemy.enemyAction()
        if key == '0':
            developerConsole.openConsole()
        if player.players[0].isExit() or key == 'e' or stop == 1:
            break
    os.system('clear')
    if stop == 1:
        print('Git Gud!')
    if stop == 2:
        print('Congratulations you got out! Somehow.')
    return 1
