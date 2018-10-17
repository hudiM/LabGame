import echo
import copy
import player
import enemy
import level
import color


def paint_dev(showHear=0):
    player.players[0].hearZone = echo.read_zone([player.players[0].x, player.players[0].y], 8)
    devMap = copy.deepcopy(level.world)
    try:
        for item in list(player.players[showHear].hearZone.items()):
            devMap[item[0][1]][item[0][0]] = color.lightblue+str(item[1])+color.reset
    except:
        pass
    devMap[player.players[0].y][player.players[0].x] = (color.green+'P'+color.reset)
    try:
        devMap[player.players[1].y][player.players[1].x] = (color.green+'T'+color.reset)
    except:
        pass
    for monster in enemy.enemies:
        devMap[monster.y][monster.x] = (color.red+'E'+color.reset)
    for i in devMap:
        print(''.join(i))
    for pid in player.players:
        print(f'Facing: {pid.facing}')
    return
