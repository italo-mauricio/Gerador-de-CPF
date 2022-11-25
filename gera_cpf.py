from tkinter import *
from tkinter import ttk
from random import randint




color1 = "#ff0000"  # red
color2 = "#008c00"  # green
color3 = "#000000"  # black


window = Tk()            # chama a biblioteca tkinter
window.title("")         # deixa o título da janela vazia
window.configure(bg=color3)         # escolho a cor de fundo da janela 
window.geometry("400x200")          # escolho o tamanho da janela
window.resizable(width= False, height= False)       # impeço do usuário mudar o tamanho da tela


text_generator = Label(window,text="CPF Generator", bg=color3, fg=color1, font=('Ivy',20,'bold')) # definindo o texto, a fonte e a cor da fundo da tela
text_generator.place(x=75,y=20)

def gerar():
        num = str(randint(100000000, 999999999))


        new_cpf = num
        reverse = 10
        total = 0


        for i in range(19):
            if i > 8:
                i -= 9
            total += int(new_cpf[i]) * reverse

            reverse -= 1
            if reverse < 2:
                reverse = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                new_cpf += str(d)

        cpf['text'] = new_cpf


bnt = Button(window, text="Generate CPF", command=gerar, bg=color2, fg=color3, font=('Arial', 15, 'bold'), 
                    relief=RAISED, overrelief=SUNKEN)
bnt.place(x=150,y=70)



cpf = Label(window, text="", bg=color3, fg=color2, font=('Arial', 30, 'bold'))
cpf.place(x=85,y=120)



window.mainloop()




