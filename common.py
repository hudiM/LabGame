import color


def printErr(error):
    print(color.reset+'['+color.red+'Error'+color.reset+'] '+str(error)+'.'+color.reset)
    return


def printWarning(error):
    print(color.reset+'['+color.orange+'Warning'+color.reset+'] '+str(error)+'.'+color.reset)
    return


def printDebug(debugmsg):
    print(color.reset+'['+color.aqua+'Debug'+color.reset+'] '+str(debugmsg)+'.'+color.reset)
    return


def printDebugS(debugmsg):
    print(color.reset+'['+color.aqua+'Debug'+color.reset+'] '+str(debugmsg)+color.green+' begin'+color.reset+'.')
    return


def printDebugE(debugmsg):
    print(color.reset+'['+color.aqua+'Debug'+color.reset+'] '+str(debugmsg)+color.red+' end'+color.reset+'.')
    return


def printGameOver():
    print(''' ██████╗ ██╗████████╗     ██████╗ ██╗   ██╗██████╗
██╔════╝ ██║╚══██╔══╝    ██╔════╝ ██║   ██║██╔══██╗
██║  ███╗██║   ██║       ██║  ███╗██║   ██║██║  ██║
██║   ██║██║   ██║       ██║   ██║██║   ██║██║  ██║
╚██████╔╝██║   ██║       ╚██████╔╝╚██████╔╝██████╔╝
 ╚═════╝ ╚═╝   ╚═╝        ╚═════╝  ╚═════╝ ╚═════╝ ''')
    return


def printGameWon():
    print('''   ____                            _         _       _   _
  / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __
 | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \\
 | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | |
  \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|
                   |___/''')
    return


def printMainMenu():
    print('''{}
▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █   ██████        ▄▄▄▄    █    ██   ▄████   ██████
▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ ▒██    ▒       ▓█████▄  ██  ▓██▒ ██▒ ▀█▒▒██    ▒
░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄         ▒██▒ ▄██▓██  ▒██░▒██░▄▄▄░░ ▓██▄
░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒  &   ▒██░█▀  ▓▓█  ░██░░▓█  ██▓  ▒   ██▒
░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░▒██████▒▒      ░▓█  ▀█▓▒▒█████▓ ░▒▓███▀▒▒██████▒▒
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░      ░▒▓███▀▒░▒▓▒ ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░
 ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░      ▒░▒   ░ ░░▒░ ░ ░   ░   ░ ░ ░▒  ░ ░
 ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░         ░    ░  ░░░ ░ ░ ░ ░   ░ ░  ░  ░
   ░       ░              ░       ░    ░  ░    ░ ░           ░       ░         ░         ░           ░       ░
 ░                                                                                  ░
{}
1. \033[38;2;255;255;100mN\033[38;2;255;255;255mew Game
2. \033[38;2;255;255;100mL\033[38;2;255;255;255moad Game
3. \033[38;2;255;255;100mE\033[38;2;255;255;255mxit Game
'''.format(color.red, color.white))
    return


def printQuit():
    print('''   ____                 _ _
  / ___| ___   ___   __| | |__  _   _  ___
 | |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \\
 | |_| | (_) | (_) | (_| | |_) | |_| |  __/
  \____|\___/ \___/ \__,_|_.__/ \__, |\___|
                                |___/      ''')
    return


def keyInput():
    pressedKey = input('Key: ')
    if pressedKey == 'w':
        pressedKey = 'up'
        return pressedKey
    if pressedKey == 's':
        pressedKey = 'down'
        return pressedKey
    if pressedKey == 'a':
        pressedKey = 'left'
        return pressedKey
    if pressedKey == 'd':
        pressedKey = 'right'
        return pressedKey
    if pressedKey == '0':
        pressedKey = 'esc'
        return pressedKey
    pressedKey = None
    return pressedKey
