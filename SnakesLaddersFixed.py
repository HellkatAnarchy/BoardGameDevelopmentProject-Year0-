import tkinter as tk
import os
from random import randint

def ExitButtonCommand():
    TkGui.destroy()
    os.system("MainMenu.py")

def RollDiceCommand():
    global PlayerTurn
    pg.display.flip()
    TkGui.update()
    
    DiceRoll = randint(1,6)

    #Displaying DiceRoll result
    if DiceRoll == 1:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultOne)
        DiceResultLabel.place(x=1500,y=200)
    elif DiceRoll == 2:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultTwo)
        DiceResultLabel.place(x=1500,y=200)
    elif DiceRoll == 3:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultThree)
        DiceResultLabel.place(x=1500,y=200)
    elif DiceRoll == 4:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultFour)
        DiceResultLabel.place(x=1500,y=200)
    elif DiceRoll == 5:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultFive)
        DiceResultLabel.place(x=1500,y=200)
    elif DiceRoll == 6:
        DiceResultLabel = tk.Label(TkGui, image = DiceResultSix)
        DiceResultLabel.place(x=1500,y=200)

    #Movement
    if CounterPosition[PlayerTurn - 1][1] %2 == 1:
        CounterPosition[PlayerTurn - 1][0] -= DiceRoll
    else:
        CounterPosition[PlayerTurn - 1][0] += DiceRoll

    #Win condition check
    if CounterPosition[PlayerTurn - 1] == [0,7]:
        screen.blit(Board,(0,0))
        PlayerOneCounterPos = ((((CounterPosition[0][0] % 8) * 90) + 45)-40,720-(int(((CounterPosition[0][1] % 8) * 90) + 45))-40)
        PlayerTwoCounterPos = ((((CounterPosition[1][0] % 8) * 90) + 45)-40,720-(int(((CounterPosition[1][1] % 8) * 90) + 45))-40)
        screen.blit(PlayerOneCounter,PlayerOneCounterPos)
        screen.blit(PlayerTwoCounter,PlayerTwoCounterPos)
        pg.display.flip()
        tk.messagebox.showinfo("Winner", "Player " + str(PlayerTurn) + " wins!")
        TkGui.destroy()
        os.system("MainMenu.py")

    #More movement
    if CounterPosition[PlayerTurn - 1][0] > 7 and CounterPosition[PlayerTurn - 1][1] %2 == 0:
            CounterPosition[PlayerTurn - 1][1] += 1
            CounterPosition[PlayerTurn - 1][0] = 7 - (CounterPosition[PlayerTurn - 1][0] - 7)
    if CounterPosition[PlayerTurn - 1][0] < 0 and CounterPosition[PlayerTurn - 1][1] %2 == 1:
        if CounterPosition [PlayerTurn - 1][1] + 1 == 8:
             CounterPosition[PlayerTurn - 1][0] += DiceRoll   
        else:
            CounterPosition[PlayerTurn - 1][1] += 1
            CounterPosition[PlayerTurn - 1][0] = -CounterPosition[PlayerTurn - 1][0]

    #Snakes and ladders checks
    if CounterPosition[PlayerTurn - 1] == [1,0]:
        CounterPosition[PlayerTurn - 1] = [2,1]
    if CounterPosition[PlayerTurn - 1] == [6,1]:
        CounterPosition[PlayerTurn - 1] = [6,0]
    if CounterPosition[PlayerTurn - 1] == [5,1]:
        CounterPosition[PlayerTurn - 1] = [4,2]
    if CounterPosition[PlayerTurn - 1] == [2,3]:
        CounterPosition[PlayerTurn - 1] = [3,1]
    if CounterPosition[PlayerTurn - 1] == [1,2]:
        CounterPosition[PlayerTurn - 1] = [1,4]
    if CounterPosition[PlayerTurn - 1] == [6,2]:
        CounterPosition[PlayerTurn - 1] = [3,5]
    if CounterPosition[PlayerTurn - 1] == [6,2]:
        CounterPosition[PlayerTurn - 1] = [3,5]
    if CounterPosition[PlayerTurn - 1] == [5,6]:
        CounterPosition[PlayerTurn - 1] = [5,2]
    if CounterPosition[PlayerTurn - 1] == [7,4]:
        CounterPosition[PlayerTurn - 1] = [7,5]
    if CounterPosition[PlayerTurn - 1] == [6,7]:
        CounterPosition[PlayerTurn - 1] = [7,6]
    if CounterPosition[PlayerTurn - 1] == [3,7]:
        CounterPosition[PlayerTurn - 1] = [3,6]
    if CounterPosition[PlayerTurn - 1] == [1,6]:
        CounterPosition[PlayerTurn - 1] = [2,7]

    if PlayerTurn == 1:
        PlayerTurn = 2
        tk.Label(TkGui, text = "Player Twos Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900) 
    elif PlayerTurn == 2:
        PlayerTurn = 1
        tk.Label(TkGui, text = "Player Ones Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900) 

    #Reblotting the gameboard to remove duplicate game peices
    screen.blit(Board,(0,0))

if 'PlayerTurn' not in vars():        
    #Variable initialisation
    PlayerTurn = 1
    CounterPosition = [[0,0],[0,0]]
    DiceRoll = 0

#Setting up of the window
TkGui = tk.Tk()
TkGui.attributes("-fullscreen", True)
tk.Label(TkGui, text = "Player Ones Turn", font = ('Myriad Pro',50), background = "#e1f5fe", fg="#ffffff").place(x=850, y=900) 

#Image setup
DiceResultOne = tk.PhotoImage(file="Images/SnakeLadderDiceOne.gif")
DiceResultTwo = tk.PhotoImage(file="Images/SnakeLadderDiceTwo.gif")
DiceResultThree = tk.PhotoImage(file="Images/SnakeLadderDiceThree.gif")
DiceResultFour = tk.PhotoImage(file="Images/SnakeLadderDiceFour.gif")
DiceResultFive = tk.PhotoImage(file="Images/SnakeLadderDiceFive.gif")
DiceResultSix = tk.PhotoImage(file="Images/SnakeLadderDiceSix.gif")

#Get Screen resolution
ScreenWidth = TkGui.winfo_screenwidth()
ScreenHeight = TkGui.winfo_screenheight()
FullscreenResolution = (str(int(ScreenWidth)) + "x" + str(int(ScreenHeight)) + "+0+0")
TkGui.geometry(FullscreenResolution)
TkGui.title('Snakes and Ladders')
TkGui.configure(background='#e1f5fe')

#ExitButton
tk.Button(TkGui, relief="flat", height = 1, width = 5, text = "X", font = ('Myriad Pro',30), foreground = "#ffffff", activeforeground="#ffffff", activebackground="#03a9f4", background = "#03a9f4", command = ExitButtonCommand).place(x=1830,y=5)

#Shapes
TheCanvas = tk.Canvas(TkGui, width=1920, height=100, background = "#e1f5fe")
TheCanvas.pack()
TheCanvas.create_rectangle(0, 0, 1920, 100, fill="#03a9f4")

#Text
tk.Label(TkGui, text = "Snakes and Ladders", font = ('Myriad Pro',50), background = "#03a9f4", fg="#ffffff").place(x=20, y=10) 

#Buttons
tk.Button(TkGui, relief="flat", height = 1, width = 5, text = "X", font = ('Myriad Pro',30), foreground = "#ffffff", activeforeground="#ffffff", activebackground="#03a9f4", background = "#03a9f4", command = ExitButtonCommand).place(x=1830,y=5)
tk.Button(TkGui, relief="raised", height = 1, width = 10, text = "Roll Dice", font = ('Myriad Pro',30), foreground = "#ffffff", activeforeground="#ffffff", activebackground="#03a9f4", background = "#03a9f4", command = RollDiceCommand).place(x=1500,y=450)

PyGUI = tk.Frame(TkGui, width=720, height=720)
PyGUI.pack()

# Tell pygame's SDL window which window ID to use
# Taken from http://stackoverflow.com/questions/8584272/using-pygame-features-in-tkinter
os.environ['SDL_WINDOWID'] = str(PyGUI.winfo_id())

# Show the window so it's assigned an ID.
TkGui.update()

# Usual pygame initialization
import pygame as pg
pg.init()
screen = pg.display.set_mode((720,720))

#Board blotting and image loading
Board = pg.image.load("Images/SnakeLadderBoard.png")
pg.init()
screen.blit(Board,(0,0))
PlayerOneCounter = pg.image.load("Images/SnakeLadderCounterOne.png")
PlayerTwoCounter = pg.image.load("Images/SnakeLadderCounterTwo.png")
PlayerCounterStack = pg.image.load("Images/SnakeLadderCounterStack.png")


while True:
    pg.display.flip()
    TkGui.update()

    PlayerOneCounterPos = ((((CounterPosition[0][0] % 8) * 90) + 45)-40,720-(int(((CounterPosition[0][1] % 8) * 90) + 45))-40)
    PlayerTwoCounterPos = ((((CounterPosition[1][0] % 8) * 90) + 45)-40,720-(int(((CounterPosition[1][1] % 8) * 90) + 45))-40)

    if CounterPosition[0] != CounterPosition[1]:
        screen.blit(PlayerOneCounter,PlayerOneCounterPos)
        screen.blit(PlayerTwoCounter,PlayerTwoCounterPos) 

    else:
        screen.blit(PlayerCounterStack,PlayerOneCounterPos)    

   
