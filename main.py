import os, io, sys, level, player, globalLogic, color

def main():
    error = globalLogic.main()
    return error

os.system('clear')
state = 0
while state == 0:
    state = main()
    # os.system('clear')
