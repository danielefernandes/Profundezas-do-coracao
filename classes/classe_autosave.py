import json


class AutoSave():
    posicao_jogadorX = None
    posicao_jogadorY = None
    tempo_duracao = 0

    def __init__(self, path):
        self.path = path

    def save(self):
        dados = {
            'posicao_jogadorX': self.posicao_jogadorX,
            'posicao_jogadorY': self.posicao_jogadorY,
            'tempo_duracao': self.tempo_duracao
        }
        with open(self.path, 'w') as f:
            json.dump(dados, f)

    def load(self):
        try:
            with open(self.path, 'r') as f:
                dados = json.load(f)
                self.posicao_jogadorX = dados['posicao_jogadorX']
                self.posicao_jogadorY = dados['posicao_jogadorY']
                self.tempo_duracao = dados['tempo_duracao']
                return True
        except FileNotFoundError:
            return False

    def novo_slot(self, path):
        self.path = path
