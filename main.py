from tkinter import *
from Arquivo import Arquivo

root = Tk()
root.geometry('500x500')
root.title('Bloco de notas')

barra_menus = Menu(root)

menu_arquivo = Menu(barra_menus, tearoff=0)
arquivo = Arquivo()
menu_arquivo.add_command(label='Novo arquivo', command=None)
menu_arquivo.add_command(label='Abrir arquivo', command=arquivo.abrir_arquivo)
menu_arquivo.add_command(label='Salvar arquivo', command=None)
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Sair', command=None)
barra_menus.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_editar = Menu(barra_menus, tearoff=0)
menu_editar.add_command(label='Cortar', command=None)
menu_editar.add_command(label='Copiar', command=None)
menu_editar.add_command(label='Colar', command=None)
menu_editar.add_separator()
menu_editar.add_command(label='Preferências', command=None)
barra_menus.add_cascade(label='Editar', menu=menu_editar)
root.config(menu=barra_menus)

text_space = Text(root)
text_space.pack(expand=TRUE, fill=BOTH)

root.mainloop()
