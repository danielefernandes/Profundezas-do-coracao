import arcade
from telas.tela_menu import TelaMenu

def main():
    janela = arcade.Window(title="Meu Jogo",
                           width=800,
                           height=800
                           )
    
    t1 = TelaMenu()
    janela.show_view(t1)

    arcade.run()

if __name__ == "__main__":
    main()