from tkinter import *
from pyperclip import copy, paste


class Editar:


    def recortar(self, text_space: Text) -> None:
        try:
            copy(text_space.get(SEL_FIRST, SEL_LAST))
            text_space.delete(SEL_FIRST, SEL_LAST)
        except TclError:
            copy('')

    
    def copiar(self, text_space: Text) -> None:
        try:
            copy(text_space.get(SEL_FIRST, SEL_LAST))
        except TclError:
            copy('')
    

    def colar(self, text_space: Text) -> None:
        text_space.insert(text_space.index(INSERT), paste())
    
