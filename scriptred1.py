from random import randint 
import math

name = 'sample2'
#Move to 2,2
#From 2,3

#UP = 3 
#DOWN = 1
#LEFT = 4
#RIGHT = 2
def getIslandCenter(pirate):
   
    up,entity_up = pirate.investigate_up()
    down,entity_down = pirate.investigate_down()
    left,entity_left= pirate.investigate_left()
    right,entity_right= pirate.investigate_right()
    ne,entity_ne = pirate.investigate_ne()
    nw,entity_nw = pirate.investigate_nw()
    se,entity_se = pirate.investigate_se()
    sw,entity_sw = pirate.investigate_sw()
    current,entity_current = pirate.investigate_current()
    island_Coord = 0
    island_string = up + down + left + right + ne + nw + se + sw
    island_num = 0
    if '1' in island_string:
         island_num = 1
    elif '2' in island_string:
         island_num = 2
    elif '3' in island_string:
         island_num = 3
    x_c = None 
    y_c = None
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 0
    if not 'island' in up and  'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 1
    if  'island' in up and  'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 2
    if  'island' in up and  'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and  'island' in nw:
        island_Coord = 3
    if  'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and  'island' in nw:
        island_Coord = 4
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and  'island' in nw:
        island_Coord = 5
    if not 'island' in up and  'island' in ne and  "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 6
    if  'island' in up and  'island' in ne and  "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 7
    if  'island' in up and  'island' in ne and  "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 8
    if  'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 9
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and not 'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 10
    if not 'island' in up and  'island' in ne and  "island" in right and  'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 11
    if  'island' in up and  'island' in ne and  "island" in right and  'island' in se and  'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 12
    if  'island' in up and  'island' in ne and  "island" in right and  'island' in se and  'island' in down and  'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 13
    if  'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and  'island' in down and  'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 14
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and  'island' in sw and  'island' in left and  'island' in nw:
        island_Coord = 15
    if not 'island' in up and not 'island' in ne and  "island" in right and  'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 16
    if not 'island' in up and not 'island' in ne and "island" in right and  'island' in se and  'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 17
    if not 'island' in up and not 'island' in ne and "island" in right and 'island' in se and 'island' in down and 'island' in sw and 'island' in left and not 'island' in nw:
        island_Coord = 18
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and  'island' in down and  'island' in sw and  'island' in left and not 'island' in nw:
        island_Coord = 19
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and  'island' in sw and  'island' in left and not 'island' in nw:
        island_Coord = 20
    if not 'island' in up and not 'island' in ne and not "island" in right and  'island' in se and not 'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 21
    if not 'island' in up and not 'island' in ne and not "island" in right and  'island' in se and  'island' in down and not 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 22
    if not 'island' in up and not 'island' in ne and not "island" in right and 'island' in se and 'island' in down and  'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 23
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and 'island' in down and 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 24
    if not 'island' in up and not 'island' in ne and not "island" in right and not 'island' in se and not 'island' in down and 'island' in sw and not 'island' in left and not 'island' in nw:
        island_Coord = 25
    x,y = pirate.getPosition()
    if island_Coord == 1:
        x_c = x + 2
        y_c = y - 2
    if island_Coord == 2:
            x_c = x + 1
            y_c = y - 2
    if island_Coord == 3:
            x_c = x 
            y_c = y - 2
    if island_Coord == 4:
            x_c = x - 1
            y_c = y - 2
    if island_Coord == 5:
            x_c = x - 2
            y_c = y - 2
    if island_Coord == 6:
            x_c = x + 2
            y_c = y - 1 
    if island_Coord == 7:
            x_c = x + 1
            y_c = y - 1
    if island_Coord == 8:
            x_c = x
            y_c = y - 1
    if island_Coord == 9:
            x_c = x - 1
            y_c = y - 1
    if island_Coord == 10:
            x_c = x - 2
            y_c = y - 1
    if island_Coord == 11:
            x_c = x + 2
            y_c = y
    if island_Coord == 12:
            x_c = x + 1
            y_c = y
    if island_Coord == 13:
            x_c = x 
            y_c = y 
    if island_Coord == 14:
            x_c = x - 1
            y_c = y
    if island_Coord == 15:
            x_c = x - 2
            y_c = y
    if island_Coord == 16:
            x_c = x + 2
            y_c = y + 1
    if island_Coord == 17:
            x_c = x + 1
            y_c = y + 1
    if island_Coord == 18:
            x_c = x
            y_c = y + 1
    if island_Coord == 19:
            x_c = x - 1
            y_c = y + 1
    if island_Coord == 20:
            x_c = x - 2
            y_c = y + 1
    if island_Coord == 21:
            x_c = x + 2
            y_c = y + 2
    if island_Coord == 22:
            x_c = x + 1
            y_c = y + 2
    if island_Coord == 23:
            x_c = x
            y_c = y + 2
    if island_Coord == 24:
            x_c = x - 1
            y_c = y + 2
    if island_Coord == 25:
            x_c = x - 2
            y_c = y + 2
    if island_Coord ==0:
         return None
    return (x_c,y_c,island_num)
