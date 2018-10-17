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
import devTools

stop = 0
dev = 2


def main():
    global stop, dev
    level.load_level(sys.path[0]+'/maps/level1')
    player.spawn(2, 2, 0, 50)
    player.spawn(36, 5, 0, 50)
    keys = {'w': (player.players[0].move, "forward"),
            's': (player.players[0].move, "backward"),
            'a': (player.players[0].turn, "left"),
            'd': (player.players[0].turn, "right"),
            'f': (player.players[0].attack,),
            'i': (player.players[1].move, "forward"),
            'k': (player.players[1].move, "backward"),
            'j': (player.players[1].turn, "left"),
            'l': (player.players[1].turn, "right"),
            'o': (player.players[1].attack,),
            'r': (enemy.enemyAction,),
            'e': (stopGame,),
            '0': (developerConsole.openConsole,)}
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
            devTools.paint_dev()
        #  -------------------------------------------------
        key = keyboard.getch()
        print(key)
        os.system('clear')
        print(f'Player Health: {player.players[0].health}')
        # keys[0][keyboard.getch()]()
        try:
            keys[key][0](*keys[key][1:])
        except:
            pass
        if stop > 0:
            break
    os.system('clear')
    if stop == 1:
        print('Git Gud!')
    if stop == 2:
        print('Congratulations you got out! Somehow.')
    if stop == 3:
        print('Goodbye!')
    return 1


def stopGame(value=3):
    global stop
    stop = value
    return
