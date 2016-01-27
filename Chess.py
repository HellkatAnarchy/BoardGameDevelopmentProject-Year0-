import tkinter as tk
import os

def ExitButtonCommand():
    TkGui.destroy()
    os.system("MainMenu.py")

#Variable Initialisation
PlayerTurn = 1
TurnState = 1

#Setting up of the window
TkGui = tk.Tk()
TkGui.attributes("-fullscreen", True)

#Get Screen resolution
ScreenWidth = TkGui.winfo_screenwidth()
ScreenHeight = TkGui.winfo_screenheight()
FullscreenResolution = (str(int(ScreenWidth)) + "x" + str(int(ScreenHeight)) + "+0+0")
TkGui.geometry(FullscreenResolution)
TkGui.title('Chess')
TkGui.configure(background='#e1f5fe')

#Shapes
TheCanvas = tk.Canvas(TkGui, width=1920, height=100, background = "#e1f5fe")
TheCanvas.pack()
TheCanvas.create_rectangle(0, 0, 1920, 100, fill="#03a9f4")

#Text
tk.Label(TkGui, text = "Chess", font = ('Myriad Pro',50), background = "#03a9f4", fg="#ffffff").place(x=20, y=10) 

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
#[Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Castle,Horse,Bishop,Queen,King,Bishop,Horse,Castle]  where each one includes a coordniate starting from bottom left
#Defaulted below
#Note for finding which peice a user clicks later [1,2,3].index(2) # => 1 (Get clicked position, search in list)
#White is player 1, black is 2

