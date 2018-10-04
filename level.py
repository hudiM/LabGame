# color code
# \033[foreground/background;2;R;G;Bm
# foreground: 38 background: 48

#####PPP###################

import player, enemy, os, math, time, echo
from copy import deepcopy

direction_index = ["▲", "►", "▼", "◄"]
world = []
facingConstant = 0.0
baseColor = "\033[38;2;130;150;132m"
monsterColor = "\033[38;2;200;0;0m"
exitColor = "\033[38;2;244;167;66m"

def load_level(fi):
    global world
    world = []
    lineNum = 0
    with open(fi + ".ter") as f:
        for line in f:
            row = []
            for i in range(0,len(line)):
                if line[i] != '\n':
                    row.append(line[i])
                    # if line[i] == 'P':
                    #     player.x = i
                    #     player.y = lineNum
            world.append(row)
            lineNum += 1

    # Reading entity info file
    try:
        with open(fi + ".inf") as f:

            mode = "seek" # Start by seeking for other parts
            notFound = []
            Found = []
            for line in f:
                if mode == "seek":
                    if "player" in line:
                        mode = "player"
                    elif "trigger" in line:
                        mode = "trigger"
                    elif "enemy" in line:
                        mode = "enemy"
                # Looking for player properties
                elif mode == "player":
                    if "x" in line:
                        try:
                            player.x = int(line[2])
                            Found.append("Player X")
                        except:
                            notFound.append("Player X")
                            pass
                    elif "y" in line:
                        try:
                            player.y = int(line[2])
                            Found.append("Player Y")
                        except:
                            notFound.append("Player Y")
                            pass
                    elif "facing" in line:
                        try:
                            player.facing = int(line[len("facing")+1:])
                            Found.append("Player Facing")
                        except:
                            notFound.append("Player Facing")
                            pass
                    elif "end" in line:
                        mode = "seek"
                # Looking for enemy 
                elif mode == "enemy":
                    if "x" in line:
                        try:
                            enemy_x = int(line[2])
                        except:
                            pass
                    elif "y" in line:
                        try:
                            enemy_y = int(line[2])
                        except:
                            pass
                    elif "facing" in line:
                        try:
                            enemy_facing = int(line[len("facing")+1])
                        except:
                            pass
                    elif "health" in line:
                        try:
                            enemy_health = int(line[len("health")+1])
                        except:
                            pass
                    elif "end" in line or "step" in line:
                        try:
                            enemy.spawn(enemy_x,enemy_y,enemy_facing,enemy_health)
                        except:
                            print("Failed to spawn enemy")
                            time.sleep(0.5)
                        if "end" in line:
                            mode = "seek"

    except:
        # Temporary testing measures
        player.x = 1
        player.y = 1
        player.facing = 2
                
# paint_level() is obsolete, only use for painting the level layout!
def paint_level():
    os.system("clear")
    paint = ""
    tempWorld = deepcopy(world)
    tempWorld[player.y][player.x] = "P"
    monsterID = 0
    for monster in enemy.enemies:
        tempWorld[monster.y][monster.x] = "M" + str(monsterID)
        monsterID += 1
    for i in range(0, len(tempWorld)):
        for j in range(0,len(tempWorld[i])):
            tile = tempWorld[i][j]
            paint += paint_tile( tile )

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

def paint_tile(tile):
    paint = ""
    if tile in ["X"," ","T","F"]:
        paint += "░"
    elif tile in ["#"]:
        paint += "▓"
    elif tile in ["E"]:
        paint += exitColor + "░" + baseColor
    elif tile in "P":
        paint += direction_index[player.facing]
    elif tile[0] == "M":
        monsterID = int(tile[1:])
        paint += monsterColor + direction_index[enemy.enemies[monsterID].facing] + baseColor
    return paint

