from random import randint 
import math

name = 'def__init__'
#Move to 2,2
#From 2,3

#UP = 3 
#DOWN = 1
#LEFT = 4
#RIGHT = 2
def nearest_island(pirate):
     x,y = pirate.getPosition()
     x1,y1,x2,y2,x3,y3 = (int(pirate.getTeamSignal().split(",")[0]),int(pirate.getTeamSignal().split(",")[1]),int(pirate.getTeamSignal().split(",")[2]),int(pirate.getTeamSignal().split(",")[3]),int(pirate.getTeamSignal().split(",")[4]),int(pirate.getTeamSignal().split(",")[5]))
     mdis1 = abs(x1-x) + abs(y1-y)
     mdis2 = abs(x2-x) + abs(y2-y)
     mdis3 = abs(x3-x) + abs(y3-y)
     if(mdis1 == min(mdis1,mdis2,mdis3)):
          return 1
     elif(mdis2 == min(mdis1,mdis2,mdis3)):
          return 2
     else:
          return 3
          
     
def gundpowder_spread(pirate):
     sig = pirate.getSignal()
    #  print(f'Gunpowder Spreading called with sig:{sig}')
     sig_spreading = sig.split(',')[1]
     try:
         counter = int(sig_spreading.split(';')[-1])
        #  print(f'COunter: {counter}')
     except:
        #   print('FAiling TRY ALways')
          counter = 0
     x_self , y_self = pirate.getPosition()
     width = pirate.getDimensionX() - 1

     id = int(pirate.getID())
    #  print(f'GUnpowder SPreading CAlled WIth COunter: {counter} FOr ID: {id} ANd SIgnal SPreading:{sig_spreading}')
     if counter % 2 == 0:
         if y_self == (id + counter)%40 and x_self == 0:
              counter += 1
            #   print('Changing signal')

              pirate.setSignal(sig.split(",")[0] + ',' + 'spreading;' + str(counter))
              return moveTo(x_self,y_self + 1,pirate)
         else:
              pirate.setSignal(sig.split(",")[0] + ',' + 'spreading;' + str(counter))
     else:
          if y_self == (id + counter)%40 and x_self == width:
              counter += 1
            #   print('Changing signal')
              pirate.setSignal(sig.split(",")[0] + ',' + 'spreading;' + str(counter))
              return moveTo(x_self,y_self + 1,pirate)
          else:
               pirate.setSignal(sig.split(",")[0] + ',' + 'spreading;' + str(counter))

     if counter % 2 == 0:
          if y_self == (id + counter)%40 and x_self !=0:
            #    print(f'MOving TO 0,{y_self}')
               return moveTo(0,y_self,pirate)
          elif y_self != (id + counter)%40:
            #    print(f'MOving TO {x_self},{(id + counter)%40}')
               return moveTo(x_self,(id + counter)%40,pirate)
     else:
          if y_self == (id + counter)%40 and x_self !=width:
            #    print(f'MOving TO {width},{(id + counter)%40}')
               return moveTo(width,y_self,pirate)
          elif y_self != (id + counter)%40:
            #    print(f'MOving TO {x_self},{(id + counter)%40}')
               return moveTo(x_self,id + counter,pirate)
          
    
     
    
          
     
     
    

def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return randint(1, 4)
    if randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1
    
def moveToNearest(pirate, li):
     x,y = pirate.getPosition()
     mdis = abs(x-li[0][0]) + abs(y-li[0][1])
     m_index = 0
     for i in range(len(li)):
          if abs(x-li[i][0]) + abs(y-li[i][1]) < mdis:
               mdis = abs(x-li[i][0]) + abs(y-li[i][1])
               m_index = i
     return moveTo(li[m_index][0], li[m_index][1], pirate)
          
def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    x=x+1
    y=y+1
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    # if Pirate.getDeployPoint()[0] != 0:
    pos = [[x + i, y + radius] for i in range(-1 * radius - 1 , radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 2, -1)])
    pos.extend([[x + i, y - radius - 1] for i in range(radius - 1, -1 * radius - 2, -1)])
    pos.extend([[x - radius - 1, y + i - 1] for i in range(-1 * radius +1, radius+1)])
    # if(radius == 19):print(pos)
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveToNearest(Pirate, pos)
        else:
            return moveToNearest(Pirate, pos)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )          

# def circleAround(x, y, radius, Pirate, clockwise=True):
#     position = Pirate.getPosition()
#     rx = position[0]
#     ry = position[1]
#     # print(radius)

