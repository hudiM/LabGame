import os, globalLogic

def main():
    error = globalLogic.main(1)
    return error

os.system('clear')
state = 0
while state == 0:
    state = main()
    # os.system('clear')
