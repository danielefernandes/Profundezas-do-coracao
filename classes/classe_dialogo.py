import arcade


class Dialogo():
    texto = []
    ativo = False
    fundo = None

    def __init__(self) -> None:
        self.fundo = arcade.load_texture("./assets/fundo_game.png")

    def incluir_dialogo(self, t):
        self.texto.appedn(t)
        self.ativo = True

    def remove_dialogo(self):
        if self.texto.count() > 0:
            self.texto.pop(0)
        else:
            self.ativo = False

    def draw_dialogo(self, x, y, width, height):
        if self.ativo:
            arcade.draw_lrwh_rectangle_textured(
                x, y,
                width,
                height,
                self.fundo
                )

            arcade.draw_text(
                self.texto[0],
                x, y,
                arcade.color.BLACK, 20,
                anchor_x="center",
                anchor_y="center"
                )
