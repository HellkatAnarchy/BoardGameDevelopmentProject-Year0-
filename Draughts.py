import tkinter as tk
import os

def ExitButtonCommand():
    TkGui.destroy()
    os.system("MainMenu.py")

#Variable Initialisation
PlayerTurn = 2
TurnState = 1

#Setting up of the window
TkGui = tk.Tk()
TkGui.attributes("-fullscreen", True)

#Get Screen resolution
ScreenWidth = TkGui.winfo_screenwidth()
ScreenHeight = TkGui.winfo_screenheight()
FullscreenResolution = (str(int(ScreenWidth)) + "x" + str(int(ScreenHeight)) + "+0+0")
TkGui.geometry(FullscreenResolution)
TkGui.title('Draughts')
TkGui.configure(background='#e1f5fe')

#Shapes
TheCanvas = tk.Canvas(TkGui, width=1920, height=100, background = "#e1f5fe")
TheCanvas.pack()
TheCanvas.create_rectangle(0, 0, 1920, 100, fill="#03a9f4")

#Text
tk.Label(TkGui, text = "Draughts", font = ('Myriad Pro',50), background = "#03a9f4", fg="#ffffff").place(x=20, y=10) 

#Buttons
tk.Button(TkGui, relief="flat", height = 1, width = 5, text = "X", font = ('Myriad Pro',30), foreground = "#ffffff", activeforeground="#ffffff", activebackground="#03a9f4", background = "#03a9f4", command = ExitButtonCommand).place(x=1830,y=5)
    
PyGUI = tk.Frame(TkGui, width=800, height=766)
PyGUI.pack()

# Tell pygame's SDL window which window ID to use
# Taken from http://stackoverflow.com/questions/8584272/using-pygame-features-in-tkinter
os.environ['SDL_WINDOWID'] = str(PyGUI.winfo_id())

# Show the window so it's assigned an ID.
TkGui.update()

# Usual pygame initialization
import pygame as pg
pg.init()
screen = pg.display.set_mode((800,766))

#Variable design for peice placement
#Go for Coordinates in a list, where there's one for each piece, then have that twice (For each player)
#Start at top left and bottom left
#Top is black, Bottom is white
PiecePositions = [[[1,0],[3,0],[5,0],[7,0],[0,1],[2,1],[4,1],[6,1],[1,2],[3,2],[5,2],[7,2]],[[0,7],[2,7],[4,7],[6,7],[1,6],[3,6],[5,6],[7,6],[0,5],[2,5],[4,5],[6,5]]]
KingStatus = [[False,False,False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False,False,False]]

#Image load
Board = pg.image.load("Images/ChessDraughtsBoard.png")
WhitePiece = pg.image.load("Images/DraughtsCounterWhite.png")
WhitePieceKinged = pg.image.load("Images/DraughtsCounterWhiteKinged.png")
BlackPiece = pg.image.load("Images/DraughtsCounterBlack.png")
BlackPieceKinged = pg.image.load("Images/DraughtsCounterBlackKinged.png")