#     pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 2)]
#     pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
#     pos.extend([[x + i, y - radius] for i in range(radius, -1 * radius - 1, -1)])
#     pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])

#     # rpos = []
#     # l = 2*radius-1 
#     # for i in range(4*l):
#     #      if i < 2*radius-1:
#     #           rpos.append([x - radius + i ,y - radius ])
#     #      elif i < 4*radius-2:
#     #           rpos.append([x + radius - 1, y - radius + i % l])
#     #      elif i < 6*radius-3:
#     #           rpos.append([x + radius - 1 - i % l, y + radius - 1])
#     #      else:
#     #           rpos.append([x + radius - 1, y + radius - 1 - i % l])
#     # print(rpos)
               
#     if [rx, ry] not in pos:
#         print(f'not on path for radius = {radius}, moving to nearest')
#         return moveToNearest(Pirate, pos)
#     else:
#         index = pos.index([rx, ry])
#         print(f'on correct path for radius = {radius}, moving to next cell')
#         return moveTo(
#             pos[(index + (1)) % len(pos)][0],
#             pos[(index + (1)) % len(pos)][1],
#             Pirate,
#         )

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

def checkenemies(pirate):
    counter = int(pirate.getSignal().split(",")[1])
    a_spawn,b_spawn = pirate.getDeployPoint()
    width =pirate.getDimensionX()
    height = pirate.getDimensionY()
    x,y = pirate.getPosition()
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    movex, movey=(0,0)
    if(up == 'enemy'):
         if(counter%2==0):
              if(a_spawn == 0):
                   return moveTo(x+1,y,pirate)
              else:
                   return moveTo(x-1,y,pirate)
         else:
              if(a_spawn == width-1):
                   return moveTo(x+1,y,pirate)
              else:
                   return moveTo(x-1,y,pirate)
    if(down == 'enemy'): movex, movey = (0,-1)
    if(right == 'enemy'): movex, movey = (-1,0)
    if(left == 'enemy'): movex, movey = (1,0)
    if(ne == 'enemy'): movex, movey = (-1,+1)
    if(se == 'enemy'): movex, movey = (-1,-1)
    if(nw == 'enemy'): movex, movey = (+1,+1)
    if(sw == 'enemy'): movex, movey = (+1,-1)
    return moveTo(x+movex, y+movey, pirate)
         
