from tkinter import *


def montar_preferencias(
    master: Toplevel, text: Text, pfonte: str, ptamanho: str,
    pestilo : str, pquebra_de_linha: str, ptamanho_tab: int,
    aplicar
) -> None:

    master.geometry('300x400')
    master.resizable(False, False)
    master.title('Bloco de Notas - Preferências')
    master.grab_set()

    lb_frame = LabelFrame(
        master, text='Fonte', bg='white', fg='black',
        relief='solid', borderwidth=1, 
        labelanchor='nw', width=280, height=150
    )
    lb_frame.place(x=10, y=10)

    fontes = ('Arial', 'Helvetica', 'Times')
    fonte = StringVar()
    fonte.set(pfonte)
    opt_menu = OptionMenu(lb_frame, fonte, *fontes)
    opt_menu.place(x=10, y=10)
    
    Label(lb_frame, text='Tamanho', bg='white', fg='black').place(x=10, y=50)
    tamanho = Spinbox(lb_frame, from_=1, to=20)
    tamanho.delete(0, END)
    tamanho.insert(0, ptamanho)
    tamanho.place(x=20, y=80, width=40)

    Label(lb_frame, text='Estilo', bg='white', fg='black').place(x=130, y=10)
    estilos = ('', 'bold', 'italic')
    estilo = StringVar()
    estilo.set(pestilo)
    estilo_opcao = IntVar()
    estilo_opcao.set(estilos.index(pestilo))
    Radiobutton(
        lb_frame, text='Regular', bg='white', fg='black', 
        variable=estilo_opcao, value=0, command=lambda: estilo.set(estilos[estilo_opcao.get()])
    ).place(x=130, y=30)
    Radiobutton(
        lb_frame, text='Negrito', bg='white', fg='black', 
        variable=estilo_opcao, value=1, command=lambda: estilo.set(estilos[estilo_opcao.get()])
    ).place(x=130, y=55)
    Radiobutton(
        lb_frame, text='Itálico', bg='white', fg='black', 
        variable=estilo_opcao, value=2, command=lambda: estilo.set(estilos[estilo_opcao.get()])
    ).place(x=130, y=80)

    Label(master, text='Quebra de linha', bg='white', fg='black').place(x=10, y=170)
    tipos_quebra_de_linha = ("none", "char", "word")
    quebra_de_linha = StringVar()
    quebra_de_linha.set(pquebra_de_linha)
    quebra_de_linha_opcao = IntVar()
    quebra_de_linha_opcao.set(tipos_quebra_de_linha.index(pquebra_de_linha))
    Radiobutton(
        master, text='Sem quebra de linha', bg='white', fg='black', borderwidth=0,
        variable=quebra_de_linha_opcao, value=0, command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
    ).place(x=20, y=190)
    Radiobutton(
        master, text='Dividir palavra em duas linhas', bg='white', fg='black', borderwidth=0, 
        variable=quebra_de_linha_opcao, value=1, command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
    ).place(x=20, y=210)
    Radiobutton(
        master, text='Quebra de linha com palavra inteira', bg='white', fg='black', borderwidth=0,
        variable=quebra_de_linha_opcao, value=2,command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
    ).place(x=20, y=230)

    Label(master, text='Recuo', bg='white', fg='black').place(x=10, y=260)
    Label(master, text='Tamanho do recuo em espaços', bg='white', fg='black').place(x=20, y=290)
    recuo = Spinbox(master, from_=1, to=24)
    recuo.delete(0, END)
    recuo.insert(0, ptamanho_tab)
    recuo.place(x=230, y=290, width=40)

    Button(master, text='Fechar', command=master.destroy).place(x=10, y=360)
    Button(
        master, text='Aplicar', 
        command=lambda: aplicar(text, fonte.get(), tamanho.get(), estilo.get(), quebra_de_linha.get(), int(recuo.get()))
    ).place(x=220, y=360)
