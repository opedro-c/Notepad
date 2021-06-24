from tkinter import *
from tkinter.font import Font
from .gui_preferencias import montar_preferencias
import os
import json


class Preferencias:


    def __init__(self, text: Text) -> None:
        if not os.path.isdir('config'):
            os.mkdir('config')
        os.chdir('config')
        if os.path.isfile('config.json'):
            with open('config.json', 'r') as config:
                configs = json.load(config)
        else:
            with open('config.json', 'w+') as config:
                preferencias = {
                        "fonte": "Arial",
                        "tamanho": "12",
                        "estilo": "",
                        "quebra_linha": "none",
                        "recuo": 4
                    }
                json.dump(preferencias, config)
                configs = preferencias
        self.__fonte = configs["fonte"]
        self.__tamanho_fonte = configs["tamanho"]
        self.__estilo_fonte = configs["estilo"]
        self.__quebra_de_linha = configs["quebra_linha"]
        self.__tamanho_tab = configs["recuo"]
        self.aplicar_preferencias(
            text, self.fonte, self.tamanho_fonte, self.estilo_fonte, 
            self.quebra_de_linha, self.tamanho_tab
        )

    def executar(self, root, text) -> None:
        self.__preferencias = Toplevel(root, bg='white')
        montar_preferencias(
            self.preferencias, text, self.fonte, self.tamanho_fonte,
            self.estilo_fonte, self.quebra_de_linha, self.tamanho_tab,
            self.aplicar_preferencias
        )


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


    def aplicar_preferencias(self, text: Text, fonte: str, tamanho: str, estilo: str, quebra_linha: str, recuo: int) -> None:
        self.fonte = fonte
        self.tamanho_fonte = tamanho
        self.estilo_fonte = estilo
        self.quebra_de_linha = quebra_linha
        self.tamanho_tab = recuo
        text.config(font=f'{fonte} {tamanho} {estilo}', wrap=quebra_linha)
        font = Font(font=text['font'])
        tab_size = font.measure(' ' * recuo)
        text.config(tabs=tab_size)
        preferencias = {
            "fonte": fonte,
            "tamanho": tamanho,
            "estilo": estilo,
            "quebra_linha": quebra_linha,
            "recuo": recuo
        }
        with open('config.json', 'w') as config:
            json.dump(preferencias, config, indent=4)
