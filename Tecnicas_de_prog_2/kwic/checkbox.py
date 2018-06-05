from tkinter import *
master = Tk()

def var_states():
	#Define variaveis dos botões
	print("English: %d,\nPortuguese %d" % (var1.get(), var2.get()))
#Define texto na primeira row com o seguinte texto
Label(master, text="What language: ").grid(row=0, sticky=W)
#Cria a variavel var1
var1 = IntVar()
#Cria o botão de checkbox com a opção de escolha ingles.
Checkbutton(master, text="English", variable=var1).grid(row=1, sticky=W)
#Cria a variavel var2
var2 = IntVar()
#Cria o botão de checkbox com a opção de escolha portugues
Checkbutton(master, text="Portuguese", variable=var2).grid(row=2, sticky=W)
#Cria dois botões, o primeiro sai do programa. O Segundo realiza a ação de mostrar o valor de var1 e var2.
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
#Continuar na execucao do programa enquanto master.quit não é chamado
mainloop()
