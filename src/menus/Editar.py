from tkinter import *
from tkinter import messagebox as mb
from pyperclip import PyperclipException, copy, paste

def validar_copia(func):
    def check(self, text_space: Tk) -> None:
        try:
            func(self, text_space)
        except PyperclipException as e:
            mb.showerror(title='Bloco de Notas', message=f'Ops! Ocorreu um erro: \n {str(e)}')
        except TclError as e:
            print(e)
    return check


class Editar:


    @validar_copia
    def recortar(self, text_space: Text) -> None:
        copy(text_space.get(SEL_FIRST, SEL_LAST))
        text_space.delete(SEL_FIRST, SEL_LAST)

    @validar_copia
    def copiar(self, text_space: Text) -> None:
        copy(text_space.get(SEL_FIRST, SEL_LAST))
    

    def colar(self, text_space: Text) -> None:
        text_space.insert(text_space.index(INSERT), paste())
    
