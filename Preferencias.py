from tkinter import *


class Preferencias:

    def executar(self, root) -> None:
        self.__preferencias = Toplevel(root, bg='white')
        self.montar_preferencias()


    @property
    def preferencias(self) -> Toplevel:
        return self.__preferencias


    def montar_preferencias(self) -> None:
        self.preferencias.geometry('300x400')
        self.preferencias.resizable(False, False)
        self.preferencias.title('Bloco de Notas - Preferências')
        self.preferencias.grab_set()

        lb_frame = LabelFrame(
            self.preferencias, text='Fonte', bg='white', fg='black',
            relief='solid', borderwidth=1, 
            labelanchor='nw', width=280, height=100
        )
        lb_frame.place(x=10, y=10)

        Label(lb_frame, text='Tamanho', bg='white').place(x=10, y=10)
        spbox = Spinbox(lb_frame, from_=1, to=20)
        spbox.place(x=80, y=10, width=40)