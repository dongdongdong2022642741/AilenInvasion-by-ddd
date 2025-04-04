class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed=1.5
        self.ship_limit= 3
        self.alien_speed=20
        self.fleet_drop_speed=10
        self.fleet_direction=1
        self.bullet_speed=2.5
        self.bullet_width=10
        self.bullet_height=30
        self.bullet_color=(60,60,60)
        self.bullet_allowd=3
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed=1.5
        self.bullet_speed=2.5
        self.alien_speed=3
        self.fleet_direction=1
        self.alien_point= 50

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_point=int(self.alien_point * self.score_scale)

        

