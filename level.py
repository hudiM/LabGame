# color code
# \033[foreground/background;2;R;G;Bm
# foreground: 38 background: 48

import player
import enemy
import os
import math
import time
import echo
import sys
import keyboard
from copy import deepcopy

SAVE_GAME_PATH = "/saves"
DIRECTION_INDEX = ["▲", "►", "▼", "◄"]
world = []
level_name = ""
FACING_CONSTANT = 0.0
BASE_COLOR = "\033[38;2;130;150;132m"
MONSTER_COLOR = "\033[38;2;200;0;0m"
EXIT_COLOR = "\033[38;2;244;167;66m"


def get_save_files():
    return [save_name for save_name in os.listdir(sys.path[0] + SAVE_GAME_PATH) if save_name[-4:] == ".sav"]


def save_game(file_name):
    with open('{}{}/{}.sav'.format(sys.path[0], SAVE_GAME_PATH, file_name), "w") as fi:
        fi.write("layout\n")
        fi.write(level_name + "\n")

        fi.write("player\n")
        for player_ID in range(len(player.players)):
            fi.write(" ".join(("x", str(player.players[player_ID].x))) + "\n")
            fi.write(" ".join(("y", str(player.players[player_ID].y))) + "\n")
            fi.write(" ".join(("facing", str(player.players[player_ID].facing))) + "\n")
            fi.write(" ".join(("health", str(player.players[player_ID].health))) + "\n")
            fi.write(" ".join(("name", str(player.players[player_ID].name))) + "\n")
            if player_ID == len(player.players) - 1:
                fi.write("end\n")
            else:
                fi.write("step\n")

        fi.write("enemy\n")
        for enemy_ID in range(len(enemy.enemies)):
            fi.write(" ".join(("x", str(enemy.enemies[enemy_ID].x))) + "\n")
            fi.write(" ".join(("y", str(enemy.enemies[enemy_ID].y))) + "\n")
            fi.write(" ".join(("facing", str(enemy.enemies[enemy_ID].facing))) + "\n")
            fi.write(" ".join(("health", str(enemy.enemies[enemy_ID].health))) + "\n")
            fi.write(" ".join(("hearing", str(enemy.enemies[enemy_ID].hearingStr))) + "\n")
            fi.write(" ".join(("ap", str(enemy.enemies[enemy_ID].ap))) + "\n")
            if enemy_ID == len(enemy.enemies) - 1:
                fi.write("end\n")
            else:
                fi.write("step\n")


def load_level(fi, player_number=0, player_names=["Lali", "Béla"]):
    global world
    world = []
    player_number_set = True if player_number == 0 else False

    # Reading entity info file
    with open(fi) as f:

        mode = "seek"  # Start by seeking for other parts
        # In case it is loaded from a standard file
        enemy_ap = 0
        enemy_hearing = 5
        current_player_id = 0
        for line in f:
            line = line[:-1].split(" ")
            print(line)
            time.sleep(0.1)
            if mode == "seek":
                if line[0] in ["layout", "player", "trigger", "enemy", "player_number", "player_names"]:
                    mode = line[0]
                    print(mode)

            # Setting up level layout
            elif mode == "layout":
                global level_name
                level_name = line[0]
                with open(sys.path[0] + '/maps/' + line[0]) as f:
                    for line in f:
                        row = []
                        for i in range(0, len(line)):
                            if line[i] != '\n':
                                row.append(line[i])
                        world.append(row)
                mode = "seek"

            elif mode == "player_number":
                player_number = line[1]

            elif mode == "player_names":
                player_names = line[1:]

            # Looking for player properties
            elif mode == "player":
                if line[0] == "x":
                    try:
                        player_x = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "y":
                    try:
                        player_y = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "facing":
                    try:
                        player_facing = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "health":
                    try:
                        player_health = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "name":
                    try:
                        player_names[current_player_id] = int(line[1])
                    except BaseException:
                        pass
                elif line[0] in ["end", "step"]:
                    try:
                        player.spawn(player_x, player_y, player_facing, player_health, player_names[current_player_id])
                        print(player_names[current_player_id], "spawned.")
                        current_player_id += 1
                    except BaseException:
                        print("player_names:", player_names)
                        print("player_number:", current_player_id)
                        print("Failed to spawn", player_names[current_player_id])
                        time.sleep(0.5)
                    if line[0] == "end":
                        mode = "seek"
                if current_player_id >= player_number:
                    mode = "seek"

            # Looking for enemy
            elif mode == "enemy":
                if line[0] == "x":
                    try:
                        enemy_x = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "y":
                    try:
                        enemy_y = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "facing":
                    try:
                        enemy_facing = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "health":
                    try:
                        enemy_health = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "ap":
                    try:
                        enemy_ap = int(line[1])
                    except BaseException:
                        pass
                elif line[0] == "hearing":
                    try:
                        enemy_hearing = int(line[1])
                    except BaseException:
                        pass
                elif line[0] in ["step", "end"]:
                    try:
                        enemy.spawn(enemy_x, enemy_y, enemy_facing, enemy_health, enemy_hearing, enemy_ap)
                        enemy_ap = 0
                        print("Enemy spawned successfully")
                    except BaseException:
                        print("Failed to spawn enemy")
                        time.sleep(0.5)
                    if line[0] == "end":
                        mode = "seek"

    print("Level Loaded!")
    time.sleep(0.5)
    input("Press enter to continue")
    os.system('clear')


