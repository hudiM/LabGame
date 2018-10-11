import os
import level
import player
import enemy
import globalLogic
import color
import copy
import common


def openConsole():
    os.system('clear')
    print(f'Player Health: {player.health}')
    display()
    cmd = input(color.orange+'input'+color.baseColor+': ').split(' ')
    if cmd[0] == 'player':
        if cmd[1] in ['hp', 'health']:
            player.health = int(cmd[2])
        if cmd[1] in ['tp', 'teleport']:
            player.x = int(cmd[2])
            player.y = int(cmd[3])
        if cmd[1] == 'face':
            player.facing = int(cmd[2])
    if cmd[0] in ['devmode', 'devmap']:
        if cmd[1] == '0':
            globalLogic.dev = 0
        if cmd[1] == '1':
            globalLogic.dev = 1
        if cmd[1] == '2':
            globalLogic.dev = 2
    if cmd[0] == 'enemy':
        if cmd[1] == 'spawn':
            enemy.spawn(int(cmd[2]), int(cmd[3]), int(cmd[4]), int(cmd[5]))
    os.system('clear')
    if cmd[0] == 'printerr':
        common.printErr(''.join(cmd[1:]))
    print(f'Player Health: {player.health}')
    return


def display():
    if globalLogic.dev == 0:    # def mode 0
        level.paint_vision()
    elif globalLogic.dev == 1:
        level.paint_level()
    elif globalLogic.dev == 2:           # dev mode 2
        devMap = copy.deepcopy(level.world)
        devMap[player.y][player.x] = (color.green+'T'+color.reset)
        for monster in enemy.enemies:
            devMap[monster.y][monster.x] = (color.red+'E'+color.reset)
        for i in devMap:
            print(''.join(i))
        print(f'Facing: {player.facing}')
