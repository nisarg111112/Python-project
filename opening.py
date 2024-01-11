import webbrowser
import subprocess
from tkinter import *

win=Tk()
win.geometry("500x500")
win.maxsize(500,500)
win.title("TETRIS")

def StartGame():
    subprocess.call(['python','main.py'])

def AboutWin():
    aboutwindow=Toplevel(win)
    aboutwindow.title("About Tetris")
    aboutwindow.geometry("")

    f1=Frame(aboutwindow,bg="#856ff8",borderwidth=10,pady=10)
    f1.pack(fill="x")
    f2=Frame(aboutwindow,bg="lightgreen",borderwidth=10,pady=10)
    f2.pack(fill="x")
    f3=Frame(aboutwindow,bg='navajo white',borderwidth=50,pady=10)
    f3.pack(fill="both")

    Title=Label(f1,text="\n\n About Tetris\n\n",font=("Times",25,"bold","italic","underline"),fg="black",bg="#856ff8")
    Title.pack()
   
    Tetris=Label(f2,text="Tetris is a puzzle video game created in 1985 by Alexey Pajitnov, a Soviet software engineer. It has been published by several companies for multiple platforms, most prominently during a dispute over the appropriation of the rights in the late 1980s. After a significant period of publication by Nintendo, in 1996 the rights reverted to Pajitnov, who co-founded the Tetris Company with Henk Rogers to manage licensing.\n\n\n In Tetris, players complete lines by moving differently shaped pieces (tetrominoes), which descend onto the playing field. The completed lines disappear and grant the player points, and the player can proceed to fill the vacated spaces. The game ends when the uncleared lines reach the top of the playing field. The longer the player can delay this outcome, the higher their score will be. In multiplayer games, players must last longer than their opponents; in certain versions, players can inflict penalties on opponents by completing a significant number of lines. Some versions add variations on the rules, such as three-dimensional displays or a system for reserving pieces.",wraplength=1000,font=("Times",16),bg="lightgreen")
    Tetris.pack()

    Link=Label(f3,text=" CLICK HERE TO CHECK THE TETRIS WORLD RECORD !!!",font=("Courier",15,"bold","underline"),fg='blue',cursor="hand2")
    Link.pack()
    Link.bind('<Button-1>',lambda x:webbrowser.open("https://youtu.be/GuJ5UuknsHU?si=0sFLun8gbmUWwlnX"))  

def HighScore():
    HSwindow=Toplevel(win)
    HSwindow.title("High Score")
    HSwindow.geometry("")
    HS=Label(HSwindow,text="NO HIGH SCORE...PLAY THE GAME!!!",font=("Times",10,"bold"))
    HS.pack()
   
    
photo=PhotoImage(file="tetris.png")
Tetris_Image=Label(image=photo,borderwidth=5,relief=RAISED)
Enter_The_Game=Button(text="Enter The Game",bg="grey",fg="black",font=("comicsansms",12,"bold"),relief=RAISED,height=1,width=15,command=StartGame)
Tetris_Image.pack()
space1=Label()
space1.pack()
Enter_The_Game.pack()
space2=Label()
space2.pack()
High_Score=Button(text="High Score",bg="grey",fg="black",font=("comicsansms",12,"bold"),relief=GROOVE,height=1,width=15,command=HighScore)
High_Score.pack()
space3=Label()
space3.pack()
About=Button(text="About",bg="grey",fg="black",font=("comicsansms",12,"bold"),relief=GROOVE,height=1,width=15,command=AboutWin)
About.pack()


win.mainloop()