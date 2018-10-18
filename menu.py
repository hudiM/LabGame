import os
import keyboard
import level
import sys
import globalLogic
import time

SAVE_GAME_PATH = "/saves/"
NEW_GAME_PATH = "/maps/"


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
    while True:
        number_of_players = input("Number of players (1 or 2): ")
        if number_of_players.isdigit and int(number_of_players) in [1,2]:
            break
    player_names = []
    for i in range(int(number_of_players)):
        while True:
            player_name = input("Name of Player {}: ".format(i+1))
            if player_name != "":
                player_names.append(player_name)
                break
            else:
                print("Please input a name!")
    level.load_level(sys.path[0]+'/maps/level1.inf', int(number_of_players), player_names)
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
        elif key == "l":
            try:
                level_to_load = input("Insert filename without extension: ")
                level.load_level(sys.path[0] + SAVE_GAME_PATH + level_to_load + ".sav")
                error = globalLogic.main()
            except FileNotFoundError:
                print_load_menu(saves, list_stage)
                print("{}.sav does not exist".format(sys.path[0] + SAVE_GAME_PATH + level_to_load))

        elif key in [str(i) for i in range(10)]:
            if int(key) == 0:
                in_load_menu = False
            if int(key) > 0:
                if int(key) <= len(saves) - list_stage * 9:
                    os.system('clear')
                    level.load_level(sys.path[0] + SAVE_GAME_PATH + saves[int(key)-1 + 9*list_stage])
                    for i in range(30):
                        level.save_game("test_save"+str(i))
                    error = globalLogic.main()
                    in_load_menu = False


def print_load_menu(saves, list_stage):
    upper_arrow = "▲" if list_stage > 0 else "■"
    lower_arrow = "▼" if list_stage < int(len(saves)/9) else "■"
    print("Total number of saves: {}\nListing saves {} to {}".format(
        len(saves), list_stage*9 + 1 if len(saves) > 0 else 0, min((list_stage + 1)*9, len(saves)))
        )
    print("-"*10+upper_arrow+"-"*10)
    for list_number in range(9):
        if 9*list_stage + list_number < len(saves):
            print(str(list_number + 1), "-", saves[9*list_stage + list_number][:-4])
        else:
            print("")
    print("-"*10+lower_arrow+"-"*10)
    print("0 Back to main menu")
    print("L Load by filename")
