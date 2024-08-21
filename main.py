import arcade
from telas.tela_menu import TelaMenu
from classes.classe_autosave import AutoSave

class Janela(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "Profundezas do Coração")
        self.tela_menu = TelaMenu()
        self.show_view(self.tela_menu)
        self.auto_save = AutoSave("./save/slot0.json")
        if self.auto_save.load():
            print("Jogo carregado com sucesso!")

def main():
    Janela()
    arcade.run()

if __name__ == "__main__":
    main()