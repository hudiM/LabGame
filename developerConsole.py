import os
import level
import player
import enemy
import globalLogic
import color
import devTools


def openConsole():
    os.system('clear')
    display()
    cmd = input(color.orange+'input'+color.baseColor+': ').split(' ')
    if cmd[0] in ['e', 'exit', 'q', 'quit', 'qqq']:
        globalLogic.stop = 3
    if cmd[0] == 'player':
        if cmd[1] in ['hp', 'health']:
            try:
                player.players[int(cmd[2])].health = int(cmd[3])
            except:
                pass
        if cmd[1] in ['tp', 'teleport']:
            try:
                player.players[int(cmd[2])].x = int(cmd[3])
                player.players[int(cmd[2])].y = int(cmd[4])
            except:
                pass
        if cmd[1] == 'face':
            try:
                player.players[int(cmd[2])].facing = int(cmd[3])
            except:
                pass
    if cmd[0] in ['devmode', 'devmap']:
        if cmd[1] == '0':
            globalLogic.dev = 0
        if cmd[1] == '1':
            globalLogic.dev = 1
        if cmd[1] == '2':
            globalLogic.dev = 2
        if cmd[1] == '3':
            globalLogic.dev = 3
    if cmd[0] == 'enemy':
        if cmd[1] == 'spawn':
            enemy.spawn(int(cmd[2]), int(cmd[3]), int(cmd[4]), int(cmd[5]), int(cmd[6]))
    os.system('clear')
    return


def display():
    if globalLogic.dev == 0:            # def mode 0
        level.paint_vision()
    elif globalLogic.dev == 1:          # dev mode 1
        level.paint_level()
    elif globalLogic.dev == 2:          # dev mode 2 player 1
        devTools.paint_dev(0)
    elif globalLogic.dev == 3:          # dev mode 2 player 2
        devTools.paint_dev(1)