def setconquering(pirate, island_num):
     sig = pirate.getSignal()
     t = sig.split(",")
     id = t[0]
     newsignal = ""
     for i in len(t):
          if(i!=1):
               newsignal+=t[i]+","
          else:
               newsignal+="conquering"+str(island_num)
     pirate.setSignal(newsignal)

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
    sig = pirate.getSignal()
    # if id < 10:
    #      sig = "00" + str(id) + sig()
    try:
         if sig.split(",")[0] == str(id):
              pass
         else :
              sig = id + "," + sig
              pirate.setSignal(sig)
    except:
        sig = id + "," + sig
        pirate.setSignal(sig)
    # id = id%40
    #  (sig)
    # if sig == "reached":
    if getIslandCenter(pirate):
             x_c , y_c,island_num = getIslandCenter(pirate)
             l = pirate.trackPlayers()
             s = pirate.getTeamSignal()
             t = s.split(",")
            #   (s)
            #   ((island_num-1)*2+1)
             if t[(island_num-1) * 2] == "" and t[(island_num-1) * 2 + 1] == "":
                    if(island_num == 1):
                        st = str(x_c) + "," + str(y_c) + "," + t[2] + "," + t[3] + "," + t[4] + "," + t[5] 
                        for i in range(6, len(t)):
                             st += "," + t[i]
                        pirate.setTeamSignal(st)
                    elif island_num == 2:
                        st = t[0] + "," + t[1] + "," + str(x_c) + "," + str(y_c) + "," + t[4] + "," + t[5]
                        for i in range(6, len(t)):
                             st += "," + t[i]
                        pirate.setTeamSignal(st)
                    elif island_num == 3:
                         st = t[0] + "," + t[1] + "," + t[2] + "," + t[3] + "," + str(x_c) + "," + str(y_c)
                         for i in range(6, len(t)):
                             st += "," + t[i]
                         pirate.setTeamSignal(st)
    if pirate.getCurrentFrame()>200:
        #Check for farman
        possible_farmans = pirate.getTeamSignal().split(',')
        for i in range(len(possible_farmans)):
             farman = possible_farmans[i]
             if f'i:{id}' in farman:
                  island_to_guard = farman.split(':')[-1]
                #    ("farman aaya hai to " + farman)

                  pirate.setSignal(pirate.getSignal().split(',')[0] + ',' + 'guarding' + island_to_guard)
                #    (pirate.getTeamSignal())
                #    (island_to_guard)
                  x_island = int(pirate.getTeamSignal().split(',')[2*(int(island_to_guard) - 1)])
                  y_island = int(pirate.getTeamSignal().split(',')[2*int(island_to_guard) -1])

                  team_sig_to_set = ''
                  for j in range(len(possible_farmans)):
                       if j != i:
                            team_sig_to_set += possible_farmans[j] + ','
                #    ("team_sig_to_set",team_sig_to_set)

                  pirate.setTeamSignal(team_sig_to_set[:-1])
                #   return moveTo(x_island,y_island,pirate) 
        
        
        l = pirate.trackPlayers()
        #  (pirate.getSignal())
        if 'guarding' in pirate.getSignal():
            #   ("entered guarding if")
             split_signal = pirate.getSignal().split(",")
             for ele in split_signal:
                  if 'guarding' in ele:
                    #     (ele)
                    #     (pirate.getTeamSignal())
                       island_to_guard = ele[-1]
                       x_island = int(pirate.getTeamSignal().split(',')[2*(int(island_to_guard) - 1)])
                       y_island = int(pirate.getTeamSignal().split(',')[2*(int(island_to_guard)) - 1])
                    #     ('guarding at',x_island," ",y_island)
                       return moveTo(x_island,y_island,pirate)
                       

        #  (l)
        if 'spreading' in pirate.getSignal()  and pirate.getTotalGunpowder() < 200:
            #  pirate.setSignal(pirate.getSignal() + ',spreading')
             return gundpowder_spread(pirate)
        elif 'guarding' not in pirate.getSignal(): 
            #  print(pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0] + "," )
             pirate.setSignal(pirate.getSignal().split(",")[0] + ",")
        
        if ('island1' in pirate.investigate_current()[0] and (l[0]!='myCapturing' or l[0]!='myCaptured')) or ('island2' in pirate.investigate_current()[0] and (l[1]!='myCapturing' or l[1]!='myCaptured')) or ('island3' in pirate.investigate_current()[0] and (l[2]!='myCapturing' or l[2]!='myCaptured')):
            #   ('Finding Reason why island is not getting captured')
            #   (f'Total Gunpowder= {pirate.getTotalGunpowder()}')
             if pirate.getTotalGunpowder() <= 150 and 'guarding' not in pirate.getSignal() and 'conquering' not in pirate.getSignal():
                  if int(pirate.getID())%2 == 0:
                    #     ('Due to GUnpowder')
                    #     (pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0] + "," )
                    #    pirate.setSignal(pirate.getSignal().split(",")[0] + "," + 'spreading')
                       return gundpowder_spread(pirate)

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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                # return moveTo(x+movex,y+movey,pirate)
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                # return moveTo(x+movex,y+movey,pirate)
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                # return moveTo(x+movex,y+movey,pirate)
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
                nearest_island_index = nearest_island(pirate)-1
                setconquering(pirate,nearest_island_index+1)
                
                if((id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()>2000) or  (l[nearest_island_index+3]=='oppCapturing' or l[nearest_island_index+3]=='oppCaptured') :
                     movex, movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id-1)%25+1  in outerMappingList and pirate.getCurrentFrame()<2000:
                    movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif (id-1)%25+1 in innerMappingList:
                     movex,movey = coord_list[innerMappingList[(pirate.getCurrentFrame()+id)%8]-1]
                elif (id)%25 !=14:
                     movex, movey = coord_list[(id)%25]
                     movex,movey = coord_list[outerMappingList[(pirate.getCurrentFrame()+id)%16]-1]
                elif id%25==14:
                     movex, movey =(0,0)
                # return moveTo(x+movex,y+movey,pirate)
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
        # if checkenemies(pirate) and pirate.getTotalGunpowder()<100:
        #      return checkenemies(pirate)
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
            #  ('Reached here')
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
                counter = int(pirate.getSignal().split(",")[1])
            except:
                counter = 0
            #  (f'y_self = {y_self} x_self = {x_self} a+counter = {a + counter}')
            if id<8:
                if a_spawn == 0 and b_spawn == 0:
                 return circleAround(width//2,height//2,width//2-id, pirate, clockwise=False)
                elif a_spawn == 0 and b_spawn == height:
                 return circleAround(width//2,height//2,width//2-id, pirate, clockwise=True)
                elif a_spawn == width and b_spawn == height:
                 return circleAround(width//2,height//2,width//2-id, pirate, clockwise=False)
                else:
                 return circleAround(width//2,height//2,width//2-id, pirate, clockwise=True)
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
            #  ('Checking for route completion')
            #  (f'Counter = {counter}')
            if counter%2==0:
                #  ('Even')
                if id <8:
                    
                    return circleAround(width//2,height//2,width//2-id,pirate)
                    if y_self==a + counter and x_self == abs(width - a_spawn) and b_spawn == 0:
                        #  ('Fired')
                        counter +=1
                        pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                        return moveTo(abs(width-a_spawn)+1,a+counter+1,pirate)
                    if y_self==height -a + counter and x_self ==abs(width - a_spawn) and b_spawn == height:
                        #  ('Fired')
                        # y_init = 39 - 1 - 0 + 1 = 39
                        #y_final = 39 - 1 -1 +1
                        counter -=1
                        pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                        #  (f'Move To: {moveTo(abs(width-a_spawn)+1,height - a-counter+1,pirate)}')
                        return moveTo(abs(width-a_spawn)+1,height - a+counter-1,pirate)
                else:
                    if y_self == a and x_self == abs(width-a_spawn) and b_spawn == 0 :
                         counter+=1
                        #   (pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0]+","+str(counter) )
                         pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                         return moveTo(abs(width-a_spawn)+1,a,pirate)
                    elif y_self == height - a and x_self == abs(width - a_spawn) and b_spawn == height:
                         counter+=1
                        #   (pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0]+","+str(counter) )
                         pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                         return moveTo(abs(width-a_spawn)+1,a,pirate)
                         
            else:
                #  ('Odd')
                if id<8:
                    return circleAround(width//2,height//2,width//2-id,pirate)
                    if y_self==a + counter and x_self ==a_spawn and b_spawn == 0:
                        #  ('Fired')
                        counter +=1
                        pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                        return moveTo(a_spawn-1,a+counter+1,pirate)
                    
                    if y_self==height -a + counter  and x_self ==a_spawn and b_spawn == height:
                        #  ('Fired')
                        #y_init = 39 - 1 -1
                        #y_final = 39 - 1 -2
                        counter -=1
                        pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                        return moveTo(a_spawn-1,height - a+counter-1,pirate)
                else:
                    if y_self == a and x_self == a_spawn and b_spawn == 0:
                         counter+=1
                        #   (pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0]+","+str(counter) )
                         pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                         return moveTo((a_spawn)-1,a,pirate)
                    elif y_self == height - a and x_self == a_spawn and b_spawn == height:
                         counter +=1
                        #   (pirate.getSignal(),"- signal changed to -",pirate.getSignal().split(",")[0]+","+str(counter) )
                         pirate.setSignal(pirate.getSignal().split(",")[0]+","+str(counter))
                         return moveTo((a_spawn)-1,a,pirate)

                           




def ActTeam(team):

    if team.getCurrentFrame() == 1:
         team.setTeamSignal(',,,,,')
    l = team.trackPlayers()
    s = team.getTeamSignal()
    s1 = s.split(',')
    li = team.getListOfSignals()
    #Guarding status should have 12 elements , corresponding to the id's protecting the island
    guarding_status =[[],[],[]]    
    for ele in li:
         try:
            pirate_id = int(ele.split(',')[0])
            if 'guarding' in ele:
                guarding_status[int(ele.split(',')[1][-1])-1].append(pirate_id)
         except:
              pass
    for i in range(len(guarding_status)):
         island_list = guarding_status[i]
         if len(island_list) < 4 and l[i]=='myCaptured':
              #Send some guards to guard the island
              for ele in li:
                   if 'guarding' not in ele and 'spreading' not in ele:
                        #Posted to guard the island farman bhejo

                        pirate_id = int(ele.split(',')[0])
                        if(pirate_id not in guarding_status[0] and pirate_id not in guarding_status[1] and pirate_id not in guarding_status[2]):
                            team.setTeamSignal(team.getTeamSignal() + ',' + f'i:{pirate_id} l:{i + 1}')
                            island_list.append(pirate_id)
                            if(len(island_list)==4):
                                break
                        #  (team.getTeamSignal())
    #  (team.getTeamSignal())
    #  (guarding_status)
    if team.getCurrentFrame()>200:

        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)
    
    #  (team.getCurrentFrame())
    # if s:

    #     # island_no = int(s1[0])
    #     #  (island_no)
    #     try:
    #         signal = l[island_no - 1]
    #         if signal == "myCaptured":
    #             # team.setTeamSignal("")
    #              pass
    #     except:
            #  pass