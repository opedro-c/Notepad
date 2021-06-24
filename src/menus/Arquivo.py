from tkinter import filedialog as fd, messagebox as mb
from tkinter import *


class Arquivo:

    filetypes = (
            ('Texto', '*.txt'),
            ('Python', '*.py'),
            ('Java', '*.java'),
            ('HTML', '*.html'),
            ('JavaScript', '*.js')
        )
    

    def __init__(self) -> None:
        self.__arquivo_atual: str = ''
        self.__conteudo_arquivo: str = ''

    @property
    def arquivo_atual(self) -> str:
        return self.__arquivo_atual


    @arquivo_atual.setter
    def arquivo_atual(self, caminho: str) -> None:
        self.__arquivo_atual = caminho


    @property
    def conteudo_arquivo(self) -> str:
        return self.__conteudo_arquivo
    

    @conteudo_arquivo.setter
    def conteudo_arquivo(self, conteudo: str) -> None:
        self.__conteudo_arquivo = conteudo
    

    def arquivo_modificado(self, text_space: Text) -> bool:
        return self.conteudo_arquivo != text_space.get('1.0', END)[:-1]


    def perguntar_salvar(self, text_space: Text) -> None:
        confirma = mb.askyesno(
            title='Bloco de Notas', 
            message='Você deseja salvar as alterações realizadas?'
        )
        if confirma:
            self.salvar_arquivo(text_space)
        elif confirma == None:
            return


    def novo_arquivo(self, text_space: Text, root: Tk) -> None:
        if self.arquivo_modificado(text_space):
            self.perguntar_salvar(text_space)
        self.conteudo_arquivo = ''
        self.arquivo_atual = ''
        text_space.delete('1.0', END)
        root.title('Bloco de Notas')

    
    def abrir_arquivo(self, text_space: Text, root: Tk) -> None:
        if self.arquivo_modificado(text_space):
            self.perguntar_salvar(text_space)
        caminho_arquivo = fd.askopenfilename(filetypes=Arquivo.filetypes)
        if caminho_arquivo:
            self.arquivo_atual = caminho_arquivo
            with open(self.arquivo_atual, 'r') as arquivo:
                self.conteudo_arquivo = arquivo.read()[:-1]
                text_space.delete('1.0', END)
                text_space.insert('1.0', self.conteudo_arquivo)
                root.title(f'Bloco de Notas - {caminho_arquivo.split("/")[-1]}')

    
    def salvar_arquivo(self, text_space: Text, root: Tk) -> None:
        if self.arquivo_atual:
            with open(self.arquivo_atual, 'w') as arquivo:
                arquivo.write(text_space.get('1.0', END))
        else:
            self.salvar_como(text_space, root)
        self.conteudo_arquivo = text_space.get('1.0', END)[:-1]
    
    
    def salvar_como(self, text_space: Text, root: Tk) -> None:
        caminho_arquivo = fd.asksaveasfilename(
            filetypes=Arquivo.filetypes,
            defaultextension='.txt'
        )
        if caminho_arquivo:
            self.arquivo_atual = caminho_arquivo
            self.salvar_arquivo(text_space)
            root.title(f'Bloco de Notas - {caminho_arquivo.split("/")[-1]}')

    
    def fechar_bloco(self, text_space: Text, root: Tk) -> None:
        if self.arquivo_modificado(text_space):
            resp = mb.askyesnocancel(
                title='Bloco de Notas',
                message='Deseja salvar as alterações antes de fechar o Bloco de Notas?'
            )
            if resp == None:
                return
            elif resp:
                self.salvar_arquivo(text_space, root)
        root.quit()
