from tkinter import *
from tkinter import ttk



color1 = "#ff0000"  # red
color2 = "#008c00"  # green
color3 = "#000000"  # black


window = Tk()            # chama a biblioteca tkinter
window.title("")         # deixa o título da janela vazia
window.configure(bg=color3)         # escolho a cor de fundo da janela 
window.geometry("400x200")          # escolho o tamanho da janela
window.resizable(width= False, height= False)       # impeço do usuário mudar o tamanho da tela


text_generator = Label(window,text="CPF Generator", bg=color3, fg=color1, font=('Arial', 20, 'bold'))
text_generator.place(x=75,y=20)






window.mainloop()






