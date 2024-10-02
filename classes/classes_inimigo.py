import arcade


class Inimigo(arcade.Sprite):
    s = None
    fisica = []
    lista_obstaculos = []
    def __init__(self):
        self.velocidade_movimento = 2
        self.s = arcade.SpriteList()
        self.tempo = 0
        

    def append(self, x, y):
        sprite = arcade.Sprite(
                            "./assets/inimigo1.png",
                            0.5,
                            center_x=x,
                            center_y=y)
        self.s.append(sprite)

    def adiciona_fisica(self, lista_obstaculos):
        self.lista_obstaculos = lista_obstaculos
        for s in self.s:
            self.fisica.append(arcade.PhysicsEnginePlatformer(
                s, lista_obstaculos
                ))

    def update(self, grito):
        if self.tempo % 100 == 0:
            self.velocidade_movimento *= -1
            self.tempo = 0
        self.tempo += 1

        for i,s in enumerate(self.s):
            self.s[i].change_x = self.velocidade_movimento
            self.s[i].change_y = 0
            self.fisica[i].update()

            if self.s[i].center_y < -200:
                self.novo_inimigo(i, s)

            if len(grito) > 0:
                if grito[0].collides_with_point((s.center_x+50, s.center_y)) or grito[0].collides_with_point((s.center_x-50, s.center_y)):
                    self.novo_inimigo(i, s)
                
        self.s.update()
        

    def draw(self):
        self.s.draw()

    def novo_inimigo(self, i, s):
        self.s.pop(i)
        self.fisica.pop(i)
        self.append(s.center_x + 700,  s.center_y+200)
        self.fisica.append(arcade.PhysicsEnginePlatformer(
            self.s[-1], self.lista_obstaculos
            ))