def paint_vision():
    # os.system("clear")
    paint = baseColor
    # creating a deep copy of the world for displayign purposes
    tempWorld = deepcopy(world)
    tempWorld[player.y][player.x] = "P"
    monsterID = 0
    for monster in enemy.enemies:
        tempWorld[monster.y][monster.x] = "M" + str(monsterID)
        monsterID += 1
    vision = in_vision([player.y,player.x,player.facing],5)
    hearing = echo.read_zone([player.y,player.x], 8)
    # walls = [] # For debugging purposes
    
    for i in range(0, len(tempWorld)):
        for j in range(0,len(tempWorld[i])):
            if [i,j] in vision:
                tile = tempWorld[i][j]
                paint += paint_tile( tile )

                # if the horizontal position is not the end then paint tiles between tiles
                if j < len(tempWorld[i])-1:
                    try:
                        if tile in ["#"] and tempWorld[i][j+1] in ["#"]:
                            paint += "▓"
                        elif tile in ["E"] and tempWorld[i][j+1] in ["E"]:
                            paint += exitColor + "░" + baseColor
                        else:
                            paint += "░"
                    except:
                        pass
            else:
                if [i,j] in hearing[1]:
                    tile = tempWorld[i][j]
                    if tile[0] == "M":
                        paint += monsterColor + "■" + baseColor
                    else:
                        paint += " "
                else:
                    paint += " "
                if j < len(world[i])-1:
                    paint += " "
        paint += "\n"
    print(paint)
    # print(walls)

def in_vision(source, viewDistance = 8.5):
    # vision = [[1,1],[1,2],[2,1],[2,2]] # Debug version
    vision = []
    # Setting up maximum possible vision
    couldView = []
    CeilViewDistance = math.ceil(viewDistance)

    # Check in a circle, add cells within to possible vision (couldView)
    for i in range(source[0] - CeilViewDistance, source[0] + CeilViewDistance + 1):
        for j in range(source[1] - CeilViewDistance, source[1] + CeilViewDistance + 1):
            if in_world(i,j):
                if get_distance(source,[i,j]) <= viewDistance:
                    # print(source,get_distance(source,[i,j]),[i,j])
                    couldView.append([i,j])
    
    # Testing if in view
    for coord in couldView:
        angle = (( get_angle([source[0],source[1]],coord) + ( source[2] + 
            facingConstant ) * math.pi/2 ) % ( math.pi * 2 ) )
        if angle < math.pi * 1.3 and angle > math.pi * 0.7:
            if check_visibility([source[0],source[1]],coord):
                vision.append(coord)

    # At the end add area around player in a 3x3 area

    for i in range(0,3):
        for j in range(0,3):
            extraVision = [source[0] - 1 + i, source[1] -1 + j]
            if extraVision not in vision:
                vision.append(extraVision)

    return vision

def get_angle(source,target):
    dx = target[0] - source [0]
    dy = target[1] - source [1]
    return math.atan2(dy,dx)

def get_distance(source,target):
    dx = target[0] - source [0]
    dy = target[1] - source [1]
    return (dx**2 + dy**2)**0.5

def check_visibility(source, target, step = 0.75, sensitivity = 0.5):

    canSee = True
    currentStep = step
    angle = get_angle(source,target)
    distance = get_distance(source,target)
    wiggleRoom = 1.0 # used for searching coordinates around current step
    
    # step through the distance between the target and source
    while currentStep < distance:
        coord = ([source[0] + currentStep * math.cos(angle),
            source[1] + currentStep * math.sin(angle)])

        # during each step, check the coordinates around the current step
        for i in range( math.floor( coord[0] - wiggleRoom ), math.ceil( coord[0] + wiggleRoom ) ):
            for j in range( math.floor( coord[1] - wiggleRoom ), math.ceil( coord[1] + wiggleRoom) ):
                # if the coordinate checked is inside the world
                if in_world(i,j):
                    # if the coordinate is within [sensitivity] 
                    # horizontal and vertical distance from the step
                    if abs(i - coord[0]) < sensitivity and abs(j - coord[1]) < sensitivity:
                        # if there is a wall at that wolrd coordinate (unless it's the target)
                        if world[i][j] in ["#"] and [i,j] != target:
                            # you can not see this tile
                            canSee = False
                            return canSee

        currentStep += step

    return canSee

def in_world(i,j):
    return (i >= 0 and j >= 0 and i < len(world) and j < len(world[i]) )



# Fal = ▓
# Terep = ░
# Player/ Enemy = ▲ ► ▼ ◄
# Enemy in hearing range = ■
# Exit = O

# print(load_level("testmap.txt"))

