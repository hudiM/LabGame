import level, os, common, player, time, sys, keyboard, echo, copy, color, enemy, developerConsole

stop = 0
dev = 0

def main():
    global stop, dev
    level.load_level(sys.path[0]+'/maps/level1')
    print(f'Player Health: {player.health}')
    level.paint_vision()
    #enemy.spawn(1,3,0,5) # debug enemy
    #enemy.spawn(5,3,0,5) # debug enemy
    while(1):
<<<<<<< HEAD
        if dev == 0:    # def mode 0
            level.paint_vision()
        elif dev == 1:
            level.paint_level()
        elif dev == 2:           # dev mode 2
            devMap = copy.deepcopy(level.world)
            devMap[player.y][player.x] = (color.green+'T'+color.white)
            for monster in enemy.enemies:
                devMap[monster.y][monster.x] = (color.red+'E'+color.white)
            for i in devMap:
                print(''.join(i))
            print(f'Facing: {player.facing}')
=======
        print(f'Player Health: {player.health}')
>>>>>>> 4f9bab264592605fbcd6f19266c1fc2066f8f93d
        key = keyboard.getch()
        os.system('clear')
        if key == 'w':
            # print('Debug: W')
            player.move("forward")
        if key == 's':
            # print('Debug: S')
            player.move("backward")
        if key == "a":
            # print('Debug: A')
            player.turn("left")
        if key == "d":
            # print('Debug: D')
            player.turn("right")
        if key == "f":
            # print('Debug: F')
            player.attack()
        if key == "r":
            enemy.enemyAction()
        if key == '0':
            developerConsole.openConsole()
        if player.isExit() or key == 'e' or stop == 1:
            break
    
    os.system('clear')
    if stop == 1:
        print('Git Gud!')
    if stop == 2:
        print('Congratulations you got out! Somehow.')
    return 1