def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    ne = pirate.investigate_ne()
    nw = pirate.investigate_nw()
    se = pirate.investigate_se()
    sw = pirate.investigate_sw()
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    x,y = pirate.getPosition()
    id = pirate.getID()
    try:
        id = int(id)+1
    except:
        id = 1
    if y==id-1:
        return moveTo(0,id-1,pirate)
    elif x == pirate.getDimensionX() - 1:
       return  moveTo(0,id-1,pirate)
    else:
       return  moveTo(pirate.getDimensionX() - 1,id-1,pirate)

def findEnemyAtIsalnd(x_c,y_c,pirate):

    coord_list = [(-1,-1),(-1,0),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
    id = pirate.getID()
    try:
        id = int(id)+1
    except:
        id = 1
    movex, movey = coord_list[id%9]
    return moveTo(x_c+movex,y_c+movey,pirate)


def ActPirate(pirate):
    x_self, y_self = pirate.getPosition()
    # if pirate.getCurrentFrame()==1:
    #     pirate.setTeamSignal(f'{x},{y}')

    id = pirate.getID()
    try:
        id = int(id)+1
    except:
        id = 1

    # id = id%40
    # print(sig)
    # if sig == "reached":
    if getIslandCenter(pirate):
             x_c , y_c,island_num = getIslandCenter(pirate)
             l = pirate.trackPlayers()
             s = pirate.getTeamSignal()
             t = s.split(",")
            #  print(s)
            #  print((island_num-1)*2+1)
             if t[(island_num-1) * 2] == "" and t[(island_num-1) * 2 + 1] == "":
                    if(island_num == 1):
                        st = str(x_c) + "," + str(y_c) + "," + t[2] + "," + t[3] + "," + t[4] + "," + t[5] 
                        pirate.setTeamSignal(st)
                    elif island_num == 2:
                        st = t[0] + "," + t[1] + "," + str(x_c) + "," + str(y_c) + "," + t[4] + "," + t[5]
                        pirate.setTeamSignal(st)
                    elif island_num == 3:
                         st = t[0] + "," + t[1] + "," + t[2] + "," + t[3] + "," + str(x_c) + "," + str(y_c)
                         pirate.setTeamSignal(st)
    if pirate.getCurrentFrame()>200:
        
        
        l = pirate.trackPlayers()
        if l[0] != 'myCaptured' and l[1]=='myCaptured' and l[2]=='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x = int(t[0])
                y = int(t[1])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif(id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000:
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                else:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                return moveTo(x+movex,y+movey,pirate)
            except:
                return spread(pirate)
        elif l[0] == 'myCaptured' and l[1]!='myCaptured' and l[2]=='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x = int(t[2])
                y = int(t[3])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                return moveTo(x+movex,y+movey,pirate)
            except:
                return spread(pirate)
        elif l[0] == 'myCaptured' and l[1]=='myCaptured' and l[2]!='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x = int(t[4])
                y = int(t[5])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                return moveTo(x+movex,y+movey,pirate)
            except:
                return spread(pirate)
        elif l[0] == 'myCaptured' and l[1]!='myCaptured' and l[2]!='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x2 = int(t[2])
                y2 = int(t[3])
                x3 = int(t[4])
                y3 = int(t[5])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                mdis2 = abs(x2 + movex - x_self) + abs(y2 + movey - y_self)
                mdis3 = abs(x3 + movex - x_self) + abs(y3 + movey - y_self)
                if(mdis2 < mdis3):
                     return moveTo(x2 + movex, y2 + movey, pirate)
                else:
                     return moveTo(x3 + movex, y3 + movey, pirate)
            except:
                return spread(pirate)
        elif l[0] != 'myCaptured' and l[1]!='myCaptured' and l[2]=='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x1 = int(t[0])
                y1 = int(t[1])
                x2 = int(t[2])
                y2 = int(t[3])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                mdis2 = abs(x2 + movex - x_self) + abs(y2 + movey - y_self)
                mdis1 = abs(x1 + movex - x_self) + abs(y1 + movey - y_self)
                if(mdis2 < mdis1):
                     return moveTo(x2 + movex, y2 + movey, pirate)
                else:
                     return moveTo(x1 + movex, y1 + movey, pirate)
            except:
                return spread(pirate)
        elif l[0] != 'myCaptured' and l[1]=='myCaptured' and l[2]!='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x1 = int(t[0])
                y1 = int(t[1])
                x3 = int(t[4])
                y3 = int(t[5])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                mdis1 = abs(x1 + movex - x_self) + abs(y1 + movey - y_self)
                mdis3 = abs(x3 + movex - x_self) + abs(y3 + movey - y_self)
                if(mdis1 < mdis3):
                     return moveTo(x1 + movex, y1 + movey, pirate)
                else:
                     return moveTo(x3 + movex, y3 + movey, pirate)
            except:
                return spread(pirate)
        elif l[0] != 'myCaptured' and l[1]!='myCaptured' and l[2]!='myCaptured':
            s = pirate.getTeamSignal()
            t = s.split(",")
            try:
                x1 = int(t[0])
                y1 = int(t[1])
                x2 = int(t[2])
                y2 = int(t[3])
                x3 = int(t[4])
                y3 = int(t[5])
                #i call this part the mating ritual
                coord_list = [(2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2),(2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),(2,0),(1,0),(0,0),(-1,0),(-2,0),(2,1),(1,1),(0,1),(-1,1),(-2,1),(2,2),(1,2),(0,2),(-1,2),(-2,2)]
                outerMappingList = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6]
                innerMappingList = [7,12,17,18,19,14,9,8]
                id = int(pirate.getID())
                if (id-1)%25  in outerMappingList:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                mdis1 = abs(x1 + movex - x_self) + abs(y1 + movey - y_self)
                mdis2 = abs(x2 + movex - x_self) + abs(y2 + movey - y_self)
                mdis3 = abs(x3 + movex - x_self) + abs(y3 + movey - y_self)
                if(mdis2 < mdis3 and mdis2 < mdis1):
                     return moveTo(x2 + movex, y2 + movey, pirate)
                elif (mdis1 < mdis3 and mdis1 < mdis2):
                     return moveTo(x1 + movex, y1 + movey, pirate)
                else:
                     return moveTo(x3 + movex, y3 + movey, pirate)
            except:
                return spread(pirate)
        else:
            return spread(pirate)
    else:
        
        # a= pirate.getID()
        id = (int(pirate.getID())-1)
        a=id%pirate.getDimensionY()
        if a%40>40:
            sig = pirate.getTeamSignal()
            try:
                sig_list = sig.split(',')
                a_spawn = pirate.getDeployPoint()[0]
                b_spawn = pirate.getDeployPoint()[1]
            except:
                a_spawn, b_spawn = (40-1,0)
            width = pirate.getDimensionX()-1
            height = pirate.getDimensionY()-1
            x_self, y_self = pirate.getPosition()
            if a_spawn == 0 and b_spawn == 0:
                if y_self == a-1:
                    return moveTo(width, y_self, pirate)
                else :
                    return moveTo(x_self, a-1, pirate)
            if a_spawn == width and b_spawn == 0:
                if y_self == a-1:
                    return moveTo(0, y_self, pirate)
                else :
                    return moveTo(x_self, a-1, pirate)
            if a_spawn == 0 and b_spawn == height:
                if y_self == height-a-1:
                    return moveTo(width, y_self, pirate)
                else :
                    return moveTo(x_self, height-a-1, pirate)
            if a_spawn == width and b_spawn == height:
                if y_self == height-a-1:
                    return moveTo(0, y_self, pirate)
                else :
                    return moveTo(x_self, height-a-1, pirate)
            return 0
        else:
            # print('Reached here')
            #The initial 8 ships will move according to this
            try:
                a_spawn = pirate.getDeployPoint()[0]
                b_spawn = pirate.getDeployPoint()[1]
            except:
                a_spawn, b_spawn = (40-1,0)
            width = pirate.getDimensionX()-1
            height = pirate.getDimensionY()-1
            x_self, y_self = pirate.getPosition()
            try:
                counter = int(pirate.getSignal())
            except:
                counter = 0
            # print(f'y_self = {y_self} x_self = {x_self} a+counter = {a + counter}')
            if counter%2 == 0 and id<8:
                if a_spawn == 0 and b_spawn == 0:
                    if y_self == a+counter and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != a+counter and x_self !=width :
                        return moveTo(x_self, a+counter, pirate)
                if a_spawn == width and b_spawn == 0:
                    if y_self == a+counter and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != a+counter and x_self !=0 :
                        return moveTo(x_self, a+counter,pirate)
                if a_spawn == 0 and b_spawn == height:
                    if y_self == height-a+counter and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != height-a+counter and x_self !=width :
                        return moveTo(x_self, height-a+counter, pirate)
                if a_spawn == width and b_spawn == height:
                    if y_self == height-a+counter and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != height-a+counter and x_self !=0:
                        return moveTo(x_self, height-a+counter, pirate)
                    
            elif counter%2!=0 and id<8:
                if a_spawn == 0 and b_spawn == 0:
                    if y_self == a+counter and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != a+counter and x_self !=0 :
                        return moveTo(x_self, a+counter, pirate)
                if a_spawn == width and b_spawn == 0:
                    if y_self == a+counter and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != a+counter and x_self !=width :
                        return moveTo(x_self, a+counter,pirate)
                if a_spawn == 0 and b_spawn == height:
                    if y_self == height-a+counter and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != height-a+counter and x_self !=0 :
                        return moveTo(x_self, height-a+counter, pirate)
                if a_spawn == width and b_spawn == height:
                    if y_self == height-a+counter and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != height-a+counter and x_self !=width:
                        return moveTo(x_self, height-a+counter, pirate)
            
            elif counter%2 == 0 and id>=8:
                if a_spawn == 0 and b_spawn == 0:
                    if y_self == a and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != a and x_self !=width :
                        return moveTo(x_self, a, pirate)
                if a_spawn == width and b_spawn == 0:
                    if y_self == a and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != a and x_self !=0 :
                        return moveTo(x_self, a,pirate)
                if a_spawn == 0 and b_spawn == height:
                    if y_self == height-a and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != height-a and x_self !=width :
                        return moveTo(x_self, height-a, pirate)
                if a_spawn == width and b_spawn == height:
                    if y_self == height-a and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != height-a and x_self !=0:
                        return moveTo(x_self, height-a, pirate)
            elif counter%2 != 0 and id>=8:
                if a_spawn == 0 and b_spawn == 0:
                    if y_self == a and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != a and x_self !=0 :
                        return moveTo(x_self, a, pirate)
                if a_spawn == width and b_spawn == 0:
                    if y_self == a and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != a and x_self !=width :
                        return moveTo(x_self, a,pirate)
                if a_spawn == 0 and b_spawn == height:
                    if y_self == height-a and x_self != 0:
                        return moveTo(0, y_self, pirate)
                    elif y_self != height-a and x_self !=0 :
                        return moveTo(x_self, height-a, pirate)
                if a_spawn == width and b_spawn == height:
                    if y_self == height-a and x_self != width:
                        return moveTo(width, y_self, pirate)
                    elif y_self != height-a and x_self !=width:
                        return moveTo(x_self, height-a, pirate)

                
            #Check if one route is over
            #If counter is even then route is from x = a_spawn to x = |width - a_spawn|
            #If counter is odd then route is from x = |width - a_spawn| to x=a_spawn
            # print('Checking for route completion')
            # print(f'Counter = {counter}')
            if counter%2==0:
                # print('Even')
                if id <8:
                    if y_self==a + counter and x_self == abs(width - a_spawn) and b_spawn == 0:
                        # print('Fired')
                        counter +=1
                        pirate.setSignal(str(counter))
                        return moveTo(abs(width-a_spawn)+1,a+counter+1,pirate)
                    if y_self==height -a + counter and x_self ==abs(width - a_spawn) and b_spawn == height:
                        # print('Fired')
                        # y_init = 39 - 1 - 0 + 1 = 39
                        #y_final = 39 - 1 -1 +1
                        counter -=1
                        pirate.setSignal(str(counter))
                        # print(f'Move To: {moveTo(abs(width-a_spawn)+1,height - a-counter+1,pirate)}')
                        return moveTo(abs(width-a_spawn)+1,height - a+counter-1,pirate)
                else:
                    if y_self == a and x_self == abs(width-a_spawn) and b_spawn == 0 :
                         counter+=1
                         pirate.setSignal(str(counter))
                         return moveTo(abs(width-a_spawn)+1,a,pirate)
                    elif y_self == height - a and x_self == abs(width - a_spawn) and b_spawn == height:
                         counter+=1
                         pirate.setSignal(str(counter))
                         return moveTo(abs(width-a_spawn)+1,a,pirate)
                         
            else:
                # print('Odd')
                if id<8:
                    if y_self==a + counter and x_self ==a_spawn and b_spawn == 0:
                        # print('Fired')
                        counter +=1
                        pirate.setSignal(str(counter))
                        return moveTo(a_spawn-1,a+counter+1,pirate)
                    
                    if y_self==height -a + counter  and x_self ==a_spawn and b_spawn == height:
                        # print('Fired')
                        #y_init = 39 - 1 -1
                        #y_final = 39 - 1 -2
                        counter -=1
                        pirate.setSignal(str(counter))
                        return moveTo(a_spawn-1,height - a+counter-1,pirate)
                else:
                    if y_self == a and x_self == a_spawn and b_spawn == 0:
                         counter+=1
                         pirate.setSignal(str(counter))
                         return moveTo((a_spawn)-1,a,pirate)
                    elif y_self == height - a and x_self == a_spawn and b_spawn == height:
                         counter +=1
                         pirate.setSignal(str(counter))
                         return moveTo((a_spawn)-1,a,pirate)

                           




def ActTeam(team):

    if team.getCurrentFrame() == 1:
         team.setTeamSignal(',,,,,')
    l = team.trackPlayers()
    s = team.getTeamSignal()
    s1 = s.split(',')
    if team.getCurrentFrame()>200:

        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)
    print(team.getCurrentFrame())
    # if s:

    #     # island_no = int(s1[0])
    #     # print(island_no)
    #     try:
    #         signal = l[island_no - 1]
    #         if signal == "myCaptured":
    #             # team.setTeamSignal("")
    #              pass
    #     except:
            #  pass