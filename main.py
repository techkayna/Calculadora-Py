from tkinter import *
from tkinter import ttk

#Cores a serem usadas em HEX
colorB = '#000000' # Black
colorW = '#FFFFFF' # White
colorG = '#8C8C8C' # Grey
colorO = '#FFA500' # Orange


janela =Tk()
janela.title('Calculadora')
janela.geometry('280x380')
janela.config(bg=colorB)

frame_screen = Frame(janela, width=280, height=50, bg=colorG)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=280, height=330)
frame_body.grid(row=1, column=0)

janela.mainloop()
