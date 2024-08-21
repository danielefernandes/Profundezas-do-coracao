import arcade
import time

class TelaGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.som_jogador_andando = arcade.load_sound('./assets/som_jogador_caminhando.ogg',False)
        self.jogador_sprite = arcade.AnimatedWalkingSprite()

        for i in range(2):
            self.jogador_sprite.walk_left_textures.append(
                arcade.load_texture(f"./assets/personagem_{i}.png", flipped_horizontally=True)
            )
            self.jogador_sprite.walk_right_textures.append(
                arcade.load_texture(f"./assets/personagem_{i}.png")
            )
        self.jogador_sprite.stand_right_textures.append(arcade.load_texture(f"./assets/personagem_idle.png"))
        self.jogador_sprite.stand_left_textures.append(arcade.load_texture(f"./assets/personagem_idle.png", flipped_horizontally=True))
        self.jogador_sprite.scale = 0.5

        if self.window.auto_save.posicao_jogadorX != None and self.window.auto_save.posicao_jogadorX!= None:
            self.jogador_sprite.center_x = self.window.auto_save.posicao_jogadorX
            self.jogador_sprite.center_y = self.window.auto_save.posicao_jogadorY
        else:
            self.jogador_sprite.center_x = 50
            self.jogador_sprite.center_y = 100

        self.jogador = arcade.SpriteList()
        self.jogador.append(self.jogador_sprite)
        self.velocidade_movimento = 3
        self.velocidade_pulo = 8

        self.lista_cenario = arcade.SpriteList()
        distancia_tile = 50
        for i in range(-50,50):
            self.lista_cenario.append(
                arcade.Sprite(
                    "./assets/tile1.png",
                    0.5,
                    center_x=i*distancia_tile,
                    center_y=50)
            )

        self.fundo = arcade.Sprite(
            "./assets/fundo_game.png",
            0.75,
            center_x=self.window.width/2,
            center_y=self.window.height/2)

        self.fisica = arcade.PhysicsEnginePlatformer(self.jogador_sprite, self.lista_cenario)


        #######################
        self.tempo_inicio = time.time()
        self.duracao_tempo_anterior = self.window.auto_save.tempo_duracao

        
    def on_draw(self):
        arcade.start_render()

        self.duracao_tempo = time.time() - self.tempo_inicio + self.duracao_tempo_anterior
        minutos = int(self.duracao_tempo // 60)
        segundos = int(self.duracao_tempo % 60)
        tempo_texto = f"Tempo: {minutos:02}:{segundos:02}"

        self.lista_cenario.draw()
        self.fundo.draw()

        arcade.draw_text(tempo_texto, self.window.width - 150, self.window.height - 30,
                         arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

        self.jogador.draw()


    def on_update(self, delta_time: float):
        self.jogador.update_animation(delta_time)
        self.jogador_sprite.update()
        self.fisica.update()

    def on_key_press(self, tecla: int, modifiers: int):
        #identificar as teclas e gerar uma ação
        if tecla == arcade.key.A:
            self.media_player = self.som_jogador_andando.play(loop=True)
            self.jogador_sprite.change_x = -self.velocidade_movimento

        if tecla == arcade.key.D:
            self.media_player = self.som_jogador_andando.play(loop=True)
            self.jogador_sprite.change_x = self.velocidade_movimento

        if tecla == arcade.key.W and self.fisica.can_jump():
            self.jogador_sprite.change_y = self.velocidade_pulo
        
        

    def on_key_release(self, tecla: int, _modifiers: int):
        if tecla == arcade.key.A or tecla == arcade.key.D:
            self.media_player.pause()
            self.jogador_sprite.change_x = 0
        if tecla == arcade.key.W or tecla == arcade.key.S:
            self.jogador_sprite.change_y = 0
        if tecla == arcade.key.ESCAPE:
            self.window.show_view(self.window.tela_menu)
        if tecla == arcade.key.O:
            self.window.auto_save.posicao_jogadorX = self.jogador_sprite.center_x
            self.window.auto_save.posicao_jogadorY = self.jogador_sprite.center_y
            self.window.auto_save.tempo_duracao = self.duracao_tempo

            self.window.auto_save.save()
            print("Jogo salvo com sucesso!")