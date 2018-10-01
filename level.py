# color code
# \033[foreground/background;2;R;G;Bm
# foreground: 38 background: 48

#####PPP###################

import player, enemy, os, math

direction_index = ["▲", "►", "▼", "◄"]
world = []

def load_level(file):
    global world
    world = []
    lineNum = 0
    with open(file) as f:
        for line in f:
            row = []
            for i in range(0,len(line)):
                if line[i] != '\n':
                    row.append(line[i])
                    if line[i] == 'P':
                        player.x = i
                        player.y = lineNum
            world.append(row)
            lineNum += 1
                
def paint_level():
    os.system("clear")
    paint = ""
    for i in range(0, len(world)):
        for j in range(0,len(world[i])):
            tile = world[i][j]
            if tile in ["X"," ","T","F"]:
                paint += "░"
            elif tile in ["#"]:
                paint += "▓"
            elif tile in "P":
                paint += direction_index[player.facing]

            if j < len(world[i])-1:
                try:
                    if tile in ["#"] and world[i][j+1] in ["#"]:
                        paint += "▓"
                    else:
                        paint += "░"
                except:
                    pass

        paint += "\n"
    print(paint)


# Fal = ▓
# Terep = ░
# Player/ Enemy = ▲ ► ▼ ◄
# Enemy = E
# Exit = O

# print(load_level("testmap.txt"))