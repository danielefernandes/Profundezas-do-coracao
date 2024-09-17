import arcade
import math
import time

import arcade.color
from classes.classe_jogador import Jogador
from classes.classe_dialogo import Dialogo
from classes.classes_inimigo import Inimigo


class TelaGame(arcade.View):
    jogador = None
    dialogo = None
    pause = False
    fundos = arcade.SpriteList()

    def __init__(self):
        super().__init__()
        self.jogador = Jogador(
            self.window.auto_save.posicao_jogadorX,
            self.window.auto_save.posicao_jogadorY)

        self.som_fundo = arcade.load_sound(
            './assets/som_fundo.ogg', False)
        self.som_fundo.play(loop=True, speed=0.1, volume=0.2)

        self.sombra = arcade.Sprite('./assets/sombra.png', 0.4)
        self.sombra.center_x = self.jogador.jSprite.center_x - 500
        self.sombra.center_y = self.jogador.jSprite.center_y + 50

        self.lista_cenario = arcade.SpriteList()
        distancia_tile = 250
        for i in range(-50, 50):
            if i % 7 == 0:
                self.lista_cenario.append(
                    arcade.Sprite(
                        "./assets/tile1.png",
                        0.5,
                        center_x=i*distancia_tile,
                        center_y=290)
                )
            else:
                self.lista_cenario.append(
                    arcade.Sprite(
                        "./assets/tile1.png",
                        0.5,
                        center_x=i*distancia_tile,
                        center_y=100)
                )
        self.lista_inimigos = Inimigo()
        distancia_inimigo = 400
        for i in range(10):
            self.lista_inimigos.append(
                        i*distancia_inimigo,
                        50)

        fundo_imagens = (
            "./assets/fundo_game.png",
            "./assets/fundo_game2.png",
            "./assets/fundo_game3.png")

        rise = 40 * 0.9
        for count, image in enumerate(fundo_imagens):
            bottom = rise * (len(fundo_imagens) - count - 1)
            #if count > 0:
            #    bottom +=  350 - (150 * count)
            sprite = arcade.Sprite(image, scale=0.9)
            sprite.bottom = bottom
            sprite.left = 0
            self.fundos.append(sprite)

            sprite = arcade.Sprite(image, scale=0.9)
            sprite.bottom = bottom
            sprite.left = sprite.width
            self.fundos.append(sprite)

        self.jogador.adiciona_fisica(self.lista_cenario)
        self.lista_inimigos.adiciona_fisica(self.lista_cenario)

        self.camera = arcade.Camera(self.window.width, self.window.height)

        #######################
        self.tempo_inicio = time.time()
        self.duracao_tempo_anterior = self.window.auto_save.tempo_duracao

        self.dialogo = Dialogo()

    def on_draw(self):
        arcade.start_render()

        self.duracao_tempo = (time.time()
                              - (self.tempo_inicio +
                                 self.duracao_tempo_anterior))
        minutos = int(self.duracao_tempo // 60)
        segundos = int(self.duracao_tempo % 60)
        tempo_texto = f"Tempo: {minutos:02}:{segundos:02}"

        self.fundos.draw()
        self.lista_cenario.draw()

        # ===================== GUI ========================
        arcade.draw_text(tempo_texto,
                         self.camera.position[0] + self.window.width - 150,
                         self.camera.position[1] + self.window.height - 50,
                         arcade.color.GRAY, 20,
                         anchor_x="center",
                         anchor_y="center")
        arcade.draw_arc_filled(
            self.camera.position[0] + self.window.width/8,
            self.camera.position[1] + self.window.height/1.15,
            150, 150,
            arcade.color.BLUE_GREEN,
            0, self.jogador.vida
        )
        arcade.draw_arc_outline(
            self.camera.position[0] + self.window.width/8,
            self.camera.position[1] + self.window.height/1.15,
            150, 150,
            arcade.color.GRAY,
            0, self.jogador.vidaTotal, 7
        )
        arcade.draw_texture_rectangle(
            self.camera.position[0] + self.window.width/8,
            self.camera.position[1] + self.window.height/1.15,
            200, 200,
            arcade.load_texture(
                "./assets/personagem_avatar.png")
            )

        # ===================== GUI ========================
        self.camera.use()
        self.sombra.draw()
        self.lista_inimigos.draw()
        self.jogador.draw()
        self.dialogo.draw(self.camera.position[0]+self.window.width/4,
                          self.camera.position[1]+50,
                          self.window.width/2,
                          self.window.height/4)

    def on_update(self, delta_time: float):
        self.jogador.update(delta_time)
        self.lista_inimigos.update(delta_time)
        self.update_sombra()
        self.move_camera()

        camera_x = self.camera.position[0]
        for count, sprite in enumerate(self.fundos):
            layer = count // 2
            frame = count % 2
            offset = camera_x / (2 ** (layer + 1))
            jump = (camera_x - offset) // sprite.width
            final_offset = offset + (jump + frame) * sprite.width
            sprite.left = final_offset

    def on_key_press(self, tecla: int, modifiers: int):
        if tecla == arcade.key.A:
            self.media_player = self.jogador.som_andando.play(loop=True)
            self.jogador.jDirecao = -1
            self.jogador.jSprite.change_x = -self.jogador.velocidade_movimento

        if tecla == arcade.key.D:
            self.media_player = self.jogador.som_andando.play(loop=True)
            self.jogador.jDirecao = 1
            self.jogador.jSprite.change_x = self.jogador.velocidade_movimento

        if tecla == arcade.key.W and self.jogador.fisica.can_jump():
            self.jogador.jSprite.change_y = self.jogador.velocidade_pulo

    def on_key_release(self, tecla: int, _modifiers: int):
        if not self.pause:
            if tecla == arcade.key.A or tecla == arcade.key.D:
                self.media_player.pause()
                self.jogador.jSprite.change_x = 0
            if tecla == arcade.key.W or tecla == arcade.key.S:
                self.jogador.jSprite.change_y = 0
            if tecla == arcade.key.ESCAPE:
                self.window.show_view(self.window.tela_menu)
            if tecla == arcade.key.O:
                self.window.auto_save.posicao_jogadorX = (
                    self.jogador.jSprite.center_x)
                self.window.auto_save.posicao_jogadorY = (
                    self.jogador.jSprite.center_y)
                self.window.auto_save.tempo_duracao = self.duracao_tempo

                self.window.auto_save.save()
                print("Jogo salvo com sucesso!")
        if tecla == arcade.key.SPACE:
            self.dialogo.remover_dialogo()
            self.pause = False

    def move_camera(self):
        position = (
            self.jogador.jSprite.center_x - self.camera.viewport_width / 2,
            self.jogador.jSprite.center_y - 200,
        )
        self.camera.move_to(position, speed=0.1)

    def update_sombra(self):
        x = self.jogador.jSprite.center_x
        y = self.jogador.jSprite.center_y
        if self.sombra.collides_with_point((x, y)):
            self.dialogo.incluir_dialogo("Aiii.. senti um arrepio! Acho melhor ir pelo outro lado.")
            self.sombra.update()
            self.jogador.vida -= 10
            self.jogador.jSprite.center_x += 30
            return None

        dx = x - self.sombra.center_x
        dy = y - self.sombra.center_y
        angle = math.atan2(dy, dx)

        if self.jogador.jDirecao < 0:
            self.sombra.alpha = 50  # Transparente
            self.sombra.change_x = 0
            self.sombra.change_y = 0
        else:
            self.sombra.alpha = 255  # Visível
            self.sombra.change_x = math.cos(angle) * 0.5
            self.sombra.change_y = math.sin(angle) * 0.5

        self.sombra.update()
