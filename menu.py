import os
import keyboard
import level
import sys
import globalLogic


def in_game_menu():
    pass


def main_menu():
    while 1:
        os.system('clear')
        print('''
1. \033[38;2;255;255;100mN\033[38;2;255;255;255mew Game
2. \033[38;2;255;255;100mL\033[38;2;255;255;255moad Game
3. \033[38;2;255;255;100mE\033[38;2;255;255;255mxit Game
''')
        key = keyboard.getch()
        if key in ["n", "1"]:
            new_game_menu()
            break
        elif key in ["l", "2"]:
            load_game_menu()
        elif key in ["e", "3"]:
            print("Ending game")
            break


def new_game_menu():
    os.system('clear')
    level.load_level(sys.path[0]+'/maps/devMap.inf')
    player.spawn(2, 2, 2, 5)
    player.spawn(1, 1, 2, 5)
    enemy.spawn(8, 8, 0, 3, 5)
    error = globalLogic.main()
    return error


def load_game_menu():
    os.system('clear')
    in_load_menu = True
    saves = sorted(level.get_save_files())
    list_stage = 0
    print_load_menu(saves, list_stage)
    while in_load_menu:
        key = keyboard.getch()
        if key == "A":
            if list_stage > 0:
                list_stage -= 1
                os.system('clear')
                print_load_menu(saves, list_stage)
        elif key == "B":
            if list_stage < int((len(saves)-1)/9):
                list_stage += 1
                os.system('clear')
                print_load_menu(saves, list_stage)
        elif key in [str(i) for i in range(10)]:
            if int(key) == 0:
                in_load_menu = False
            if int(key) > 0:
                if int(key) <= len(saves) - list_stage * 9:
                    os.system('clear')
                    level.load_level(sys.path[0]+'/maps/'+saves[int(key)-1 + 9*list_stage])
                    error = globalLogic.main()
                    in_load_menu = False


def print_load_menu(saves, list_stage):
    print("Total number of saves: {}\nListing saves {} to {}".format(
        len(saves), list_stage*9 + 1, min((list_stage + 1)*9, len(saves)))
        )
    print("-"*10+"▲"+"-"*10)
    for list_number in range(9):
        if 9*list_stage + list_number < len(saves):
            print(str(list_number + 1), "-", saves[9*list_stage + list_number][:-4])
        else:
            break
    print("-"*10+"▼"+"-"*10)
    print("0 Back to main menu")
