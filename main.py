import os, globalLogic, keyboard

def main():
    print('''
1. \033[38;2;255;255;100mN\033[38;2;255;255;255mew Game
2. \033[38;2;155;155;155mL\033[38;2;125;125;125moad Game\033[38;2;255;255;255m
3. \033[38;2;255;255;100mE\033[38;2;255;255;255mxit Game
''')
    while 1:
        key = keyboard.getch()
        if key in ["n","1"]:
            os.system('clear')
            error = globalLogic.main()
            return error
        elif key in ["l","2"]:
            pass
        elif key in ["e","3"]:
            print("Ending game")
            break

os.system('clear')
state = 0
while state == 0:
    state = main()
    # os.system('clear')
