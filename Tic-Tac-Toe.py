import pyautogui 
import pygame
import sys
import time
pygame.init()

Line1 = 195
Line2 = 405
Line3 = 195
Line4 = 405 

SCREEN = pygame.display.set_mode((600,600))
SCREEN.fill((250,250,250))

color = {'X':(0,230,230),'O':(0,230,0),'GRID':(0,0,0)}
FLAG = {}
for i in range(1,10):
    FLAG[i]=0

X = []
O = []

xMOVE = True
oMove = False

def drawGrid():
    pygame.draw.line(SCREEN,color["GRID"],(195,0),(195,600),10)
    pygame.draw.line(SCREEN,color["GRID"],(395,0),(395,600),10)
    pygame.draw.line(SCREEN,color["GRID"],(0,195),(600,195),10)
    pygame.draw.line(SCREEN,color["GRID"],(0,395),(600,395),10)

def draw_X():
    
    for i in X:

        if i == 1:
            pygame.draw.rect(SCREEN,color['X'],[70,70,50,50])
        if i == 2:
            pygame.draw.rect(SCREEN,color['X'],[270,70,50,50])
        if i == 3:
            pygame.draw.rect(SCREEN,color['X'],[470,70,50,50])

        if i == 4:
            pygame.draw.rect(SCREEN,color['X'],[70,270,50,50])
        if i == 5:
            pygame.draw.rect(SCREEN,color['X'],[270,270,50,50])
        if i == 6:
            pygame.draw.rect(SCREEN,color['X'],[470,270,50,50])

        if i == 7:
            pygame.draw.rect(SCREEN,color['X'],[70,470,50,50])
        if i == 8:
            pygame.draw.rect(SCREEN,color['X'],[270,470,50,50])
        if i == 9:
            pygame.draw.rect(SCREEN,color['X'],[470,470,50,50])

def draw_O():
    for i in O:

        if i == 1:
            pygame.draw.rect(SCREEN,color['O'],[70,70,50,50])
        if i == 2:
            pygame.draw.rect(SCREEN,color['O'],[270,70,50,50])
        if i == 3:
            pygame.draw.rect(SCREEN,color['O'],[470,70,50,50])

        if i == 4:
            pygame.draw.rect(SCREEN,color['O'],[70,270,50,50])
        if i == 5:
            pygame.draw.rect(SCREEN,color['O'],[270,270,50,50])
        if i == 6:
            pygame.draw.rect(SCREEN,color['O'],[470,270,50,50])

        if i == 7:
            pygame.draw.rect(SCREEN,color['O'],[70,470,50,50])
        if i == 8:
            pygame.draw.rect(SCREEN,color['O'],[270,470,50,50])
        if i == 9:
            pygame.draw.rect(SCREEN,color['O'],[470,470,50,50])

def isWinner():

    if all( i in X for i in [1,2,3]):
        return "X Wins"

    elif all( i in X for i in [1,5,9]):
        return "X Wins"

    elif all( i in X for i in [1,4,7]):
        return "X Wins"

    elif all( i in X for i in [2,5,8]):
        return "X Wins"

    elif all( i in X for i in [3,5,7]):
        return "X Wins"

    elif all( i in X for i in [3,6,9]):
        return "X Wins"

    elif all( i in X for i in [4,5,6]):
        return "X Wins"

    elif all( i in X for i in [7,8,9]):
        return "X Wins"
#################################
    elif all( i in O for i in [1,2,3]):
        return "O Wins"

    elif all( i in O for i in [1,5,9]):
        return "O Wins"

    elif all( i in O for i in [1,4,7]):
        return "O Wins"

    elif all( i in O for i in [2,5,8]):
        return "O Wins"

    elif all( i in O for i in [3,5,7]):
        return "O Wins"

    elif all( i in O for i in [3,6,9]):
        return "O Wins"

    elif all( i in O for i in [4,5,6]):
        return "O Wins"

    elif all( i in O for i in [7,8,9]):
        return "O Wins"
    else:
        return "None"

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y =pygame.mouse.get_pos()

                if x < Line1 and y < Line3 and FLAG[1] == 0 :
                    if xMOVE:
                        X.append(1)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(1)
                        xMOVE = True
                        oMove = False
                    FLAG[1] = 1

                if x < Line2 and x > Line1 and y < Line3 and FLAG[2] == 0 :
                    if xMOVE:
                        X.append(2)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(2)
                        xMOVE = True
                        oMove = False
                    FLAG[2] = 1

                if  x > Line2 and y < Line3 and FLAG[3] == 0 :
                    if xMOVE:
                        X.append(3)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(3)
                        xMOVE = True
                        oMove = False
                    FLAG[3] = 1

                if x < Line1 and y < Line4 and y > Line3 and FLAG[4] == 0 :
                    if xMOVE:
                        X.append(4)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(4)
                        xMOVE = True
                        oMove = False
                    FLAG[4] = 1

                if x < Line2 and x > Line1 and y < Line4 and y> Line3 and FLAG[5] == 0 :
                    if xMOVE:
                        X.append(5)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(5)
                        xMOVE = True
                        oMove = False
                    FLAG[5] = 1

                if x > Line2 and y < Line4 and y > Line3 and FLAG[6] == 0 :
                    if xMOVE:
                        X.append(6)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(6)
                        xMOVE = True
                        oMove = False
                    FLAG[6] = 1

                if x < Line1 and y > Line4 and FLAG[7] == 0 :
                    if xMOVE:
                        X.append(7)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(7)
                        xMOVE = True
                        oMove = False
                    FLAG[7] = 1

                if x < Line2 and x > Line1 and y > Line4 and FLAG[8] == 0 :
                    if xMOVE:
                        X.append(8)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(8)
                        xMOVE = True
                        oMove = False
                    FLAG[8] = 1

                if x > Line2 and y > Line4 and FLAG[9] == 0 :
                    if xMOVE:
                        X.append(9)
                        xMOVE = False
                        oMove = True
                    else:
                        O.append(9)
                        xMOVE = True
                        oMove = False
                    FLAG[9] = 1

    drawGrid()
    draw_X()
    draw_O()
    
    Winner = isWinner()

    if Winner == "X Wins" or Winner == "O Wins":
        print(Winner)
        pygame.display.update()
        time.sleep(1)
        sys.exit()
    

    pygame.display.update()