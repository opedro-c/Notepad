from tkinter import *
from Arquivo import Arquivo

root = Tk()
root.geometry('500x500')
root.title('Bloco de notas')

text_space = Text(root, relief=FLAT)
text_space.pack(expand=TRUE, fill=BOTH)

barra_menus = Menu(root)

menu_arquivo = Menu(barra_menus, tearoff=0)
arquivo = Arquivo()
menu_arquivo.add_command(label='Novo arquivo', command=lambda: arquivo.novo_arquivo(text_space))
menu_arquivo.add_command(label='Abrir arquivo', command=lambda: arquivo.abrir_arquivo(text_space))
menu_arquivo.add_command(label='Salvar', command=lambda: arquivo.salvar_arquivo(text_space))
menu_arquivo.add_command(label='Salvar como', command=lambda: arquivo.salvar_como(text_space))
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Fechar', command=lambda: arquivo.fechar_bloco(text_space, root))
barra_menus.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_editar = Menu(barra_menus, tearoff=0)
menu_editar.add_command(label='Cortar', command=None)
menu_editar.add_command(label='Copiar', command=None)
menu_editar.add_command(label='Colar', command=None)
menu_editar.add_separator()
menu_editar.add_command(label='Preferências', command=None)
barra_menus.add_cascade(label='Editar', menu=menu_editar)
root.config(menu=barra_menus)

root.mainloop()
