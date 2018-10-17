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
