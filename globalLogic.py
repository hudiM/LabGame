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
dev = 0


def main():
    global stop, dev
    level.load_level(sys.path[0]+'/maps/level1')
    print(f'Player Health: {player.health}')
    # level.paint_vision()
    while(1):
        if dev == 0:  # dev mode 0
            level.paint_vision()
        elif dev == 1:  # dev mode 1
            level.paint_level()
        elif dev == 2:  # dev mode 2
            devMap = copy.deepcopy(level.world)
            devMap[player.y][player.x] = (color.green+'T'+color.reset)
            for monster in enemy.enemies:
                devMap[monster.y][monster.x] = (color.red+'E'+color.reset)
            for i in devMap:
                print(''.join(i))
            print(f'Facing: {player.facing}')
        key = keyboard.getch()
        os.system('clear')
        print(f'Player Health: {player.health}')
        if key == 'w':
            player.move("forward")
        if key == 's':
            player.move("backward")
        if key == "a":
            player.turn("left")
        if key == "d":
            player.turn("right")
        if key == "f":
            player.attack()
        if key == "r":
            enemy.enemyAction()
        if key == '0':
            developerConsole.openConsole()
        if player.isExit() or key == 'e' or stop == 1:
            break
    os.system('clear')
    if stop == 1:
        print('Git Gud!')
    if stop == 2:
        print('Congratulations you got out! Somehow.')
    return 1
