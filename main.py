from tkinter import *
from tkinter.font import Font
from Arquivo import Arquivo
from Editar import Editar
from Preferencias import Preferencias

root = Tk()
root.geometry('500x500')
root.title('Bloco de notas')


text_space = Text(root, relief=FLAT, wrap=NONE, font='Arial 12')
font = Font(font=text_space['font'])
tab_size = font.measure('    ')
text_space.config(tabs=tab_size)
text_space.pack(expand=TRUE, fill=BOTH)

scrollbar1 = Scrollbar(text_space, width=8)
text_space.config(yscrollcommand=scrollbar1.set)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.config(command=text_space.yview)

scrollbar2 = Scrollbar(text_space, width=8, orient='horizontal')
text_space.config(xscrollcommand=scrollbar2.set)
scrollbar2.pack(side=BOTTOM, fill=X)
scrollbar2.config(command=text_space.xview)


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
editar = Editar()
menu_editar.add_command(label='Recortar', command=lambda: editar.recortar(text_space))
menu_editar.add_command(label='Copiar', command=lambda: editar.copiar(text_space))
menu_editar.add_command(label='Colar', command=lambda: editar.colar(text_space))
menu_editar.add_separator()
preferencias = Preferencias()
menu_editar.add_command(label='Preferências', command=lambda: preferencias.executar(root, text_space))
barra_menus.add_cascade(label='Editar', menu=menu_editar)

root.config(menu=barra_menus)

root.mainloop()
