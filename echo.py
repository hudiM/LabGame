import level, math

def read_zone(source,hearDistance):
    world = level.world
    hearingDistance = [ 0 ]
    hearingZone = [ [ source[0] , source[1] ], ]
    lastElementID = 0
    currentElementID = 0
    for step in range(1,hearDistance+1):
        for element in range(currentElementID,len(hearingDistance)):
            # print(hearingZone[element][1],hearingZone[element][0])
            for facing in range(0,4):
                x = int(math.cos(facing * math.pi/2) + hearingZone[element][1])
                y = int(math.sin(facing * math.pi/2) + hearingZone[element][0])
                # print("X",x,"Y",y)
                if world[y][x] not in ["#"] and [y,x] not in hearingZone:
                    hearingZone.append([y,x])
                    hearingDistance.append(step)
        currentElementID = lastElementID
        lastElementID = len(hearingDistance)
        

    return hearingDistance , hearingZone
