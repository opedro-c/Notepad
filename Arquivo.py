from tkinter import filedialog
from tkinter import *

class Arquivo:
    
    def __init__(self):
        self.__arquivo_atual = ''

    @property
    def arquivo_atual(self):
        return self.__arquivo_atual


    @arquivo_atual.setter
    def arquivo_atual(self, caminho):
        self.__arquivo_atual = caminho


    def novo_arquivo(self):
        pass

    
    def abrir_arquivo(self, text_space):
        filetypes = (
            ('Texto', '*.txt'),
            ('Python', '*.py'),
            ('Java', '*.java'),
            ('HTML', '*.html')
        )
        self.arquivo_atual = filedialog.askopenfilename(filetypes=filetypes)
        with open(self.arquivo_atual, 'r') as arquivo:
            texto_arquivo = arquivo.read()
            text_space.delete('1.0', END)
            text_space.insert('1.0', texto_arquivo)

    def salvar_arquivo(self):
        pass
