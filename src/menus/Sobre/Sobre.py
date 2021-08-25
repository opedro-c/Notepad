from tkinter import Label, PhotoImage, Tk, Toplevel
from os.path import dirname


class Sobre:
    

    def __init__(self) -> None:
        self.image = PhotoImage(file=dirname(__file__) +'/imgs/notepad.png')

    def sobre(self, master: Tk) -> None:
        gui_sobre = Toplevel(master=master)
        gui_sobre.title('Bloco de Notas - Sobre')
        gui_sobre.resizable(False, False)
        gui_sobre.wait_visibility()
        gui_sobre.grab_set()
        Label(master=gui_sobre, image=self.image).pack(fill='x')
        Label(master=gui_sobre, text='Notepad\nv 1.0\nNotepad é um simples bloco de notas').pack(fill='x')
        Label(master=gui_sobre, text='Criado por: Pedro Costa Aragão').pack(fill='x')
        Label(master=gui_sobre, text='Esse produto não possui garantia alguma').pack(fill='x')