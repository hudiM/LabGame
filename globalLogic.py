import os
import common
import devTools
import developerConsole
import keyboard
import color
import menu
import level
import player
import enemy

stop = 0
dev = 0
activeActor = 0
keys = {}


def main():
    global stop, dev, keys, activeActor
    init()
    activeVar = None
    actionVar = None
    keysP1 = ('w', 's', 'a', 'd', 'f', 'e', '0', '\r')
    keysP2 = ('A', 'B', 'C', 'D', '-', 'e', '0', '\r')
    display(activeActor)
    while(1):  # game logic
        turnVar = 0
        while(turnVar < len(player.players)):  # one round
            key = keyboard.getch()
            os.system('clear')
            if (activeActor == 0 or len(player.players) == 1) and key in keysP1:  # player 1 turn
                actionVar = keys[key][0](*keys[key][1:])
                if actionVar is not None or key == '\r':
                    activeActor = 1
                    turnVar += 1
            elif (activeActor == 1 or len(player.players) == 1) and key in keysP2:  # Player 2 turn
                actionVar = keys[key][0](*keys[key][1:])
                if actionVar is not None or key == '\r':
                    activeActor = 0
                    turnVar += 1
            display(activeActor, actionVar)
            if stop > 0:
                break
            if activeActor > len(player.players):
                break
        if actionVar is not None:
            enemy.enemyAction()
        if stop > 0:
            break
    os.system('clear')
    if stop == 1:
        common.printGameOver()
        print("\nPress enter to continue!")
        wait_for_enter()
    elif stop == 2:
        common.printGameWon()
        print("\nPress enter to continue!")
        wait_for_enter()
    level.level_clean_up()
    return 1


def stopGame(value=3):
    global stop
    stop = value
    return


def init():
    global keys, stop, activeActor
    stop = 0
    activeActor = 0
    keys = {}
    dev = 0
    keys['\r'] = (enemy.enemyAction,)
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
        keys['-'] = (player.players[1].attack,)
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


def wait_for_enter():
    while True:
        if keyboard.getch() == '\r':
            break