# Paints the entire level.
def paint_level():
    paint = ""
    tempWorld = deepcopy(world)

    monster_ID = 0
    for monster in enemy.enemies:
        tempWorld[monster.y][monster.x] = "M" + str(monster_ID)
        monster_ID += 1

    player_ID = 0
    for current_player in player.players:
        tempWorld[current_player.y][current_player.x] = "P" + str(player_ID)
        player_ID += 1

    for i in range(0, len(tempWorld)):
        for j in range(0, len(tempWorld[i])):
            tile = tempWorld[i][j]
            paint += paint_tile(tile)

            if j < len(world[i])-1:
                try:
                    if tile in ["#"] and world[i][j+1] in ["#"]:
                        paint += "▓"
                    else:
                        paint += "░"
                except BaseException:
                    pass

        paint += "\n"
    print(paint)


def paint_tile(tile):
    paint = ""
    if tile in ["X", " ", "T", "F"]:
        paint += "░"
    elif tile in ["#"]:
        paint += "▓"
    elif tile in ["E"]:
        paint += EXIT_COLOR + "░" + BASE_COLOR
    elif tile[0] in "P":
        player_ID = int(tile[1:])
        paint += DIRECTION_INDEX[player.players[player_ID].facing]
    elif tile[0] == "M":
        monsterID = int(tile[1:])
        paint += MONSTER_COLOR + DIRECTION_INDEX[enemy.enemies[monsterID].facing] + BASE_COLOR
    return paint


def paint_vision():
    paint = BASE_COLOR
    # creating a deep copy of the world for displayign purposes
    tempWorld = deepcopy(world)

    monsterID = 0
    for monster in enemy.enemies:
        tempWorld[monster.y][monster.x] = "M" + str(monsterID)
        monsterID += 1

    player_ID = 0
    vision = []
    hearing = []

    for current_player in player.players:
        tempWorld[current_player.y][current_player.x] = "P" + str(player_ID)
        player_ID += 1
        vision.extend(in_vision([current_player.x, current_player.y, current_player.facing], 5))
        hearing.extend(echo.read_zone([current_player.x, current_player.y], 8).keys())

    for i in range(0, len(tempWorld)):
        for j in range(0, len(tempWorld[i])):
            if [i, j] in vision:
                tile = tempWorld[i][j]
                paint += paint_tile(tile)

                # if the horizontal position is not the end then paint tiles between tiles
                if j < len(tempWorld[i])-1:
                    try:
                        if tile in ["#"] and tempWorld[i][j+1] in ["#"]:
                            paint += "▓"
                        elif tile in ["E"] and tempWorld[i][j+1] in ["E"]:
                            paint += EXIT_COLOR + "░" + BASE_COLOR
                        else:
                            paint += "░"
                    except BaseException:
                        pass
            else:
                if (j, i) in hearing:
                    tile = tempWorld[i][j]
                    if tile[0] == "M":
                        paint += MONSTER_COLOR + "■" + BASE_COLOR
                    else:
                        paint += " "
                else:
                    paint += " "
                if j < len(world[i])-1:
                    paint += " "
        paint += "\n"
    print(paint)


def in_vision(source, viewDistance=8.5):
    # vision = [[1,1],[1,2],[2,1],[2,2]] # Debug version
    vision = []
    # Setting up maximum possible vision
    couldView = []
    CeilViewDistance = math.ceil(viewDistance)

    # Check in a circle, add cells within to possible vision (couldView)
    for i in range(source[1] - CeilViewDistance, source[1] + CeilViewDistance + 1):
        for j in range(source[0] - CeilViewDistance, source[0] + CeilViewDistance + 1):
            if in_world(i, j):
                if get_distance(source, [j, i]) <= viewDistance:
                    couldView.append([i, j])

    # Testing if in view
    for coord in couldView:
        angle = ((get_angle([source[1], source[0]], coord) + (source[2] + FACING_CONSTANT) * math.pi/2) % (math.pi*2))
        if angle < math.pi * 1.3 and angle > math.pi * 0.7:
            if check_visibility([source[1], source[0]], coord):
                vision.append(coord)

    # At the end add area around player in a 3x3 area

    for i in range(0, 3):
        for j in range(0, 3):
            extraVision = [source[1] - 1 + i, source[0] - 1 + j]
            if extraVision not in vision:
                vision.append(extraVision)

    return vision


def get_angle(source, target):
    dx = target[0] - source[0]
    dy = target[1] - source[1]
    return math.atan2(dy, dx)


def get_distance(source, target):
    dx = target[0] - source[0]
    dy = target[1] - source[1]
    return (dx**2 + dy**2)**0.5


def check_visibility(source, target, step=0.75, sensitivity=0.5):
    canSee = True
    currentStep = step
    angle = get_angle(source, target)
    distance = get_distance(source, target)
    wiggleRoom = 1.0  # used for searching coordinates around current step

    # step through the distance between the target and source
    while currentStep < distance:
        coord = ([source[0] + currentStep * math.cos(angle), source[1] + currentStep * math.sin(angle)])

        # during each step, check the coordinates around the current step
        for i in range(math.floor(coord[0] - wiggleRoom), math.ceil(coord[0] + wiggleRoom)):
            for j in range(math.floor(coord[1] - wiggleRoom), math.ceil(coord[1] + wiggleRoom)):
                # if the coordinate checked is inside the world
                if in_world(i, j):
                    # if the coordinate is within [sensitivity]
                    # horizontal and vertical distance from the step
                    if abs(i - coord[0]) < sensitivity and abs(j - coord[1]) < sensitivity:
                        # if there is a wall at that wolrd coordinate (unless it's the target)
                        if world[i][j] in ["#"] and [i, j] != target:
                            # you can not see this tile
                            canSee = False
                            return canSee

        currentStep += step

    return canSee


def in_world(i, j):
    return (i >= 0 and j >= 0 and i < len(world) and j < len(world[i]))

# Fal = ▓
# Terep = ░
# Player/ Enemy = ▲ ► ▼ ◄
# Enemy in hearing range = ■
# Exit = O

# print(load_level("testmap.txt"))
