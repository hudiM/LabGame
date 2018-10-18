import os
import menu


def main():
    return menu.main_menu()


os.system('clear')
state = 0
while state == 0:
    state = main()
    # os.system('clear')
