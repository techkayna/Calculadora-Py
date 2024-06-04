from tkinter import *
from tkinter import ttk

#Cores a serem usadas em HEX

colorB = '#000000' # Black
colorW = '#FFFFFF' # White
colorG = '#8C8C8C' # Grey
colorO = '#FFA500' # Orange


janela =Tk()
janela.title('Calculadora')
janela.geometry('240x318')
janela.config(bg=colorB)

frame_screen = Frame(janela, width=240, height=50, bg=colorG)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=240, height=268)
frame_body.grid(row=1, column=0)

b_1 = Button(frame_body, text='C', width=15, height=2, relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=0)
b_2 = Button(frame_body, text='%', width=8, height=2, relief=RAISED, overrelief=RIDGE) 
b_2.place(x=110, y=0)
b_3 = Button(frame_body, text='/', width=8, height=2, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=177, y=0)

b_4 = Button(frame_body, text='7', width=8, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=0, y=40)
b_4 = Button(frame_body, text='8', width=8, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=110, y=40)
b_4 = Button(frame_body, text='9', width=8, height=2, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=118, y=40)
b_3 = Button(frame_body, text='*', width=8, height=2, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=177, y=40)

janela.mainloop()
