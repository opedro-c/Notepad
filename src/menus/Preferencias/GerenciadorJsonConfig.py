import os
import json


class GerenciadorJsonConfig:


    @classmethod
    def criar_json_config(cls) -> None:
        if not os.path.isdir('.config'):
            os.mkdir('.config')
        os.chdir('.config')
        if not os.path.isfile('Notepad_preferences.json'):
            with open('Notepad_preferences.json', 'w') as config:
                preferencias = {
                    "fonte": "Arial",
                    "tamanho": "12",
                    "estilo": "",
                    "quebra_linha": "none",
                    "recuo": 4
                }
                json.dump(preferencias, config)
        os.chdir('..')   

    @classmethod
    def conteudo_json_config(cls) -> dict:
        os.chdir('.config')
        with open('Notepad_preferences.json', 'r') as config:
            os.chdir('..')
            return json.load(config)

    @classmethod
    def gravar_json_config(cls, conteudo: dict) -> None:
        os.chdir('.config')
        with open('Notepad_preferences.json', 'w') as config:
            json.dump(conteudo, config, indent=4)
            os.chdir('..')
