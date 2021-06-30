from tkinter import *
from tkinter.font import Font
from .gui_preferencias import montar_preferencias
from .GerenciadorJsonConfig import GerenciadorJsonConfig as gjc


class Preferencias:


    def __init__(self, text: Text) -> None:
        gjc.criar_json_config()
        self.__preferencias = gjc.conteudo_json_config()
        self.aplicar_preferencias(
            text, self.preferencias["fonte"], self.preferencias['tamanho'], self.preferencias['estilo'], 
            self.preferencias['quebra_linha'], self.preferencias['recuo']
        )

    def executar(self, root, text) -> None:
        self.__gui_pref = Toplevel(root, bg='white')
        montar_preferencias(self.gui_pref, text, self.preferencias, self.aplicar_preferencias)

    @property
    def gui_pref(self) -> Toplevel:
        return self.__gui_pref

    @property
    def preferencias(self) -> dict:
        return self.__preferencias
    
    @preferencias.setter
    def preferencias(self, novas_preferencias) -> None:
        self.__preferencias = novas_preferencias

    def aplicar_preferencias(self, text: Text, fonte: str, tamanho: str, estilo: str, quebra_linha: str, recuo: int) -> None:
        self.preferencias = {
            "fonte": fonte,
            "tamanho": tamanho,
            "estilo": estilo,
            "quebra_linha": quebra_linha,
            "recuo": recuo
        }
        text.config(
            font=f'{self.preferencias["fonte"]} ' + 
            f'{self.preferencias["tamanho"]} ' + 
            f'{self.preferencias["estilo"]}', 
            wrap=self.preferencias["quebra_linha"]
            )
        font = Font(font=text['font'])
        tab_size = font.measure(' ' * self.preferencias['recuo'])
        text.config(tabs=tab_size)
        gjc.gravar_json_config(self.preferencias)
        
