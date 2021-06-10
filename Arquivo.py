from tkinter import filedialog as fd
from tkinter import *

class Arquivo:

    filetypes = (
            ('Texto', '*.txt'),
            ('Python', '*.py'),
            ('Java', '*.java'),
            ('HTML', '*.html')
        )
    
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
        caminho_arquivo = fd.askopenfilename(filetypes=Arquivo.filetypes)
        if caminho_arquivo:
            self.arquivo_atual = caminho_arquivo
            with open(self.arquivo_atual, 'r') as arquivo:
                texto_arquivo = arquivo.read()
                text_space.delete('1.0', END)
                text_space.insert('1.0', texto_arquivo)

    
    def salvar_arquivo(self, text_space):
        if self.arquivo_atual:
            with open(self.arquivo_atual, 'w') as arquivo:
                arquivo.write(text_space.get('1.0', END))
        else:
            self.salvar_como(text_space)
    
    
    def salvar_como(self, text_space):
        caminho_arquivo = fd.asksaveasfilename(
            filetypes=Arquivo.filetypes,
            defaultextension='.txt'
        )
        if caminho_arquivo:
            self.arquivo_atual = caminho_arquivo
            self.salvar_arquivo(text_space)
