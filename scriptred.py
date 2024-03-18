from random import randint 
import math

name = 'sample9'
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
    island_Coord = 0
    x_c = None
    y_c = None
    if 'island' in up and 'island' in right and "island" in ne:
        island_Coord = 1
    elif 'island' in up and 'island' in right and "island" in left and 'island' in ne and 'island' in nw:
        island_Coord = 2
    elif 'island' in up and 'island' in left and "island" in nw:
        island_Coord = 3
    elif 'island' in up and 'island' in right and "island" in ne and 'island' in se and 'island' in down:
        island_Coord = 4
    elif 'island' in up and 'island' in right and "island" in ne and 'island' in down and 'island' in left and 'island' in nw and 'island' in se and 'island' in sw:
        island_Coord = 5
    elif 'island' in up and 'island' in left and "island" in down and 'island' in nw and 'island' in sw:
        island_Coord = 6
    elif 'island' in right and 'island' in down and "island" in se:
        island_Coord = 7
    elif 'island' in left and 'island' in right and "island" in down and 'island' in se and 'island' in sw:
        island_Coord = 8
    elif 'island' in down and 'island' in left and "island" in sw:
        island_Coord = 9
    x,y = pirate.getPosition()
    if island_Coord == 1:
        x_c = x + 1
        y_c = y - 1
    if island_Coord == 2:
            x_c = x
            y_c = y - 1
    if island_Coord == 3:
            x_c = x - 1
            y_c = y - 1
    if island_Coord == 4:
            x_c = x + 1
            y_c = y
    if island_Coord == 5:
            x_c = x 
            y_c = y
    if island_Coord == 6:
            x_c = x - 1
            y_c = y
    if island_Coord == 7:
            x_c = x + 1
            y_c = y + 1
    if island_Coord == 8:
            x_c = x
            y_c = y + 1
    if island_Coord == 9:
            x_c = x - 1
            y_c = y + 1
    return (x_c,y_c)
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
    elif x == 39:
       return  moveTo(0,id-1,pirate)
    else:
       return  moveTo(39,id-1,pirate)

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
    x, y = pirate.getPosition()
    if pirate.getCurrentFrame()==1:
        pirate.setTeamSignal(f'{x},{y}')
    id = pirate.getID()
    try:
        id = int(id)+1
    except:
        id = 1
    # print(sig)
    # if sig == "reached":
    if pirate.getCurrentFrame()>200:
        up = pirate.investigate_up()[0]
        down = pirate.investigate_down()[0]
        left = pirate.investigate_left()[0]
        right = pirate.investigate_right()[0]
        pirate.setSignal("")
        s = pirate.trackPlayers()
        
        if (
            (up == "island1" and s[0] != "myCaptured")
            or (up == "island2" and s[1] != "myCaptured")
            or (up == "island3" and s[2] != "myCaptured")
        ):
            s = up[-1] + str(x) + "," + str(y - 1)
            pirate.setTeamSignal(s)

        if (
            (down == "island1" and s[0] != "myCaptured")
            or (down == "island2" and s[1] != "myCaptured")
            or (down == "island3" and s[2] != "myCaptured")
        ):
            s = down[-1] + str(x) + "," + str(y + 1)
            pirate.setTeamSignal(s)

        if (
            (left == "island1" and s[0] != "myCaptured")
            or (left == "island2" and s[1] != "myCaptured")
            or (left == "island3" and s[2] != "myCaptured")
        ):
            s = left[-1] + str(x - 1) + "," + str(y)
            pirate.setTeamSignal(s)

        if (
            (right == "island1" and s[0] != "myCaptured")
            or (right == "island2" and s[1] != "myCaptured")
            or (right == "island3" and s[2] != "myCaptured")
        ):
            s = right[-1] + str(x + 1) + "," + str(y)
            pirate.setTeamSignal(s)

        
        if pirate.getTeamSignal() != "":
            s = pirate.getTeamSignal()
            l = s.split(",")
            try:
                x = int(l[0][1:])
                y = int(l[1])
                return findEnemyAtIsalnd(x, y, pirate)
            except:
                return spread(pirate)

        else:
            return spread(pirate)
    else:
        
        # a= pirate.getID()
        try:
            a = int(pirate.getID())
            sig = pirate.getTeamSignal()
            try:
                sig_list = sig.split(',')
                a_spawn = int(sig_list[0])
                b_spawn = int(sig_list[1])
            except:
                a_spawn, b_spawn = (40-1,0)
            width = 40-1
            height = 40-1
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
        except:
            a = 0
            # print('Reached here')
            #The initial 8 ships will move according to this
            sig = pirate.getTeamSignal()
            try:
                sig_list = sig.split(',')
                a_spawn = int(sig_list[0])
                b_spawn = int(sig_list[1])
            except:
                a_spawn, b_spawn = (40-1,0)
            width = 40-1
            height = 40-1
            x_self, y_self = pirate.getPosition()
            try:
                counter = int(pirate.getSignal())
            except:
                counter = 0
            # print(f'y_self = {y_self} x_self = {x_self} a+counter = {a + counter}')
            if counter%2 == 0:
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
            else:
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

                
            #Check if one route is over
            #If counter is even then route is from x = a_spawn to x = |width - a_spawn|
            #If counter is odd then route is from x = |width - a_spawn| to x=a_spawn
            # print('Checking for route completion')
            # print(f'Counter = {counter}')
            if counter%2==0:
                # print('Even')
                if y==a + counter and x == abs(width - a_spawn):
                    # print('Fired')
                    counter +=1
                    pirate.setSignal(str(counter))
                    return moveTo(abs(width-a_spawn)+1,a+counter+1,pirate)
            else:
                # print('Odd')
                if y==a + counter and x ==a_spawn:
                    # print('Fired')
                    counter +=1
                    pirate.setSignal(str(counter))
                    return moveTo(a_spawn-1,a+counter+1,pirate)      




def ActTeam(team):

    # print(team.getCurrentFrame()) 
    l = team.trackPlayers()
    s = team.getTeamSignal()
    if team.getCurrentFrame()>200:

        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")