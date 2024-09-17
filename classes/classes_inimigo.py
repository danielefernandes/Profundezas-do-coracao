import arcade


class Inimigo(arcade.Sprite):
    s = None

    def __init__(self):
        self.velocidade_movimento = 3
        self.s = arcade.SpriteList()

    def append(self, x, y):
        sprite = arcade.Sprite(
                            "./assets/inimigo1.png",
                            0.5,
                            center_x=x,
                            center_y=y)

        self.s.append(sprite)

    def adiciona_fisica(self, lista_obstaculos):
        for s in self.s:
            self.fisica = arcade.PhysicsEnginePlatformer(
                s, lista_obstaculos
                )

    def update(self, delta_time):
        for s in self.s:
            if delta_time % 1000 == 0:
                self.velocidade_movimento *= -1
            s.change_x = self.velocidade_movimento
            s.change_y = self.velocidade_movimento

    def draw(self):
        self.s.draw()
