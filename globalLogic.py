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
import menu

stop = 0
dev = 0
activeActor = 0
keys = {}


def main():
    global stop, dev, keys, activeActor
    init()
    activeVar = None
    actionVar = None
    display(activeActor)
    while(1):  # game logic
        turnVar = 0
        while(turnVar < len(player.players)):  # one round
            key = keyboard.getch()
            os.system('clear')
            for pid in player.players:
                if pid.spawnid == 0 and activeActor == 0:
                    if key in ('w', 's', 'a', 'd', 'f', 'e', '0', 'r'):
                        actionVar = keys[key][0](*keys[key][1:])
                        if actionVar is not None:
                            activeActor = nextPlayerTurn(activeActor, 1)
                            if actionVar == 'exit':
                                activeActor = 1
                            turnVar += 1
                        if key == 'r':
                            activeActor = nextPlayerTurn(activeActor, 1)
                            turnVar += 1
                            break
                elif pid.spawnid == 1 and activeActor == 1:
                    if key in ('A', 'B', 'C', 'D', 'í', 'e', '0', 'r'):
                        actionVar = keys[key][0](*keys[key][1:])
                        if actionVar is not None:
                            activeActor = nextPlayerTurn(activeActor, 0)
                            if actionVar == 'exit':
                                activeActor = 0
                            turnVar += 1
                        if key == 'r':
                            activeActor = nextPlayerTurn(activeActor, 0)
                            turnVar += 1
                            break
            display(activeActor, actionVar)
            if stop > 0:
                break
            if activeActor > 1:
                break
        if actionVar is not None:
            enemy.enemyAction()
        if len(player.players) == 1:
            activeActor = player.players[0].spawnid
        if stop > 0:
            break
    os.system('clear')
    if stop == 1:
        print(color.red+'''  ▄████  ██▓▄▄▄█████▓     ▄████  █    ██ ▓█████▄ 
 ██▒ ▀█▒▓██▒▓  ██▒ ▓▒    ██▒ ▀█▒ ██  ▓██▒▒██▀ ██▌
▒██░▄▄▄░▒██▒▒ ▓██░ ▒░   ▒██░▄▄▄░▓██  ▒██░░██   █▌
░▓█  ██▓░██░░ ▓██▓ ░    ░▓█  ██▓▓▓█  ░██░░▓█▄   ▌
░▒▓███▀▒░██░  ▒██▒ ░    ░▒▓███▀▒▒▒█████▓ ░▒████▓ 
 ░▒   ▒ ░▓    ▒ ░░       ░▒   ▒ ░▒▓▒ ▒ ▒  ▒▒▓  ▒ 
  ░   ░  ▒ ░    ░         ░   ░ ░░▒░ ░ ░  ░ ▒  ▒ 
░ ░   ░  ▒ ░  ░         ░ ░   ░  ░░░ ░ ░  ░ ░  ░ 
      ░  ░                    ░    ░        ░    
                                          ░      '''+color.reset)
    if stop == 2:
        print('''   ____                            _         _       _   _
  / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __
 | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \
 | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | |
  \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|
                   |___/''')
    if stop == 3:
        print('''   ____                 _ _
  / ___| ___   ___   __| | |__  _   _  ___
 | |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \\
 | |_| | (_) | (_) | (_| | |_) | |_| |  __/
  \____|\___/ \___/ \__,_|_.__/ \__, |\___|
                                |___/      ''')
    return 1


def nextPlayerTurn(currentActor, nextActor):
    if len(player.players) == 1:
        return currentActor
    elif len(player.players) > 1:
        return nextActor


def stopGame(value=3):
    global stop
    stop = value
    return


def init():
    global keys
    keys['r'] = (enemy.enemyAction,)
    keys['e'] = (menu.in_game_menu,)
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


def display(currentPlayer, msg=None):
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
    if msg is not None and msg is not 1:
        print(msg)
    displayHealth(currentPlayer)
    return


def displayHealth(currentPlayer):
    if len(player.players) == 1:
        print(f'{player.players[0].name} health: {player.players[0].health}')
    elif len(player.players) == 2:
        if currentPlayer == 0:
            print(color.bold+color.white+f'{player.players[0].name} health: {player.players[0].health}'+color.reset)
            print(f'{player.players[1].name} health: {player.players[1].health}')
        elif currentPlayer == 1:
            print(f'{player.players[0].name} health: {player.players[0].health}')
            print(color.bold+color.white+f'{player.players[1].name} health: {player.players[1].health}'+color.reset)
    return
