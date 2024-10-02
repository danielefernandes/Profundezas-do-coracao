import arcade
#from telas.tela_game import TelaGame

class TelaGameover(arcade.View):

    def __init__(self):
        super().__init__()

        self.fundo = arcade.load_texture("./assets/fundo_menu.png")
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.titulo = arcade.Text("GAME OVER", 
                                  0, self.window.height/2,
                                  align="center",
                                  width=self.window.width,
                                  font_size=24)
        self.texturas_botao_normal = [
            arcade.load_texture("./assets/botao_1.png"),
            arcade.load_texture("./assets/botao_2.png"),
            arcade.load_texture("./assets/botao_3.png"),
            arcade.load_texture("./assets/botao_4.png")
        ]

        self.texturas_botao_selecionado = [
            arcade.load_texture("./assets/botao_1s.png"),
            arcade.load_texture("./assets/botao_2s.png"),
            arcade.load_texture("./assets/botao_3s.png"),
            arcade.load_texture("./assets/botao_4s.png")
        ]

        self.botoes = []
        for i in range(4):
            botao = arcade.Sprite(
                self.texturas_botao_normal[i].name,
                0.1,
                center_x=self.window.width / 4,
                center_y=self.window.height / 2 - i * 50 
            )
            if i==1 and self.window.jogoCarregado:
                botao.alpha = 255
            elif i==1:
                botao.alpha = 100
            self.botoes.append(botao)

    def on_draw(self):
        arcade.start_render()
        self.camera.use()

        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            self.window.width,
            self.window.height,
            self.fundo
        )

        for botao in self.botoes:
            botao.draw()

        self.titulo.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for index, botao in enumerate(self.botoes):
            if botao.collides_with_point((x, y)):
                if index == 0:
                    t2 = TelaGame()
                    self.window.show_view(t2)
                if index == 1 and self.window.jogoCarregado:
                    t2 = TelaGame(carregaConteudo = True)
                    self.window.show_view(t2)
                if index == 3:
                    arcade.close_window()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        for i, botao in enumerate(self.botoes):
            if botao.collides_with_point((x, y)):
                if i != 1:
                    botao.texture = self.texturas_botao_selecionado[i]
                elif self.window.jogoCarregado:
                    botao.texture = self.texturas_botao_selecionado[i]
                else:
                    botao.alpha = 100
            else:
                botao.texture = self.texturas_botao_normal[i]