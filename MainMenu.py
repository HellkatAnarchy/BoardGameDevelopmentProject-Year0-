#MainMenu.py
#Is the main menu

#//Importing of libraries\\#
from tkinter import * # The GUI module.
import sys
import os

def ChessFunction():
    MenuGui.destroy()
    os.system("Chess.py") 

def DraughtsFunction():
    MenuGui.destroy()
    os.system("Draughts.py") 

def SLFunction():
    MenuGui.destroy()
    os.system("SnakesLaddersFixed.py") 

##def BSFunction():
##    messagebox.showinfo("Battleships is incomplete and is not playable at this time")

def TTTFunction():
    MenuGui.destroy()
    os.system("TicTacToe.py")    

def ChessHelpFunction():
    messagebox.showinfo("Chess help",
                        """Chess is a game played between two opponents on opposite sides of a board containing 64 squares of alternating colors. Each player has 16 pieces: 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights, and 8 pawns. The goal of the game is to checkmate the other king. Checkmate happens when the king is in a position to be captured (in check) and cannot escape from capture.

To learn more, go to: www.chess.com/learn-how-to-play-chess""")

def DraughtsHelpFunction():
    messagebox.showinfo("Draughts help","""Draughts (or checkers) is played by two opponents, on opposite sides of the gameboard. One player has the dark pieces; the other has the light pieces. Players alternate turns. A player may not move an opponent's piece. The player with the light pieces moves first unless stated otherwise. A move consists of moving a piece diagonally to an adjacent unoccupied square. If the adjacent square contains an opponent's piece, and the square immediately beyond it is vacant, the piece may be captured (and removed from the game) by jumping over it.

To learn more go to: http://www.wikiwand.com/en/Draughts#/General_rules""")

def SLHelpFunction():
    messagebox.showinfo("Snakes and ladders help","Players take turns rolling a dice to move their counter up the board. The objective is to get to the end square, but if you land on a ladder you must climb the ladder and if you land on a snake, you must go down the snake.")

##def BSHelpFunction():
##    messagebox.showinfo("Battleships help","Players begin by placing their battleships. Then players take turns guessing a square where they think the opposing player may have placed a ship. If a square is guessed, it is hit and they get another go. If all of the ship is hit, then the ship is sunk. If all of a players ships are sunk, then the opposing player wins.")

def TTTHelpFunction():
    messagebox.showinfo("Tic-tac-toe help","Players take turns choosing squares. One players is X's and the other O's. When they choose a square, either an X or an O is placed on that square (Depending on who placed it). If 3 squares horizontally, vertically or diagonally have the same symbol, then the owner of that symbol wins.")

def ExitButtonCommand():
    MenuGui.destroy()
    quit()

MenuGui = Tk()

#Get Screen resolution
ScreenWidth = MenuGui.winfo_screenwidth()
ScreenHeight = MenuGui.winfo_screenheight()

#Setting the windowed resolution
WindowedResolution = (str(int(ScreenWidth / 2)) + "x" + str(int(ScreenHeight / 2)) + "+0+0")
FullscreenResolution = (str(int(ScreenWidth)) + "x" + str(int(ScreenHeight)) + "+0+0")

#Telling the menu to display in fullscreen
MenuGui.attributes("-fullscreen", True) 

#Setting up the screen
MenuGui.geometry(FullscreenResolution)
MenuGui.resizable(width = FALSE, height = FALSE)
MenuGui.title('Main menu')
MenuGui.configure(background='#e1f5fe')

#Image setup
ChessImage = PhotoImage(file="Images/ChessImage.gif")
DraughtsImage = PhotoImage(file="Images/DraughtsImage.gif")
SLImage = PhotoImage(file="Images/SLImage.gif")
##BSImage = PhotoImage(file="Images/BSImage.gif")
TTTImage = PhotoImage(file="Images/TTTImage.gif")
HelpImage = PhotoImage(file="Images/HelpImage.gif")

#Drawing design elements
TheCanvas = Canvas(MenuGui, width=1920, height=1080, background = "#e1f5fe")
TheCanvas.pack()
TheCanvas.create_rectangle(0, 0, 1920, 100, fill="#03a9f4")
TheCanvas.create_rectangle(0, 100, 1920, 200, fill="#e0e0e0")
TheCanvas.create_rectangle(0, 370, 1920, 380, fill="#fafafa")
TheCanvas.create_rectangle(0, 620, 1920, 630, fill="#fafafa")

#Game Buttons
Button(MenuGui, height = 227, width = 227, foreground = "#b3e5fc", background = "#b3e5fc", image=ChessImage, command = ChessFunction).place(x=200,y=385)
Button(MenuGui, height = 227, width = 227, foreground = "#b3e5fc", background = "#b3e5fc", image=DraughtsImage, command = DraughtsFunction).place(x=500,y=385)
Button(MenuGui, height = 227, width = 227, foreground = "#b3e5fc", background = "#b3e5fc", image=SLImage, command = SLFunction).place(x=800,y=385)
##Button(MenuGui, height = 227, width = 227, foreground = "#b3e5fc", background = "#b3e5fc", image=BSImage, command = BSFunction).place(x=1100,y=385)
Button(MenuGui, height = 227, width = 227, foreground = "#b3e5fc", background = "#b3e5fc", image=TTTImage, command = TTTFunction).place(x=1400,y=385)

#HelpButtons             
Button(MenuGui, relief="flat", height = 2, width = 5, text = "+", font = ('Myriad Pro',20), foreground = "#000000", activeforeground="#03a9f4", activebackground="#03a9f4", background = "#03a9f4", command = ChessHelpFunction).place(x=275,y=580)
Button(MenuGui, relief="flat", height = 2, width = 5, text = "+", font = ('Myriad Pro',20), foreground = "#000000", activeforeground="#03a9f4", activebackground="#03a9f4", background = "#03a9f4", command = DraughtsHelpFunction).place(x=575,y=580)
Button(MenuGui, relief="flat", height = 2, width = 5, text = "+", font = ('Myriad Pro',20), foreground = "#000000", activeforeground="#03a9f4", activebackground="#03a9f4", background = "#03a9f4", command = SLHelpFunction).place(x=875,y=580)
##Button(MenuGui, relief="flat", height = 2, width = 5, text = "+", font = ('Myriad Pro',20), foreground = "#000000", activeforeground="#03a9f4", activebackground="#03a9f4", background = "#03a9f4", command = BSHelpFunction).place(x=1175,y=580)
Button(MenuGui, relief="flat", height = 2, width = 5, text = "+", font = ('Myriad Pro',20), foreground = "#000000", activeforeground="#03a9f4", activebackground="#03a9f4", background = "#03a9f4", command = TTTHelpFunction).place(x=1475,y=580)

#ExitButton
Button(MenuGui, relief="flat", height = 1, width = 5, text = "X", font = ('Myriad Pro',30), foreground = "#ffffff", activeforeground="#ffffff", activebackground="#03a9f4", background = "#03a9f4", command = ExitButtonCommand).place(x=1830,y=5)

#Text
Label(MenuGui, text = "Main Menu", font = ('Myriad Pro',50), background = "#03a9f4", fg="#ffffff").place(x=20, y=10) 
Label(MenuGui, text = "Games", font = ('Myriad Pro',38), background = "#e0e0e0", fg="#a4a4a4").place(x=20, y=110) 


mainloop()

