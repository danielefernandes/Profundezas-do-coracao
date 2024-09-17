import arcade


class Poder(arcade.Sprite):
    def __init__(self):
        super().__init__(
            "./assets/",
            scale=0.1,
        )

    def on_update(self, delta_time: float = 1 / 60):
        self.position = (
            self.center_x + self.change_x * delta_time,
            self.center_y + self.change_y * delta_time,
        )
