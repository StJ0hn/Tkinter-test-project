from tkinter import *


janela = Tk()
janela.title("Entry")
janela.geometry("250x250")
janela.config(bg='Black')
janela.resizable()
janela.iconbitmap('Aulas/storm_icon.ico')

#Bloco para inserir nome.
label = Label(janela, width=10, text='Nome: ', font=('Times 11'), bg='#1808a3', fg='#94fa41')
label.grid(row=0, column=0, padx=10, pady= 10)

entry = Entry(janela, width=10, bg='Black', fg='White')
entry.grid(row=0, column=1)

#Bloco para inserir idade.
label_idade = Label(janela, width=10, text='Idade: ', font=('Times 11'), bg='#1808a3', fg='#94fa41')
label_idade.grid(row=1, column=0, padx=10, pady= 10)

entry_idade = Entry(janela, width=10, bg='Black', fg='White')
entry_idade.grid(row=1, column=1)

#Bloco para país.
label_país = Label(janela, width=10, text='País: ', font=('Times 11'), bg='#1808a3', fg='#94fa41')
label_país.grid(row=2, column=0, padx=10, pady= 10)

entry_país = Entry(janela, width=10, bg='Black', fg='White')
entry_país.grid(row=2, column=1)

janela.mainloop()