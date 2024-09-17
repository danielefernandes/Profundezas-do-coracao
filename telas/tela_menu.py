import arcade
from telas.tela_game import TelaGame


class TelaMenu(arcade.View):
    botao_iniciar = None

    def __init__(self):
        super().__init__()
        self.fundo = arcade.load_texture("./assets/fundo_menu.png")

        self.botao_iniciar = arcade.Sprite(
            "./assets/botao_1.png",
            0.1,
            center_x=self.window.width/4,
            center_y=self.window.height/2)
        
        self.botao_continue = arcade.Sprite(
            "./assets/botao_2.png",
            0.1,
            center_x=self.window.width/4,
            center_y=self.window.height/2 - 50)
        
        self.botao_config = arcade.Sprite(
            "./assets/botao_3.png",
            0.1,
            center_x=self.window.width/4,
            center_y=self.window.height/2 - 100)
        
        self.botao_sobre = arcade.Sprite(
            "./assets/botao_4.png",
            0.1,
            center_x=self.window.width/4,
            center_y=self.window.height/2 - 150)

        self.camera = arcade.Camera(self.window.width, self.window.height)

    def on_draw(self):
        arcade.start_render()
        self.camera.use()
        arcade.draw_lrwh_rectangle_textured(
                0, 0,
                self.window.width,
                self.window.height,
                self.fundo,
                )
        self.botao_iniciar.draw()
        self.botao_continue.draw()
        self.botao_config.draw()
        self.botao_sobre.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.botao_iniciar.collides_with_point((x, y)):
            t2 = TelaGame()
            self.window.show_view(t2)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.botao_iniciar.collides_with_point((x, y)):
            self.botao_iniciar = arcade.Sprite(
                "./assets/botao_1s.png",
                0.1,
                center_x=self.window.width/4,
                center_y=self.window.height/2)
        else:
            self.botao_iniciar = arcade.Sprite(
                "./assets/botao_1.png",
                0.1,
                center_x=self.window.width/4,
                center_y=self.window.height/2)