from tkinter import *
from tkinter import ttk

# Paletas de cores em HEX
colorB = '#000000' # Black
colorW = '#FFFFFF' # White
colorA = '#8686A6' # Azul Acizentado
colorG = '#8C8C8C' # Grey
colorO = '#FFA500' # Orange

# Criando a janela da calculadora
janela =Tk()
janela.title('Calculadora')
janela.geometry('260x314')
janela.config(bg=colorB)

# Criando os frames de tela
frame_screen = Frame(janela, width=260, height=53, bg=colorA)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=260, height=261)
frame_body.grid(row=1, column=0)

# Variavel valores
todos_valores = '' 

#Criando label
valor_texto = StringVar()

# Criando a função para calcular
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    # Exibir valor
    valor_texto.set(todos_valores)

# função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

#função clean
def clean():
    global todos_valores
    todos_valores =''
    valor_texto.set('')

app_label = Label(frame_screen, textvariable=valor_texto, width=19, height=2, padx=7, relief=FLAT, anchor='e', justify=LEFT, bg=colorA, fg=colorW, font=('Ivy 17'))
app_label.place(x=0, y=0)

# Criando Buttons
b_1 = Button(frame_body, command=clean, text='C', width=17, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_1.place(x=-0, y=0)
b_2 = Button(frame_body, command = lambda: entrar_valores('%'), text='%', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_2.place(x=128, y=0)
b_3 = Button(frame_body, command = lambda: entrar_valores('/'), text='/', width=8, height=3, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_3.place(x=194, y=0)

b_4 = Button(frame_body, command = lambda: entrar_valores('7'), text='7', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_4.place(x=-1, y=52)
b_5 = Button(frame_body, command = lambda: entrar_valores('8'), text='8', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_5.place(x=63, y=52)
b_6 = Button(frame_body, command = lambda: entrar_valores('9'), text='9', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_6.place(x=128, y=52)
b_7 = Button(frame_body, command = lambda: entrar_valores('*'), text='*', width=8, height=3, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_7.place(x=194, y=52)

b_8 = Button(frame_body, command = lambda: entrar_valores('4'), text='4', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_8.place(x=1, y=104)
b_9 = Button(frame_body, command = lambda: entrar_valores('5'), text='5', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_9.place(x=63, y=104)
b_10 = Button(frame_body, command = lambda: entrar_valores('6'), text='6', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_10.place(x=128, y=104)
b_11 = Button(frame_body, command = lambda: entrar_valores('-'), text='-', width=8, height=3, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_11.place(x=194, y=104)

b_12 = Button(frame_body, command = lambda: entrar_valores('1'), text='1', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_12.place(x=1, y=156)
b_13 = Button(frame_body, command = lambda: entrar_valores('2'), text='2', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_13.place(x=63, y=156)
b_14 = Button(frame_body, command = lambda: entrar_valores('3'), text='3', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_14.place(x=128, y=156)
b_15 = Button(frame_body, command = lambda: entrar_valores('+'), text='+', width=8, height=3, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_15.place(x=194, y=156)

b_16 = Button(frame_body, command = lambda: entrar_valores('0'), text='0', width=17, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_16.place(x=-0, y=208)
b_17 = Button(frame_body, command = lambda: entrar_valores(','), text=',', width=8, height=3, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_17.place(x=128, y=208)
b_18 = Button(frame_body, command = calcular, text='=', width=8, height=3, bg=colorO, fg=colorW, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold')) 
b_18.place(x=194, y=208)

janela.mainloop()
# Fim do loop