WhitePiecePositions = [[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
BlackPiecePositions = [[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7]]

CheckMateSpaces = [[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False]]

#Image load
WhitePawn = pg.image.load("Images/ChessWhitePawn.png")
WhiteBishop = pg.image.load("Images/ChessWhiteBishop.png")
WhiteCastle = pg.image.load("Images/ChessWhiteCastle.png")
WhiteHorse = pg.image.load("Images/ChessWhiteHorse.png")
WhiteKing = pg.image.load("Images/ChessWhiteKing.png")
WhiteQueen = pg.image.load("Images/ChessWhiteQueen.png")
BlackPawn = pg.image.load("Images/ChessBlackPawn.png")
BlackBishop = pg.image.load("Images/ChessBlackBishop.png")
BlackCastle = pg.image.load("Images/ChessBlackCastle.png")
BlackHorse = pg.image.load("Images/ChessBlackHorse.png")
BlackKing = pg.image.load("Images/ChessBlackKing.png")
BlackQueen = pg.image.load("Images/ChessBlackQueen.png")
Board = pg.image.load("Images/ChessDraughtsBoard.png")


while True:
    pg.display.flip()
    TkGui.update()

    #Board display
    screen.blit(Board,(0,0))

    #Piece display
    screen.blit(WhitePawn,((((WhitePiecePositions[0][0]+1)*100)-100),(((WhitePiecePositions[0][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[1][0]+1)*100)-100),(((WhitePiecePositions[1][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[2][0]+1)*100)-100),(((WhitePiecePositions[2][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[3][0]+1)*100)-100),(((WhitePiecePositions[3][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[4][0]+1)*100)-100),(((WhitePiecePositions[4][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[5][0]+1)*100)-100),(((WhitePiecePositions[5][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[6][0]+1)*100)-100),(((WhitePiecePositions[6][1]+1)*100)-100)))
    screen.blit(WhitePawn,((((WhitePiecePositions[7][0]+1)*100)-100),(((WhitePiecePositions[7][1]+1)*100)-100)))
    screen.blit(WhiteCastle,((((WhitePiecePositions[8][0]+1)*100)-100),(((WhitePiecePositions[8][1]+1)*100)-100)))
    screen.blit(WhiteHorse,((((WhitePiecePositions[9][0]+1)*100)-100),(((WhitePiecePositions[9][1]+1)*100)-100)))
    screen.blit(WhiteBishop,((((WhitePiecePositions[10][0]+1)*100)-100),(((WhitePiecePositions[10][1]+1)*100)-100)))
    screen.blit(WhiteQueen,((((WhitePiecePositions[11][0]+1)*100)-100),(((WhitePiecePositions[11][1]+1)*100)-100)))
    screen.blit(WhiteKing,((((WhitePiecePositions[12][0]+1)*100)-100),(((WhitePiecePositions[12][1]+1)*100)-100)))
    screen.blit(WhiteBishop,((((WhitePiecePositions[13][0]+1)*100)-100),(((WhitePiecePositions[13][1]+1)*100)-100)))
    screen.blit(WhiteHorse,((((WhitePiecePositions[14][0]+1)*100)-100),(((WhitePiecePositions[14][1]+1)*100)-100)))
    screen.blit(WhiteCastle,((((WhitePiecePositions[15][0]+1)*100)-100),(((WhitePiecePositions[15][1]+1)*100)-100)))

    screen.blit(BlackPawn,((((BlackPiecePositions[0][0]+1)*100)-100),(((BlackPiecePositions[0][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[1][0]+1)*100)-100),(((BlackPiecePositions[1][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[2][0]+1)*100)-100),(((BlackPiecePositions[2][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[3][0]+1)*100)-100),(((BlackPiecePositions[3][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[4][0]+1)*100)-100),(((BlackPiecePositions[4][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[5][0]+1)*100)-100),(((BlackPiecePositions[5][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[6][0]+1)*100)-100),(((BlackPiecePositions[6][1]+1)*100)-120)))
    screen.blit(BlackPawn,((((BlackPiecePositions[7][0]+1)*100)-100),(((BlackPiecePositions[7][1]+1)*100)-120)))
    screen.blit(BlackCastle,((((BlackPiecePositions[8][0]+1)*100)-100),(((BlackPiecePositions[8][1]+1)*100)-120)))
    screen.blit(BlackHorse,((((BlackPiecePositions[9][0]+1)*100)-100),(((BlackPiecePositions[9][1]+1)*100)-120)))
    screen.blit(BlackBishop,((((BlackPiecePositions[10][0]+1)*100)-100),(((BlackPiecePositions[10][1]+1)*100)-120)))
    screen.blit(BlackQueen,((((BlackPiecePositions[11][0]+1)*100)-100),(((BlackPiecePositions[11][1]+1)*100)-120)))
    screen.blit(BlackKing,((((BlackPiecePositions[12][0]+1)*100)-100),(((BlackPiecePositions[12][1]+1)*100)-120)))
    screen.blit(BlackBishop,((((BlackPiecePositions[13][0]+1)*100)-100),(((BlackPiecePositions[13][1]+1)*100)-120)))
    screen.blit(BlackHorse,((((BlackPiecePositions[14][0]+1)*100)-100),(((BlackPiecePositions[14][1]+1)*100)-120)))
    screen.blit(BlackCastle,((((BlackPiecePositions[15][0]+1)*100)-100),(((BlackPiecePositions[15][1]+1)*100)-120)))
        
    if PlayerTurn == 1:
        tk.Label(TkGui, text = "Player Ones Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900)
    elif PlayerTurn == 2:
        tk.Label(TkGui, text = "Player Twos Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900)
    if TurnState == 1:
        #Get where the user has clicked
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONDOWN:
            if PlayerTurn == 1:
                try:
                    SelectedPieceCoordinates = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                    SelectedPieceLocation = BlackPiecePositions.index([int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)])
                    TurnState = 2
                except ValueError:
                    pass
            if PlayerTurn == 2:
                try:
                    SelectedPieceCoordinates = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                    SelectedPieceLocation = WhitePiecePositions.index([int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)])
                    TurnState = 2
                except ValueError:
                    pass
    elif TurnState == 2:
        i = 0
        i2 = 0
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONDOWN:
            #Now we need to handle moving of pieces
            #First find what kind of piece it is. 0..7 is Pawn, 8 and 15 are castle, 9 and 14 horse, 10 and 13 bishop, 11 queen, 12 king.
            if 0 <= SelectedPieceLocation <= 7: #PAWN - WORKS
                if PlayerTurn == 1:
                    if SelectedPieceCoordinates[1] == 6: #If on the start spaces
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                            TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                            continue
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                            continue
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] + 1,(SelectedPieceCoordinates[1]-1)] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] - 1,(SelectedPieceCoordinates[1]-1)]:
                            if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                                BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]-2)]: #Moving 2
                            if ((SelectedPieceCoordinates[1])-1) in BlackPiecePositions or ((SelectedPieceCoordinates[1])-1) in WhitePiecePositions:
                                continue
                            else:
                                BlackPiecePositions[SelectedPieceLocation] = [BlackPiecePositions[SelectedPieceLocation][0],(BlackPiecePositions[SelectedPieceLocation][1]-2)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]-1)]: #Moving 1
                                BlackPiecePositions[SelectedPieceLocation] = [BlackPiecePositions[SelectedPieceLocation][0],(BlackPiecePositions[SelectedPieceLocation][1]-1)]
                                TurnState = 3
                        else:
                            continue
                    else:
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                            TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                            continue
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                            continue
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] + 1,(SelectedPieceCoordinates[1]-1)] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] - 1,(SelectedPieceCoordinates[1]-1)]:
                            if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                                BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]-1)]: #Moving 1 only because not on start space
                            BlackPiecePositions[SelectedPieceLocation] = [BlackPiecePositions[SelectedPieceLocation][0],(BlackPiecePositions[SelectedPieceLocation][1]-1)]
                            TurnState = 3
                        else:
                            continue
                    if BlackPiecePositions[SelectedPieceLocation][1] == 0: #Pawn promotion
                        if BlackPiecePositions[11] == [8,8]:
                            BlackPiecePositions[11] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[10] == [8,8]:
                            BlackPiecePositions[10] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[13] == [8,8]:
                            BlackPiecePositions[13] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[9] == [8,8]:
                            BlackPiecePositions[9] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[14] == [8,8]:
                            BlackPiecePositions[14] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[8] == [8,8]:
                            BlackPiecePositions[8] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]
                        elif BlackPiecePositions[15] == [8,8]:
                            BlackPiecePositions[15] = BlackPiecePositions[SelectedPieceLocation]
                            BlackPiecePositions[SelectedPieceLocation] = [8,8]                          
                if PlayerTurn == 2:
                    if SelectedPieceCoordinates[1] == 1: #If on the start spaces
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                            TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[12]:
                            continue
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                            continue
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] + 1,(SelectedPieceCoordinates[1] + 1)] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] - 1,(SelectedPieceCoordinates[1] + 1)]:
                            if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                                WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]+2)]: #Moving 2
                            if ((SelectedPieceCoordinates[1]) + 2) in BlackPiecePositions or ((SelectedPieceCoordinates[1]) + 2) in WhitePiecePositions:
                                continue
                            else:
                                WhitePiecePositions[SelectedPieceLocation] = [WhitePiecePositions[SelectedPieceLocation][0],(WhitePiecePositions[SelectedPieceLocation][1]+2)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]+1)]: #Moving 1
                            WhitePiecePositions[SelectedPieceLocation] = [WhitePiecePositions[SelectedPieceLocation][0],(WhitePiecePositions[SelectedPieceLocation][1]+1)]
                            TurnState = 3
                        else:
                            continue
                    else:
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                            TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                            continue
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                            continue
                        if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] + 1,(SelectedPieceCoordinates[1] + 1)] or [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0] - 1,(SelectedPieceCoordinates[1] + 1)]:
                            if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                                WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                                TurnState = 3
                        elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [SelectedPieceCoordinates[0],(SelectedPieceCoordinates[1]+1)]: #Moving 1 because not on start space
                            WhitePiecePositions[SelectedPieceLocation] = [WhitePiecePositions[SelectedPieceLocation][0],(WhitePiecePositions[SelectedPieceLocation][1]+1)]
                            TurnState = 3
                        else:
                            continue
                    if WhitePiecePositions[SelectedPieceLocation][1] == 0: #Pawn promotion
                        if WhitePiecePositions[11] == [8,8]:
                            WhitePiecePositions[11] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[10] == [8,8]:
                            WhitePiecePositions[10] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[13] == [8,8]:
                            WhitePiecePositions[13] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[9] == [8,8]:
                            WhitePiecePositions[9] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[14] == [8,8]:
                            WhitePiecePositions[14] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[8] == [8,8]:
                            WhitePiecePositions[8] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]
                        elif WhitePiecePositions[15] == [8,8]:
                            WhitePiecePositions[15] = WhitePiecePositions[SelectedPieceLocation]
                            WhitePiecePositions[SelectedPieceLocation] = [8,8]  
            elif SelectedPieceLocation == 8 or SelectedPieceLocation == 15:
                print("CASTLE")
                if PlayerTurn == 1:
                    if (int(pg.mouse.get_pos()[0]/100)) != BlackPiecePositions[SelectedPieceLocation][0] and (int(pg.mouse.get_pos()[1]/100)) != BlackPiecePositions[SelectedPieceLocation][1]:#If X and Y are different
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:#If moving onto a teammates
                        continue
                    if int(pg.mouse.get_pos()[0]/100) > BlackPiecePositions[SelectedPieceLocation][0]: #If moving right
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][0] + i) < int(pg.mouse.get_pos()[0]/100):
                            if [BlackPiecePositions[SelectedPieceLocation][0] + i,BlackPiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0] + i,BlackPiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[0]/100) < BlackPiecePositions[SelectedPieceLocation][0]: #If moving left
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][0] - i) > int(pg.mouse.get_pos()[0]/100):
                            if [BlackPiecePositions[SelectedPieceLocation][0] - i,BlackPiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0] - i,BlackPiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) < BlackPiecePositions[SelectedPieceLocation][1]: #If moving up
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][1] - i) > int(pg.mouse.get_pos()[1]/100):
                            if [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] - i] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] - i] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) > BlackPiecePositions[SelectedPieceLocation][1]: #If moving down
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][1] + i) < int(pg.mouse.get_pos()[1]/100):
                            if [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] + i] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] + i] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                if PlayerTurn == 2:
                    if (int(pg.mouse.get_pos()[0]/100)) != WhitePiecePositions[SelectedPieceLocation][0] and (int(pg.mouse.get_pos()[1]/100)) != WhitePiecePositions[SelectedPieceLocation][1]:#If X and Y are different
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:#If moving onto a teammate
                        continue
                    if int(pg.mouse.get_pos()[0]/100) > WhitePiecePositions[SelectedPieceLocation][0]: #If moving right
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][0] + i) < pg.mouse.get_pos()[0]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0] + i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0] + i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[0]/100) < WhitePiecePositions[SelectedPieceLocation][0]: #If moving left
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][0] - i) > pg.mouse.get_pos()[0]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0] - i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0] - i,WhitePiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) < WhitePiecePositions[SelectedPieceLocation][1]: #If moving up
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][1] - i) > int(pg.mouse.get_pos()[1]/100):
                            if [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] - i] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] - i] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) > WhitePiecePositions[SelectedPieceLocation][1]: #If moving down
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][1] + i) < pg.mouse.get_pos()[1]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] + i] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] + i] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
            elif SelectedPieceLocation == 9 or SelectedPieceLocation == 14:
                print("HORSE")
                if PlayerTurn == 1:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 2)]: #Up right
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 1)]: #Right up
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 1)]: #Right down
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 2)]: #Down right
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 2)]: #Down left
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 1)]: #Left down
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 1)]: #Left up
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 2)]: #Up left
                        BlackPiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 2)]
                        TurnState = 3
                    else:
                        continue
                if PlayerTurn == 2:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] - 2)]: #Up right
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 1)]: #Right up
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] - 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 1)]: #Right down
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 2),(SelectedPieceCoordinates[1] + 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 2)]: #Down right
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] + 1),(SelectedPieceCoordinates[1] + 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 2)]: #Down left
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] + 2)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 1)]: #Left down
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] + 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 1)]: #Left up
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 2),(SelectedPieceCoordinates[1] - 1)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] ==  [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 2)]: #Up left
                        WhitePiecePositions[SelectedPieceLocation] = [(SelectedPieceCoordinates[0] - 1),(SelectedPieceCoordinates[1] - 2)]
                        TurnState = 3
                    else:
                        continue
            elif SelectedPieceLocation == 10 or SelectedPieceLocation == 13:
                if PlayerTurn == 1:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                        continue
                    elif abs(int(pg.mouse.get_pos()[0]/100) - BlackPiecePositions[SelectedPieceLocation][0]) == abs(int(pg.mouse.get_pos()[1]/100) - BlackPiecePositions[SelectedPieceLocation][1]):
                        if (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down right collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] + i),(BlackPiecePositions[SelectedPieceLocation][1] + i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down left collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] - i),(BlackPiecePositions[SelectedPieceLocation][1] + i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up left collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] - i),(BlackPiecePositions[SelectedPieceLocation][1] - i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up right collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] + i),(BlackPiecePositions[SelectedPieceLocation][1] - i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3                                          
                if PlayerTurn == 2:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                        continue
                    elif abs(int(pg.mouse.get_pos()[0]/100) - WhitePiecePositions[SelectedPieceLocation][0]) == abs(int(pg.mouse.get_pos()[1]/100) - WhitePiecePositions[SelectedPieceLocation][1]):
                        if (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down right collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] + i),(WhitePiecePositions[SelectedPieceLocation][1] + i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down left collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] - i),(WhitePiecePositions[SelectedPieceLocation][1] + i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up left collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] - i),(WhitePiecePositions[SelectedPieceLocation][1] - i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up right collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] + i),(WhitePiecePositions[SelectedPieceLocation][1] - i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3            
            elif SelectedPieceLocation == 11:
                print("QUEEN")
                if PlayerTurn == 1:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:#If moving onto a teammates
                        continue
                    elif (abs(int(pg.mouse.get_pos()[0]/100) - BlackPiecePositions[SelectedPieceLocation][0])) == (abs(int(pg.mouse.get_pos()[1]/100) - BlackPiecePositions[SelectedPieceLocation][1])):
                        print("DIAG")
                        if (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down right collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] + i),(BlackPiecePositions[SelectedPieceLocation][1] + i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down left collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] - i),(BlackPiecePositions[SelectedPieceLocation][1] + i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up left collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] - i),(BlackPiecePositions[SelectedPieceLocation][1] - i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        elif (BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (BlackPiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up right collision check
                            i = abs((BlackPiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(BlackPiecePositions[SelectedPieceLocation][0] + i),(BlackPiecePositions[SelectedPieceLocation][1] - i)] in BlackPiecePositions:
                                    i = "FAULT"
                                    break
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[0]/100) > BlackPiecePositions[SelectedPieceLocation][0]: #If moving right
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][0] +
                               i) < pg.mouse.get_pos()[0]/100:
                            if [BlackPiecePositions[SelectedPieceLocation][0] + i,BlackPiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0] + i,BlackPiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[0]/100) < BlackPiecePositions[SelectedPieceLocation][0]: #If moving left
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][0] - i) > pg.mouse.get_pos()[0]/100:
                            if [BlackPiecePositions[SelectedPieceLocation][0] - i,BlackPiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0] - i,BlackPiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) < BlackPiecePositions[SelectedPieceLocation][1]: #If moving up
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][1] - i) > int(pg.mouse.get_pos()[1]/100):
                            if [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] - i] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] - i] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) > BlackPiecePositions[SelectedPieceLocation][1]: #If moving down
                        #Find difference between
                        i = 1
                        while (BlackPiecePositions[SelectedPieceLocation][1] + i) < pg.mouse.get_pos()[1]/100:
                            if [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] + i] in BlackPiecePositions or [BlackPiecePositions[SelectedPieceLocation][0],BlackPiecePositions[SelectedPieceLocation][1] + i] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                if PlayerTurn == 2:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:#If moving onto a teammates
                        continue
                    if int(pg.mouse.get_pos()[0]/100) > WhitePiecePositions[SelectedPieceLocation][0]: #If moving right
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][0] + i) < pg.mouse.get_pos()[0]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0] + i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0] + i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[0]/100) < WhitePiecePositions[SelectedPieceLocation][0]: #If moving left
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][0] - i) > pg.mouse.get_pos()[0]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0] - i,WhitePiecePositions[SelectedPieceLocation][1]] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0] - i,WhitePiecePositions[SelectedPieceLocation][1]] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) < WhitePiecePositions[SelectedPieceLocation][1]: #If moving up
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][1] - i) > int(pg.mouse.get_pos()[1]/100):
                            if [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] - i] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] - i] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    elif int(pg.mouse.get_pos()[1]/100) > WhitePiecePositions[SelectedPieceLocation][1]: #If moving down
                        #Find difference between
                        i = 1
                        while (WhitePiecePositions[SelectedPieceLocation][1] + i) < pg.mouse.get_pos()[1]/100:
                            if [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] + i] in WhitePiecePositions or [WhitePiecePositions[SelectedPieceLocation][0],WhitePiecePositions[SelectedPieceLocation][1] + i] in BlackPiecePositions:
                                i = "FAULT"
                                break    
                            else:
                                i= i + 1
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:#If moving onto a teammates
                        continue
                    elif (abs(int(pg.mouse.get_pos()[0]/100) - WhitePiecePositions[SelectedPieceLocation][0])) == (abs(int(pg.mouse.get_pos()[1]/100) - WhitePiecePositions[SelectedPieceLocation][1])):
                        print("DIAG")
                        if (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down right collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] + i),(WhitePiecePositions[SelectedPieceLocation][1] + i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) < 0):
                            #Down left collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] - i),(WhitePiecePositions[SelectedPieceLocation][1] + i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) > 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up left collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] - i),(WhitePiecePositions[SelectedPieceLocation][1] - i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        elif (WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100) < 0 and (WhitePiecePositions[SelectedPieceLocation][1] - int(pg.mouse.get_pos()[1]/100)) > 0):
                            #Up right collision check
                            i = abs((WhitePiecePositions[SelectedPieceLocation][0] - int(pg.mouse.get_pos()[0]/100)))
                            for i in range(1,i):
                                if [(WhitePiecePositions[SelectedPieceLocation][0] + i),(WhitePiecePositions[SelectedPieceLocation][1] - i)] in WhitePiecePositions:
                                    i = "FAULT"
                                    break
                        if i != "FAULT":
                            WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                            TurnState = 3
            elif SelectedPieceLocation == 12:
                print("KING")
                if PlayerTurn == 1:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == BlackPiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in BlackPiecePositions:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][0] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][1] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][2] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1]] and CheckMateSpaces[PlayerTurn-1][3] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1]] and CheckMateSpaces[PlayerTurn-1][4] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][5] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][6] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][7] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0]),(BlackPiecePositions[SelectedPieceLocation][1] - 1)] and [(BlackPiecePositions[SelectedPieceLocation][0]),(BlackPiecePositions[SelectedPieceLocation][1] - 1)] not in BlackPiecePositions: #Up
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1] - 1)]  and [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1] - 1)] not in BlackPiecePositions: #Up-right 
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1])]  and [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1])] not in BlackPiecePositions: #Right
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1] + 1)]  and [(BlackPiecePositions[SelectedPieceLocation][0] + 1),(BlackPiecePositions[SelectedPieceLocation][1] + 1)] not in BlackPiecePositions: #Down-Right
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0]),(BlackPiecePositions[SelectedPieceLocation][1] +1)]  and [(BlackPiecePositions[SelectedPieceLocation][0]),(BlackPiecePositions[SelectedPieceLocation][1] + 1)] not in BlackPiecePositions: #Down
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1] + 1)]  and [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1] + 1)] not in BlackPiecePositions: #Down-left
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1])]  and [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1])] not in BlackPiecePositions: #Left
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1] - 1)]  and [(BlackPiecePositions[SelectedPieceLocation][0] - 1),(BlackPiecePositions[SelectedPieceLocation][1] + 1)] not in BlackPiecePositions: #Up-Left
                        BlackPiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    else:
                        continue
                if PlayerTurn == 2:
                    if [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[SelectedPieceLocation]: #This allows the user to click on the same space to pass
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == WhitePiecePositions[12]:
                            continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] in WhitePiecePositions:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][0] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][1] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] - 1] and CheckMateSpaces[PlayerTurn-1][2] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1]] and CheckMateSpaces[PlayerTurn-1][3] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1]] and CheckMateSpaces[PlayerTurn-1][4] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][5] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][6] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] + 1] and CheckMateSpaces[PlayerTurn-1][7] == True:
                        continue
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0]),(WhitePiecePositions[SelectedPieceLocation][1] - 1)] and [(WhitePiecePositions[SelectedPieceLocation][0]),(WhitePiecePositions[SelectedPieceLocation][1] - 1)] not in WhitePiecePositions: #Up
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1] - 1)]  and [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1] - 1)] not in WhitePiecePositions: #Up-right 
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1])]  and [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1])] not in WhitePiecePositions: #Right
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1] + 1)]  and [(WhitePiecePositions[SelectedPieceLocation][0] + 1),(WhitePiecePositions[SelectedPieceLocation][1] + 1)] not in WhitePiecePositions: #Down-Right
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0]),(WhitePiecePositions[SelectedPieceLocation][1] +1)]  and [(WhitePiecePositions[SelectedPieceLocation][0]),(WhitePiecePositions[SelectedPieceLocation][1] + 1)] not in WhitePiecePositions: #Down
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1] + 1)]  and [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1] + 1)] not in WhitePiecePositions: #Down-left
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1])]  and [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1])] not in WhitePiecePositions: #Left
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    elif [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)] == [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1] - 1)]  and [(WhitePiecePositions[SelectedPieceLocation][0] - 1),(WhitePiecePositions[SelectedPieceLocation][1] + 1)] not in WhitePiecePositions: #Up-Left
                        WhitePiecePositions[SelectedPieceLocation] = [int(pg.mouse.get_pos()[0]/100),int(pg.mouse.get_pos()[1]/100)]
                        TurnState = 3
                    else:
                        continue
            else:
                continue
            pg.display.flip()
            TkGui.update()
    elif TurnState == 3:
        #Taking of enemy pieces
        i = 0
        if PlayerTurn == 1:
            for i in range(0,16):
                if BlackPiecePositions[i] in WhitePiecePositions:
                    if BlackPiecePositions[i] == [8,8]: #If this part isn't there, then 1-There will be unnecesary processing and 2-Bugs will happen related to dead pieces taking other dead pieces
                        pass
                    else:
                        WhitePiecePositions[WhitePiecePositions.index(BlackPiecePositions[i])] = [8,8] #[8,8] will be where dead pieces lie due to Type
        i = 0
        if PlayerTurn == 2:
            for i in range(0,16):
                if WhitePiecePositions[i] in BlackPiecePositions:
                    if WhitePiecePositions[i] == [8,8]: #If this part isn't there, then 1-There will be unnecesary processing and 2-Bugs will happen related to dead pieces taking other dead pieces
                        pass
                    else:
                        BlackPiecePositions[BlackPiecePositions.index(WhitePiecePositions[i])] = [8,8]
        #Check
        #Check occurs if a piece can take the king.
        #To know if it can take it, we can check if any movements of any piece will land on the king.
        #Remember we also need to stop the king from being able to move onto peices where he would be checked. This can be done by modifying the code for checking for checks though.
        CheckMateSpaces = [[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False]] #We reinitialise so that if the king(s) have moved out of check then it does a fresh check instead of stacking ontop of the same one.
        if PlayerTurn == 1:
            i = 0
            for i in range(0,16):
                print(i)
                if i < 8: #Check checks for pawn
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == WhitePiecePositions[12]:
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == WhitePiecePositions[12]:
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][0] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][1] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][2] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] - 1]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1]]:
                        CheckMateSpaces[1][3] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1]]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1]]:
                        CheckMateSpaces[1][4] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1]]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] + 1]:
                        CheckMateSpaces[1][5] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] - 1,WhitePiecePositions[12][1] +1]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] + 1]:
                        CheckMateSpaces[1][6] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0],WhitePiecePositions[12][1] + 1]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] + 1]:
                        CheckMateSpaces[1][7] = True
                    elif [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 1)] == [WhitePiecePositions[12][0] + 1,WhitePiecePositions[12][1] + 1]:
                        CheckMateSpaces[1][7] = True
                if i == 8 or i == 15: #Check checks for castle
                    if BlackPiecePositions[i][0] < WhitePiecePositions[12][0] and BlackPiecePositions[i][1] == WhitePiecePositions[12][1]: #If to left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < WhitePiecePositions[12][0]:
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                            CheckMateSpaces[0][3] = True
                    elif BlackPiecePositions[i][0] > WhitePiecePositions[12][0] and BlackPiecePositions[i][1] == WhitePiecePositions[12][1]: #If to right
                        Count = 1
                        while (BlackPiecePositions[i][0] - Count) > WhitePiecePositions[12][0]:
                            if [BlackPiecePositions[i][0] - Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] - Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                            CheckMateSpaces[0][4] = True
                    elif BlackPiecePositions[i][1] > WhitePiecePositions[12][1] and BlackPiecePositions[i][0] == WhitePiecePositions[12][0]: #If below
                        Count = 1
                        while (BlackPiecePositions[i][1] - Count) > WhitePiecePositions[12]:
                            if [BlackPiecePositions[i][0],BlackPiecePositions[i][1] - Count] in BlackPiecePositions or [BlackPiecePositions[i][0],BlackPiecePositions[i][1] - Count] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                                CheckMateSpaces[0][6] = True
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                    elif BlackPiecePositions[i][1] < WhitePiecePositions[12][1] and BlackPiecePositions[i][0] == WhitePiecePositions[12][0]: #If above
                        Count = 1
                        while (BlackPiecePositions[i][1] + Count) < WhitePiecePositions[12]:
                            if [BlackPiecePositions[i][0],BlackPiecePositions[i][1] + Count] in BlackPiecePositions or [BlackPiecePositions[i][0],BlackPiecePositions[i][1] + Count] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                                CheckMateSpaces[0][1] = True
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][0] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0]) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up and to the right
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] + 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][2] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1]): #Check for to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][3] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1]): #Check for to the right
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] + 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][4] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][5] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0]) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][6] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][7] = True
                if i == 9 or i == 14: #Check checks for knight
                    if WhitePiecePositions[12] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]: #Right up
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]: #Right down
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]: #Down right
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] + 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]: #Down left
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] + 2)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]: #Left down
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] + 1)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]: #Left up
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 2),(BlackPiecePositions[i][1] - 1)]:
                        CheckMateSpaces[0][7] = True
                    if WhitePiecePositions[12] ==  [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]: #Up left
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[0][8] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] - 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1])] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[12][0] - 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[12][0]),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[12][0] + 1),(WhitePiecePositions[12][1] + 1)] == [(BlackPiecePositions[i][0] - 1),(BlackPiecePositions[i][1] - 2)]:
                        CheckMateSpaces[0][7] = True
                if i == 10 or i == 13:
                    if abs(WhitePiecePositions[12][0] - BlackPiecePositions[i][0]) == abs(WhitePiecePositions[12][1] - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs(((WhitePiecePositions[12][1] - 1)) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) < 0:
                                #Down left collision check
                                Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) > 0:
                                #Up left collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) > 0:
                                #Up right collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        if Count != "FAULT":
                                CheckMateSpaces[0][0] = True
                    if abs(WhitePiecePositions[12][0] - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] - 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] - 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][2] = True
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs(WhitePiecePositions[12][1] - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                            Count = "FAULT"
                                            break
                        if Count != "FAULT":
                                CheckMateSpaces[0][3] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs(WhitePiecePositions[12][1] - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up left collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][4] = True
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][5] = True
                    if abs((WhitePiecePositions[12][0]) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                                        CheckMateSpaces[0][6] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][7] = True
                if i == 11:
                    if BlackPiecePositions[i][0] < WhitePiecePositions[12][0] and BlackPiecePositions[i][1] == WhitePiecePositions[12][1]: #If to left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < WhitePiecePositions[12][0]:
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                            CheckMateSpaces[0][3] = True
                    elif BlackPiecePositions[i][0] > WhitePiecePositions[12][0] and BlackPiecePositions[i][1] == WhitePiecePositions[12][1]: #If to right
                        Count = 1
                        while (BlackPiecePositions[i][0] - Count) > WhitePiecePositions[12][0]:
                            if [BlackPiecePositions[i][0] - Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] - Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                            CheckMateSpaces[0][4] = True
                    elif BlackPiecePositions[i][1] > WhitePiecePositions[12][1] and BlackPiecePositions[i][0] == WhitePiecePositions[12][0]: #If below
                        Count = 1
                        while (BlackPiecePositions[i][1] - Count) > WhitePiecePositions[12][1]:
                            if [BlackPiecePositions[i][0],BlackPiecePositions[i][1] - Count] in BlackPiecePositions or [BlackPiecePositions[i][0],BlackPiecePositions[i][1] - Count] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                                CheckMateSpaces[0][6] = True
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                    elif BlackPiecePositions[i][1] < WhitePiecePositions[12][1] and BlackPiecePositions[i][0] == WhitePiecePositions[12][0]: #If above
                        Count = 1
                        while (BlackPiecePositions[i][1] + Count) < WhitePiecePositions[12][1]:
                            if [BlackPiecePositions[i][0],BlackPiecePositions[i][1] + Count] in BlackPiecePositions or [BlackPiecePositions[i][0],BlackPiecePositions[i][1] + Count] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                                CheckMateSpaces[0][1] = True
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","White is in check")
                            CheckMateSpaces[0][8] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][0] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0]) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] - 1): #Check for up and to the right
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] + 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][2] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1]): #Check for to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][3] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1]): #Check for to the right
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] + 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][4] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] - 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0] - 1):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][5] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0]) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][6] = True
                    if BlackPiecePositions[i][0] < (WhitePiecePositions[12][0] + 1) and BlackPiecePositions[i][1] == (WhitePiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (BlackPiecePositions[i][0] + Count) < (WhitePiecePositions[12][0]):
                            if [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions or [BlackPiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in WhitePiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[0][7] = True
                    if (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                        #Down right collision check
                        Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                        for Count in range(1,Count):
                            if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                Count = "FAULT"
                                break
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs(((WhitePiecePositions[12][1] - 1)) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) < 0:
                                #Down left collision check
                                Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) > 0:
                                #Up left collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - ((WhitePiecePositions[12][1] - 1))) > 0:
                                #Up right collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        if Count != "FAULT":
                                CheckMateSpaces[0][0] = True
                    if abs(WhitePiecePositions[12][0] - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] - 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - WhitePiecePositions[12][0]) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - WhitePiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] - 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][2] = True
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs(WhitePiecePositions[12][1] - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                            Count = "FAULT"
                                            break
                        if Count != "FAULT":
                                CheckMateSpaces[0][3] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs(WhitePiecePositions[12][1] - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up left collision check
                                Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                                for Count in range(1,Count):
                                    if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - WhitePiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][4] = True
                    if abs((WhitePiecePositions[12][0] - 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][5] = True
                    if abs((WhitePiecePositions[12][0]) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                                        CheckMateSpaces[0][6] = True
                    if abs((WhitePiecePositions[12][0] + 1) - BlackPiecePositions[i][0]) == abs((WhitePiecePositions[12][1] + 1) - BlackPiecePositions[i][1]):
                        if (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:#and !=
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(BlackPiecePositions[i][0] - WhitePiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] + Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) > 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] - Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)) < 0 and (BlackPiecePositions[i][1] - (WhitePiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((BlackPiecePositions[i][0] - (WhitePiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in BlackPiecePositions or [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] in WhitePiecePositions and [(BlackPiecePositions[i][0] + Count),(BlackPiecePositions[i][1] - Count)] != WhitePiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][7] = True
        if PlayerTurn == 2:
            i = 0
            for i in range(0,16):
                print(i)
                if i < 8: #Check checks for pawn
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == BlackPiecePositions[12]:
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == BlackPiecePositions[12]:
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][0] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][0] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][1] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][1] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][2] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] - 1]:
                        CheckMateSpaces[0][2] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1]]:
                        CheckMateSpaces[0][3] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1]]:
                        CheckMateSpaces[0][3] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1]]:
                        CheckMateSpaces[0][4] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1]]:
                        CheckMateSpaces[0][4] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] + 1]:
                        CheckMateSpaces[0][5] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] - 1,BlackPiecePositions[12][1] +1]:
                        CheckMateSpaces[0][5] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] + 1]:
                        CheckMateSpaces[0][6] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0],BlackPiecePositions[12][1] + 1]:
                        CheckMateSpaces[0][6] = True
                    if [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] + 1]:
                        CheckMateSpaces[0][7] = True
                    elif [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 1)] == [BlackPiecePositions[12][0] + 1,BlackPiecePositions[12][1] + 1]:
                        CheckMateSpaces[0][7] = True
                if i == 8 or i == 15: #Check checks for castle
                    if WhitePiecePositions[i][0] < BlackPiecePositions[12][0] and WhitePiecePositions[i][1] == BlackPiecePositions[12][1]: #If to left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < BlackPiecePositions[12][0]:
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][0] > BlackPiecePositions[12][0] and WhitePiecePositions[i][1] == BlackPiecePositions[12][1]: #If to right
                        Count = 1
                        while (WhitePiecePositions[i][0] - Count) > BlackPiecePositions[12][0]:
                            if [WhitePiecePositions[i][0] - Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] - Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][1] > BlackPiecePositions[12][1] and WhitePiecePositions[i][0] == BlackPiecePositions[12][0]: #If below
                        Count = 1
                        while (WhitePiecePositions[i][1] - Count) > BlackPiecePositions[12]:
                            if [WhitePiecePositions[i][0],WhitePiecePositions[i][1] - Count] in WhitePiecePositions or [WhitePiecePositions[i][0],WhitePiecePositions[i][1] - Count] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][1] < BlackPiecePositions[12][1] and WhitePiecePositions[i][0] == BlackPiecePositions[12][0]: #If above
                        Count = 1
                        while (WhitePiecePositions[i][1] + Count) < BlackPiecePositions[12]:
                            if [WhitePiecePositions[i][0],WhitePiecePositions[i][1] + Count] in WhitePiecePositions or [WhitePiecePositions[i][0],WhitePiecePositions[i][1] + Count] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][0] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0]) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][1] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up and to the right
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] + 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][2] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1]): #Check for to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][3] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1]): #Check for to the right
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] + 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][4] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][5] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0]) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][6] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][7] = True
                if i == 9 or i == 14: #Check checks for knight
                    if BlackPiecePositions[12] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]: #Right up
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]: #Right down
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]: #Down right
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] + 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]: #Down left
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] + 2)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]: #Left down
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] + 1)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]: #Left up
                        tk.messagebox.showinfo("Check","Black is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 2),(WhitePiecePositions[i][1] - 1)]:
                        CheckMateSpaces[1][7] = True
                    if BlackPiecePositions[12] ==  [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]: #Up left
                        tk.messagebox.showinfo("Check","White is in check")
                        CheckMateSpaces[1][8] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][0] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][1] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] - 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][2] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][3] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1])] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][4] = True
                    if [(BlackPiecePositions[12][0] - 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][5] = True
                    if [(BlackPiecePositions[12][0]),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][6] = True
                    if [(BlackPiecePositions[12][0] + 1),(BlackPiecePositions[12][1] + 1)] == [(WhitePiecePositions[i][0] - 1),(WhitePiecePositions[i][1] - 2)]:
                        CheckMateSpaces[1][7] = True
                if i == 10 or i == 13:
                    if abs(BlackPiecePositions[12][0] - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                            if (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
				#Down right collision check
                                Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                            elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                                #Down left collision check
                                Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12])
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                            elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                                #Up left collision check
                                Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                            elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                                #Up right collision check
                                Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12]))
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                            if Count != "FAULT":
                                tk.messagebox.showinfo("Check","Black is in check")
                                CheckMateSpaces[1][8] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs(((BlackPiecePositions[12][1] - 1)) - WhitePiecePositions[i][1]):
                            if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) < 0:
                                #Down right collision check
                                Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                            elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) < 0:
                                    #Down left collision check
                                    Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                                    for Count in range(1,Count):
                                        if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                            Count = "FAULT"
                                            break
                            elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) > 0:
                                    #Up left collision check
                                    Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                                    for Count in range(1,Count):
                                        if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                            Count = "FAULT"
                                            break
                            elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) > 0:
                                    #Up right collision check
                                    Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                                    for Count in range(1,Count):
                                        if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                            Count = "FAULT"
                                            break
                            if Count != "FAULT":
                                    CheckMateSpaces[1][0] = True
                    if abs(BlackPiecePositions[12][0] - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] - 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] - 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][2] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                            Count = "FAULT"
                                            break
                        if Count != "FAULT":
                            CheckMateSpaces[1][3] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up left collision check
                                Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                                for Count in range(1,Count):
                                    if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][4] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][5] = True
                    if abs((BlackPiecePositions[12][0]) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][6] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][7] = True
                if i == 11:
                    if WhitePiecePositions[i][0] < BlackPiecePositions[12][0] and WhitePiecePositions[i][1] == BlackPiecePositions[12][1]: #If to left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < BlackPiecePositions[12][0]:
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][0] > BlackPiecePositions[12][0] and WhitePiecePositions[i][1] == BlackPiecePositions[12][1]: #If to right
                        Count = 1
                        while (WhitePiecePositions[i][0] - Count) > BlackPiecePositions[12][0]:
                            if [WhitePiecePositions[i][0] - Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] - Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][1] > BlackPiecePositions[12][1] and WhitePiecePositions[i][0] == BlackPiecePositions[12][0]: #If below
                        Count = 1
                        while (WhitePiecePositions[i][1] - Count) > BlackPiecePositions[12]:
                            if [WhitePiecePositions[i][0],WhitePiecePositions[i][1] - Count] in WhitePiecePositions or [WhitePiecePositions[i][0],WhitePiecePositions[i][1] - Count] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    elif WhitePiecePositions[i][1] < BlackPiecePositions[12][1] and WhitePiecePositions[i][0] == BlackPiecePositions[12][0]: #If above
                        Count = 1
                        while (WhitePiecePositions[i][1] + Count) < BlackPiecePositions[12]:
                            if [WhitePiecePositions[i][0],WhitePiecePositions[i][1] + Count] in WhitePiecePositions or [WhitePiecePositions[i][0],WhitePiecePositions[i][1] + Count] in BlackPiecePositions:
                                Count = "FAULT"
                                break
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][0] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0]) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][1] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] - 1): #Check for up and to the right
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] + 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][2] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1]): #Check for to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,BlackPiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][3] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1]): #Check for to the right
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] + 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][4] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] - 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0] - 1):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][5] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0]) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][6] = True
                    if WhitePiecePositions[i][0] < (BlackPiecePositions[12][0] + 1) and WhitePiecePositions[i][1] == (BlackPiecePositions[12][1] + 1): #Check for down and to the left
                        Count = 1
                        while (WhitePiecePositions[i][0] + Count) < (BlackPiecePositions[12][0]):
                            if [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in WhitePiecePositions or [WhitePiecePositions[i][0] + Count,WhitePiecePositions[i][1]] in BlackPiecePositions:
                                Count = "FAULT"
                                break    
                            else:
                                Count = Count + 1
                        if Count != "FAULT":
                            CheckMateSpaces[1][7] = True
                    if abs(BlackPiecePositions[12][0] - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
			    #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
			    #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
			    #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
			    #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            tk.messagebox.showinfo("Check","Black is in check")
                            CheckMateSpaces[1][8] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs(((BlackPiecePositions[12][1] - 1)) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - ((BlackPiecePositions[12][1] - 1))) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][0] = True
                    if abs(BlackPiecePositions[12][0] - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] - 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - BlackPiecePositions[12][0]) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - BlackPiecePositions[12][0]))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[0][1] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] - 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                        Count = "FAULT"
                                        break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] - 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][2] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][3] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs(BlackPiecePositions[12][1] - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - BlackPiecePositions[12][1]) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][4] = True
                    if abs((BlackPiecePositions[12][0] - 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] - 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] - 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][5] = True
                    if abs((BlackPiecePositions[12][0]) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0])
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0])))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][6] = True
                    if abs((BlackPiecePositions[12][0] + 1) - WhitePiecePositions[i][0]) == abs((BlackPiecePositions[12][1] + 1) - WhitePiecePositions[i][1]):
                        if (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down right collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) < 0:
                            #Down left collision check
                            Count = abs(WhitePiecePositions[i][0] - BlackPiecePosition[12][0] + 1)
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] + Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) > 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up left collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] - Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        elif (WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)) < 0 and (WhitePiecePositions[i][1] - (BlackPiecePositions[12][1] + 1)) > 0:
                            #Up right collision check
                            Count = abs((WhitePiecePositions[i][0] - (BlackPiecePositions[12][0] + 1)))
                            for Count in range(1,Count):
                                if [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in WhitePiecePositions or [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] in BlackPiecePositions and [(WhitePiecePositions[i][0] + Count),(WhitePiecePositions[i][1] - Count)] != BlackPiecePositions[12]:
                                    Count = "FAULT"
                                    break
                        if Count != "FAULT":
                            CheckMateSpaces[1][7] = True

        if CheckMateSpaces[0] == [True,True,True,True,True,True,True,True,True]:
            tk.messagebox.showinfo("Checkmate","Black wins.")
            TkGui.destroy()
            os.system("MainMenu.py")
        elif CheckMateSpaces[1] == [True,True,True,True,True,True,True,True,True]:
            tk.messagebox.showinfo("Checkmate","White wins.")
            TkGui.destroy()
            os.system("MainMenu.py")
        else:
            #PlayerSwap
            if PlayerTurn == 1:
                PlayerTurn = 2
            elif PlayerTurn == 2:
                PlayerTurn = 1
            TurnState = 1
        
print("IM OUT OF THE WHILE TRUE")




