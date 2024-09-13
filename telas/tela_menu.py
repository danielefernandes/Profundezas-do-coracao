import arcade
from telas.tela_game import TelaGame


class TelaMenu(arcade.View):
    botao_iniciar = None

    def __init__(self):
        super().__init__()
        self.fundo = arcade.Sprite(
            "./assets/fundo_menu.png",
            0.75,
            center_x=self.window.width/2,
            center_y=self.window.height/2)
        self.botao_iniciar = arcade.Sprite(
            "./assets/botao_start.png",
            0.4,
            center_x=self.window.width/2 - 10,
            center_y=self.window.height/2 - 30)

        self.camera = arcade.Camera(self.window.width, self.window.height)

    def on_draw(self):
        arcade.start_render()
        self.camera.use()
        self.fundo.draw()
        self.botao_iniciar.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.botao_iniciar.collides_with_point((x, y)):
            # se houver colisão com o botão iniciar
            t2 = TelaGame()
            self.window.show_view(t2)