while True:
    pg.display.flip()
    TkGui.update()

    #Board display
    screen.blit(Board,(0,0))

    #Piece display
    Count = 0
    for Count in range(0,12):
        if KingStatus[1][Count] == True:
            screen.blit(WhitePieceKinged,(((((PiecePositions[1][Count][0]) + 1)*100)-100),(((((PiecePositions[1][Count][1]) + 1)*100)-100))))
        else:
            screen.blit(WhitePiece,((((((PiecePositions[1][Count][0]) + 1)*100)-100),(((((PiecePositions[1][Count][1]) + 1)*100)-100)))))
    Count = 0
    for Count in range(0,12):
        if KingStatus[0][Count] == True:
            screen.blit(BlackPieceKinged,((((((PiecePositions[0][Count][0]) + 1)*100)-100),(((((PiecePositions[0][Count][1]) + 1)*100)-100)))))
        else:
            screen.blit(BlackPiece,((((((PiecePositions[0][Count][0]) + 1)*100)-100),(((((PiecePositions[0][Count][1]) + 1)*100)-100)))))
            
    #PlayerTurn text
    if PlayerTurn == 1:
        tk.Label(TkGui, text = "Player Ones Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900)
    elif PlayerTurn == 2:
        tk.Label(TkGui, text = "Player Twos Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900)

    if TurnState == 1: #Input phase 
        #Get where the user has clicked
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONDOWN:
            if PlayerTurn == 1:
                try:
                    SelectedPieceCoordinates = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                    SelectedPieceIndex = PiecePositions[0].index([int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)])
                    TurnState = 2
                except ValueError:
                    pass
            if PlayerTurn == 2:
                try:
                    SelectedPieceCoordinates = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                    SelectedPieceIndex = PiecePositions[1].index([int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)])
                    TurnState = 2
                except ValueError:
                    pass
                
    elif TurnState == 2: #Movement Phase
        #Movement conditions for a man: One diagonal movement if not obstructed. Two diagonally if there's one obstructing but nothing behind it.
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONDOWN:
            if KingStatus[PlayerTurn - 1][SelectedPieceIndex] == False: #If not king
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],SelectedPieceCoordinates[1]]: #Click selected piece again to pick another piece
                    TurnState = 1
                    continue
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in PiecePositions[0] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in PiecePositions[1]: #If trying to move onto another piece
                    continue
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)] and PlayerTurn == 1:
                    PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)] and PlayerTurn == 1:
                    PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)] and PlayerTurn == 2:
                    PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 1)] and PlayerTurn == 2:
                    PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 2)] and PlayerTurn == 2:#This and below are for jumping the pieces
                    if [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 2)] and PlayerTurn == 2:
                    if [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 2)] and PlayerTurn == 1:
                    if [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 2)] and PlayerTurn == 1:
                    if [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)])] = [8,8]
                    else:
                        continue
                else:
                    continue
                if PlayerTurn == 1 and PiecePositions[PlayerTurn - 1][SelectedPieceIndex][1] == 7: #Promotion
                    KingStatus[PlayerTurn - 1][SelectedPieceIndex] = True
                if PlayerTurn == 2 and PiecePositions[PlayerTurn - 1][SelectedPieceIndex][1] == 0: #Promotion
                    KingStatus[PlayerTurn - 1][SelectedPieceIndex] = True
            else: #If king
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],SelectedPieceCoordinates[1]]: #Click selected piece again to pick another piece
                    TurnState = 1
                    continue
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in PiecePositions[0] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in PiecePositions[1]: #If trying to move onto another piece
                    continue
                if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)]:
                    PiecePositions[PlayerTurn][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)]:
                    PiecePositions[PlayerTurn][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)]:
                    PiecePositions[PlayerTurn][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 1)]:
                    PiecePositions[PlayerTurn][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 2)]:#This and below are for jumping the pieces
                    if [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[0] - 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 2)]:
                    if [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 2)]:
                    if [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 1)])] = [8,8]
                    else:
                        continue
                elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 2)]:
                    if [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)] in PiecePositions[PlayerTurn % 2]:
                        PiecePositions[PlayerTurn - 1][SelectedPieceIndex] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        PiecePositions[PlayerTurn % 2][PiecePositions[PlayerTurn % 2].index([(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 1)])] = [8,8]
                    else:
                        continue
                else:
                    continue
            pg.display.flip()
            TkGui.update()
            TurnState = 3
            
    elif TurnState == 3: #Check and playerswap phase
        #Check
        if PiecePositions[0] == [[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8]]:
            tk.messagebox.showinfo("Winner!","White wins.")
            TkGui.destroy()
            os.system("MainMenu.py")
        if PiecePositions[1] == [[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8],[8,8]]:
            tk.messagebox.showinfo("Winner!","Black wins.")
            TkGui.destroy()
            os.system("MainMenu.py")
        #PlayerSwap
        if PlayerTurn == 1:
            PlayerTurn = 2
        elif PlayerTurn == 2:
            PlayerTurn = 1
        TurnState = 1

    pg.display.flip()
    TkGui.update()
        
print("IM OUT OF THE WHILE TRUE")




