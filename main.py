from tkinter import *
from tkinter import ttk

#Cores a serem usadas em HEX

colorB = '#000000' # Black
colorW = '#FFFFFF' # White
colorG = '#8C8C8C' # Grey
colorO = '#FFA500' # Orange


janela =Tk()
janela.title('Calculadora')
janela.geometry('240x256')
janela.config(bg=colorB)

frame_screen = Frame(janela, width=240, height=55, bg=colorG)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=240, height=206)
frame_body.grid(row=1, column=0)

b_1 = Button(frame_body, text='AC', width=16, height=2, relief=RAISED, overrelief=RIDGE) 
b_1.place(x=-2, y=0)
b_2 = Button(frame_body, text='%', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_2.place(x=121, y=0)
b_3 = Button(frame_body, text='/', width=7, height=2, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=181, y=0)

b_4 = Button(frame_body, text='7', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=1, y=40)
b_4 = Button(frame_body, text='8', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=61, y=40)
b_4 = Button(frame_body, text='9', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=121, y=40)
b_3 = Button(frame_body, text='X', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=181, y=40)

b_4 = Button(frame_body, text='4', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=1, y=80)
b_4 = Button(frame_body, text='5', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=61, y=80)
b_4 = Button(frame_body, text='6', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=121, y=80)
b_3 = Button(frame_body, text='-', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=181, y=80)

b_4 = Button(frame_body, text='1', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=1, y=120)
b_4 = Button(frame_body, text='2', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=61, y=120)
b_4 = Button(frame_body, text='3', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=121, y=120)
b_3 = Button(frame_body, text='+', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_3.place(x=181, y=120)

b_4 = Button(frame_body, text='0', width=16, height=2, relief=RAISED, overrelief=RIDGE) 
b_4.place(x=-2, y=160)
b_5 = Button(frame_body, text=',', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_5.place(x=121, y=160)
b_6 = Button(frame_body, text='=', width=7, height=2, relief=RAISED, overrelief=RIDGE) 
b_6.place(x=181, y=160)

janela.mainloop()
