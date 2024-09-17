import arcade
from telas.tela_menu import TelaMenu
from classes.classe_autosave import AutoSave


class Janela(arcade.Window):
    jogoCarregado = None
    def __init__(self):
        super().__init__(800, 800, "Profundezas do Coração", True)
        self.tela_menu = TelaMenu()
        self.show_view(self.tela_menu)
        self.auto_save = AutoSave("./save/slot0.json")
        self.jogoCarregado = self.auto_save.load()
        if self.jogoCarregado:
            print("Jogo carregado com sucesso!")


def main():
    Janela()
    arcade.run()


if __name__ == "__main__":
    main()
