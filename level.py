import os,sys, player

world = []

def load_level(file):
    global world
    world = []
    with open(file) as f:
        lineNum = 0
        for line in f:
            row = []
            for i in range(0, len(line)):
                if line[i] != '\n':
                    row.append(line[i])
                    if line[i] == 'P':
                        player.x = i
                        player.y = lineNum
            world.append(row)
            lineNum+=1
    return