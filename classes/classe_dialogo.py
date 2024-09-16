import arcade


class Dialogo():
    texto = []
    ativo = False
    fundo = None

    def __init__(self) -> None:
        self.fundo = arcade.load_texture("./assets/fundo_dialogo.png")

    def incluir_dialogo(self, t):
        self.texto.append(t)
        self.ativo = True

    def remover_dialogo(self):
        if len(self.texto) > 0:
            self.texto.pop(0)
            if len(self.texto) == 0:
                self.ativo = False
        else:
            self.ativo = False

    def draw(self, x, y, width, height):
        if self.ativo:
            arcade.draw_lrwh_rectangle_textured(
                x, y,
                width,
                height,
                self.fundo
                )

            arcade.draw_text(
                self.texto[0],
                x+300, y+100,
                arcade.color.BLACK, 15,
                width,
                anchor_x="left",
                anchor_y="baseline"
                )
