import color


def printErr(error):
    print(color.reset+'['+color.red+'Error'+color.reset+'] '+error+'.'+color.reset)
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
