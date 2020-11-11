#_______________________________Tkinterrr functions_______________________________

from tkinter import Label, Button, Grid, mainloop, Pack, Tk
from tkinter import font as tkFont
import time
import pygame

gRoot = Tk()

helv = tkFont.Font(family='Helvetica', weight='bold')

gRoot.configure(bg='mint cream')
current_player = 'O'

g_status = Button(gRoot, text="Game status: Playing")
g_status.grid(row=0, column=3)

def changeText(arg):

        if arg == 1:
            flip_turn()
            b1['text'] = current_player
            pop()
            
            b1.configure(state="disabled")
            
        elif arg == 2:
            flip_turn()
            b2['text'] =  current_player
            pop()
            b2.configure(state="disabled")
            
    
        elif arg == 3:
            flip_turn()
            b3['text'] =  current_player
            pop()
            b3.configure(state="disabled")
            

        elif arg == 4:
            flip_turn()
            b4['text'] =  current_player
            pop()
            b4.configure(state="disabled")
            
     
        elif arg == 5:
            flip_turn()
            b5['text'] =  current_player
            pop()
            b5.configure(state="disabled")
            
    
        elif arg == 6:
            flip_turn()
            b6['text'] =  current_player
            pop()
            b6.configure(state="disabled")
            
    
        elif arg == 7:
            flip_turn()
            b7['text'] =  current_player
            pop()
            b7.configure(state="disabled")
            
    
        elif arg == 8:
            flip_turn()
            b8['text'] =  current_player
            pop()
            b8.configure(state="disabled")
            
     
        elif arg == 9:
            flip_turn()
            b9['text'] =  current_player
            pop()
            b9.configure(state="disabled")
            
        row_1 = b1['text'] == b2['text'] == b3['text'] != ""
        row_2 = b4['text'] == b5['text'] == b6['text'] != ""
        row_3 = b7['text'] == b8['text'] == b9['text'] != ""

        col1 = b1['text'] == b4['text'] == b7['text'] != ""
        col2 = b2['text'] == b5['text'] == b8['text'] != ""
        col3 = b3['text'] == b6['text'] == b9['text'] != ""

        diag1 = b1['text'] == b5['text'] == b9['text'] != ""  
        diag2 = b3['text'] == b5['text'] == b7['text'] != ""

        if row_1:                                       #1
            b1['bg'] = "green"
            b2['bg'] = "green"
            b3['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif row_2:                                      #2
            b4['bg'] = "green"
            b5['bg'] = "green"
            b6['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif row_3:                                      #3
            b7['bg'] = "green"
            b8['bg'] = "green"
            b9['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif col1:                                      #4
            b1['bg'] = "green"
            b4['bg'] = "green"
            b7['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif col2:                                      #5
            b2['bg'] = "green"
            b5['bg'] = "green"
            b8['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif col3:                                      #6
            b3['bg'] = "green"
            b6['bg'] = "green"
            b9['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif diag1:                                      #7
            b1['bg'] = "green"
            b5['bg'] = "green"
            b9['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
        elif diag2:                                      #8
            b7['bg'] = "green"
            b5['bg'] = "green"
            b3['bg'] = "green"
            g_status['text'] = "Game status: GameOver"
            disableAll()
            Air_horn()
            
        # if tie
        if b1['text'] and b2['text'] and b3['text'] and b4['text'] and b5['text'] and b6['text'] and b7['text'] and b8['text'] and b9['text'] != "":
            g_status['text'] = "Game status: GameOver"
            game_over_sound()
            disableAll()
            

def disableAll():
    b1.config(state = "disabled")
    b2.config(state = "disabled")
    b3.config(state = "disabled")
    b4.config(state = "disabled")
    b5.config(state = "disabled")
    b6.config(state = "disabled")
    b7.config(state = "disabled")
    b8.config(state = "disabled")
    b9.config(state = "disabled")


def flip_turn():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return current_player

pygame.mixer.init()

def pop():
    pygame.mixer.music.load(r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\Tic-Tac-Toe Project\Sound\pop.mp3") # r means 'raw string'
    pygame.mixer.music.play()

def Air_horn():
    pygame.mixer.music.load(r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\Tic-Tac-Toe Project\Sound\Air horn.mp3") # r means 'raw string'
    pygame.mixer.music.play()


def game_over_sound():
    pygame.mixer.music.load(r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\Tic-Tac-Toe Project\Sound\gameOver.mp3") # r means 'raw string'
    pygame.mixer.music.play()




#tp = Button(gRoot, text="Play music", command=play_music)
#tp.grid(row=4, column=1)





#___________________________________Tkinter(main)______________________________________

l1 = Label(gRoot, text="Player 1: X", font="times 15", padx=0)
l1.grid(row=0, column=1)

l2 = Label(gRoot, text="Player 2: O", font="times 15", padx=0)
l2.grid(row=0, column=2)

#BUTTONS
b1 = Button(gRoot, width=15, height=5, text="", font=helv, bd=9, bg="floral white", command=lambda:changeText(1))
b1.grid(row=1, column=1)

b2 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(2))
b2.grid(row=1, column=2)

b3 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(3))
b3.grid(row=1, column=3)

b4 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(4))
b4.grid(row=2, column=1)

b5 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(5))
b5.grid(row=2, column=2)

b6 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(6))
b6.grid(row=2, column=3)

b7 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(7))
b7.grid(row=3, column=1)

b8 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(8))
b8.grid(row=3, column=2)

b9 = Button(gRoot, width=15, height=5, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(9))
b9.grid(row=3, column=3)

#b10 = Button(gRoot, width=10, height=3, text="", bd=9, font=helv, bg="floral white", command=lambda:changeText(9))
#b9.grid(row=4, column=1)

gRoot.mainloop()





 
