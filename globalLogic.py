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
keys = {}
activeActor = 0


def main():
<<<<<<< HEAD
    global stop, dev
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
        except BaseException:
            pass
=======
    global stop, dev, keys, activeActor
    level.load_level(sys.path[0]+'/maps/devMap')
    player.spawn(2, 2, 2, 5)
    player.spawn(1, 1, 2, 5)
    enemy.spawn(8, 8, 0, 3, 5)
    init()
    activeVar = None
    display()
    while(1):  # game logic
        while(activeActor > (-1)):  # one round
            key = keyboard.getch()
            os.system('clear')
            if activeActor == 0:
                if key in ('w', 's', 'a', 'd', 'f', 'e', '0', 'r'):
                    actionVar = keys[key][0](*keys[key][1:])
                    if key == 'r':
                        activeActor += 1
            if activeActor == 1:
                if key in ('A', 'B', 'C', 'D', 'í', 'e', '0', 'r'):
                    actionVar = keys[key][0](*keys[key][1:])
                    if key == 'r':
                        activeActor += 1
            display(msg)
            common.printDebug(str(activeActor))
            if stop > 0:
                break
            if activeActor > 1:
                break
        if actionVar is not None:
            enemy.enemyAction()
        activeActor = 0
>>>>>>> 3d4450c37df375cbd16e5e2256fa10205de177d4
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


def init():
    global keys
    keys['r'] = (enemy.enemyAction,)
    keys['e'] = (stopGame,)
    keys['0'] = (developerConsole.openConsole,)
    keys['w'] = (player.players[0].move, "forward")
    keys['s'] = (player.players[0].move, "backward")
    keys['a'] = (player.players[0].turn, "left")
    keys['d'] = (player.players[0].turn, "right")
    keys['f'] = (player.players[0].attack,)
    if len(player.players) >= 2:
        keys['A'] = (player.players[1].move, "forward")
        keys['B'] = (player.players[1].move, "backward")
        keys['D'] = (player.players[1].turn, "left")
        keys['C'] = (player.players[1].turn, "right")
        keys['í'] = (player.players[1].attack,)
    return


def display(msg=None):
    #  --------------- dev mode 0 ----------------------
    if dev == 0:
        level.paint_vision()
    #  --------------- dev mode 1 ----------------------
    elif dev == 1:
        level.paint_level()
    #  --------------- dev mode 2 ----------------------
    elif dev == 2:
        devTools.paint_dev(0)
    #  --------------- dev mode 3 ----------------------
    elif dev == 3:
        devTools.paint_dev(1)
    #  -------------------------------------------------
    if msg is not None:
        print(msg)
    displayHealth()
    return


def displayHealth():
    if len(player.players) == 1:
        print(f'Player 1 health: {player.players[0].health}')
    elif len(player.players) == 2:
        print(f'Player 1 health: {player.players[0].health}')
        print(f'Player 2 health: {player.players[1].health}')
    return
