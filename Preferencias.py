from tkinter import *
from tkinter.font import Font


class Preferencias:


    def __init__(self) -> None:
        self.__fonte = 'Arial'
        self.__tamanho_fonte = '12'
        self.__estilo_fonte = 'regular'
        self.__quebra_de_linha = NONE
        self.__tamanho_tab = 4


    def executar(self, root, text) -> None:
        self.__preferencias = Toplevel(root, bg='white')
        self.montar_preferencias(text)


    @property
    def preferencias(self) -> Toplevel:
        return self.__preferencias


    @property
    def fonte(self) -> str:
        return self.__fonte


    @fonte.setter
    def fonte(self, nova_fonte: str) -> None:
        self.__fonte = nova_fonte
    

    @property
    def tamanho_fonte(self) -> str:
        return self.__tamanho_fonte
    

    @tamanho_fonte.setter
    def tamanho_fonte(self, novo_tamanho: str) -> None:
        self.__tamanho_fonte = novo_tamanho

    
    @property
    def estilo_fonte(self) -> str:
        return self.__estilo_fonte

    
    @estilo_fonte.setter
    def estilo_fonte(self, novo_estilo: str) -> None:
        self.__estilo_fonte = novo_estilo
    

    @property
    def quebra_de_linha(self) -> str:
        return self.__quebra_de_linha
    

    @quebra_de_linha.setter
    def quebra_de_linha(self, nova_quebra: str) -> None:
        self.__quebra_de_linha = nova_quebra
    

    @property
    def tamanho_tab(self) -> int:
        return self.__tamanho_tab
    

    @tamanho_tab.setter
    def tamanho_tab(self, novo_tamanho: int) -> None:
        self.__tamanho_tab = novo_tamanho


    def montar_preferencias(self, text) -> None:
        
        self.preferencias.geometry('300x400')
        self.preferencias.resizable(False, False)
        self.preferencias.title('Bloco de Notas - Preferências')
        self.preferencias.grab_set()

        lb_frame = LabelFrame(
            self.preferencias, text='Fonte', bg='white', fg='black',
            relief='solid', borderwidth=1, 
            labelanchor='nw', width=280, height=150
        )
        lb_frame.place(x=10, y=10)

        fontes = ('Arial', 'Helvetica', 'Times')
        fonte = StringVar()
        fonte.set(self.fonte)
        opt_menu = OptionMenu(lb_frame, fonte, *fontes)
        opt_menu.place(x=10, y=10)
        
        Label(lb_frame, text='Tamanho', bg='white', fg='black').place(x=10, y=50)
        tamanho = Spinbox(lb_frame, from_=1, to=20)
        tamanho.delete(0, END)
        tamanho.insert(0, self.tamanho_fonte)
        tamanho.place(x=20, y=80, width=40)

        Label(lb_frame, text='Estilo', bg='white', fg='black').place(x=130, y=10)
        estilos = ('regular', 'bold', 'italic')
        estilo = StringVar()
        estilo.set(self.estilo_fonte)
        estilo_opcao = IntVar()
        estilo_opcao.set(estilos.index(self.estilo_fonte))
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

        Label(self.preferencias, text='Quebra de linha', bg='white', fg='black').place(x=10, y=170)
        tipos_quebra_de_linha = (NONE, CHAR, WORD)
        quebra_de_linha = StringVar()
        quebra_de_linha.set(self.quebra_de_linha)
        quebra_de_linha_opcao = IntVar()
        quebra_de_linha_opcao.set(tipos_quebra_de_linha.index(self.quebra_de_linha))
        Radiobutton(
            self.preferencias, text='Sem quebra de linha', bg='white', fg='black', borderwidth=0,
            variable=quebra_de_linha_opcao, value=0, command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
        ).place(x=20, y=190)
        Radiobutton(
            self.preferencias, text='Dividir palavra em duas linhas', bg='white', fg='black', borderwidth=0, 
            variable=quebra_de_linha_opcao, value=1, command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
        ).place(x=20, y=210)
        Radiobutton(
            self.preferencias, text='Quebra de linha com palavra inteira', bg='white', fg='black', borderwidth=0,
            variable=quebra_de_linha_opcao, value=2,command=lambda: quebra_de_linha.set(tipos_quebra_de_linha[quebra_de_linha_opcao.get()])
        ).place(x=20, y=230)

        Label(self.preferencias, text='Recuo', bg='white', fg='black').place(x=10, y=260)
        Label(self.preferencias, text='Tamanho do recuo em espaços', bg='white', fg='black').place(x=20, y=290)
        recuo = Spinbox(self.preferencias, from_=1, to=24)
        recuo.delete(0, END)
        recuo.insert(0, self.tamanho_tab)
        recuo.place(x=230, y=290, width=40)

        Button(self.preferencias, text='Fechar', command=self.preferencias.destroy).place(x=10, y=360)
        Button(
            self.preferencias, text='Aplicar', 
            command=lambda: self.gravar_preferencias(text, fonte.get(), tamanho.get(), estilo.get(), quebra_de_linha.get(),int(recuo.get()))
        ).place(x=220, y=360)


    def gravar_preferencias(self, text: Text, fonte: str, tamanho: str, estilo: str, quebra_linha: str, recuo: int) -> None:
        print(f'fonte: -{fonte}- tamanho: -{tamanho}- estilo: -{estilo}- quebra: -{quebra_linha}- recuo: -{recuo}-')
        self.fonte = fonte
        self.tamanho_fonte = tamanho
        self.estilo_fonte = estilo
        self.quebra_de_linha = quebra_linha
        self.tamanho_tab = recuo
        text.config(font=f'{fonte} {tamanho} {estilo}', wrap=quebra_linha)
        font = Font(font=text['font'])
        tab_size = font.measure(' ' * recuo)
        text.config(tabs=tab_size)
