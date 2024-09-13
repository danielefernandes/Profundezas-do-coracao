import arcade


class Jogador():
    j = None
    jSprite = None
    jDirecao = None
    velocidade_pulo = None
    velocidade_movimento = None
    som_andando = None
    fisica = None

    def __init__(self, load_posicao_X, load_posicao_Y):
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
        self.jSprite.scale = 0.5
        self.jDirecao = 1

        if (load_posicao_X is not None and
                load_posicao_Y is not None):
            self.jSprite.center_x = load_posicao_X
            self.jSprite.center_y = load_posicao_Y
        else:
            self.jSprite.center_x = 50
            self.jSprite.center_y = 100

        self.j = arcade.SpriteList()
        self.j.append(self.jSprite)
        self.velocidade_movimento = 3
        self.velocidade_pulo = 8

    def adiciona_fisica(self, lista_obstaculos):
        self.fisica = arcade.PhysicsEnginePlatformer(
            self.jSprite, lista_obstaculos
            )

    def update(self, delta_time):
        self.j.update_animation(delta_time)
        self.jSprite.update()
        self.fisica.update()

    def draw(self):
        self.j.draw()
