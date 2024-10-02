import arcade


class Jogador():
    j = None
    jSprite = None
    jDirecao = None
    velocidade_pulo = None
    velocidade_movimento = None
    som_andando = None
    fisica = None
    vida = 100
    vidaTotal = 100

    def __init__(self, load_posicao_X=500, load_posicao_Y=100):
        self.som_andando = arcade.load_sound(
            './assets/som_jogador_caminhando.ogg', False)
        self.jSprite = arcade.AnimatedWalkingSprite()

        for i in range(2):
            self.jSprite.walk_left_textures.append(
                arcade.load_texture(f"./assets/personagem_{i}.png",
                                    flipped_horizontally=True)
            )
            self.jSprite.walk_right_textures.append(
                arcade.load_texture(f"./assets/personagem_{i}.png")
            )
        self.jSprite.stand_right_textures.append(
            arcade.load_texture("./assets/personagem_idle.png")
            )
        self.jSprite.stand_left_textures.append(
            arcade.load_texture("./assets/personagem_idle.png",
                                flipped_horizontally=True)
                                )
        self.jSprite.scale = 0.4
        self.jDirecao = 1

        self.jSprite.center_x = load_posicao_X
        self.jSprite.center_y = load_posicao_Y

        self.j = arcade.SpriteList()
        self.j.append(self.jSprite)
        self.velocidade_movimento = 3
        self.velocidade_pulo = 10

    def adiciona_fisica(self, lista_obstaculos):
        self.fisica = arcade.PhysicsEnginePlatformer(
            self.jSprite, lista_obstaculos
            )

    def update(self, delta_time, inimigos):
        self.j.update_animation(delta_time)
        self.jSprite.update()
        self.fisica.update()
        for i, s in enumerate(inimigos):
            if self.jSprite.collides_with_point((s.center_x, s.center_y)):
                self.vida -= 10

    def draw(self):
        self.j.draw()
