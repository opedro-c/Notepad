from tkinter import *
from menus.Arquivo import Arquivo
from menus.Editar import Editar
from menus.Preferencias.Preferencias import Preferencias
from os import chdir
from pathlib import Path

from menus.Sobre.Sobre import Sobre

chdir(Path.home())

root = Tk()
root.geometry('500x500')
root.title('Bloco de Notas')

text_space = Text(root, relief=FLAT)
preferencias = Preferencias(text_space)

scrollbar1 = Scrollbar(root, width=14)
text_space.config(yscrollcommand=scrollbar1.set)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.config(command=text_space.yview)

scrollbar2 = Scrollbar(root, width=14, orient='horizontal')
text_space.config(xscrollcommand=scrollbar2.set)
scrollbar2.pack(side=BOTTOM, fill=X)
text_space.pack(expand=TRUE, fill=BOTH)
scrollbar2.config(command=text_space.xview)

barra_menus = Menu(root)

menu_arquivo = Menu(barra_menus, tearoff=0)
arquivo = Arquivo()
menu_arquivo.add_command(label='Novo arquivo', command=lambda: arquivo.novo_arquivo(text_space, root))
menu_arquivo.add_command(label='Abrir arquivo', command=lambda: arquivo.abrir_arquivo(text_space, root))
menu_arquivo.add_command(label='Salvar', command=lambda: arquivo.salvar_arquivo(text_space, root))
menu_arquivo.add_command(label='Salvar como', command=lambda: arquivo.salvar_como(text_space, root))
menu_arquivo.add_separator()
menu_arquivo.add_command(label='Fechar', command=lambda: arquivo.fechar_bloco(text_space, root))
barra_menus.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_editar = Menu(barra_menus, tearoff=0)
editar = Editar()
menu_editar.add_command(label='Recortar', command=lambda: editar.recortar(text_space))
menu_editar.add_command(label='Copiar', command=lambda: editar.copiar(text_space))
menu_editar.add_command(label='Colar', command=lambda: editar.colar(text_space))
menu_editar.add_separator()
menu_editar.add_command(label='PreferĂȘncias', command=lambda: preferencias.executar(root, text_space))
barra_menus.add_cascade(label='Editar', menu=menu_editar)

sobre = Sobre()
barra_menus.add_command(command=lambda: sobre.sobre(root), label='Sobre')

root.config(menu=barra_menus)

root.mainloop()
