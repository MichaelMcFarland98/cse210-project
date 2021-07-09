import arcade
from game.player import Player

class Output_service:

    def __init__(self):
        self.HEALTHBAR_HEIGHT = 10
        self.HEALTHBAR_WIDTH = 70
        # self.player_max_hp = player.get_health()

    def execute(self, actors):
        players = actors['player'][0]
        zombies = actors['zombie'][0] 
        walls = actors['wall'][0]
        obsticals = actors['obsticals'][0]
        

        
        for player in players:
            player.draw()
        for zombie in zombies:
            zombie.draw()
        for wall in walls:
            wall.draw() 
        for obstical in obsticals:
            obstical.draw()
    
        
        arcade.draw_text(f"Score: {player.get_score()}", 10, 630, arcade.color.WHITE, 14)

        # This code displays the health bar in the bottom left.
        self.player_max_hp = player.get_max_health()

        health_width = self.HEALTHBAR_WIDTH * (player.get_health() / self.player_max_hp)

        if player.get_health() < self.player_max_hp:
            arcade.draw_rectangle_filled(50, 20, width=self.HEALTHBAR_WIDTH, height=self.HEALTHBAR_HEIGHT, color=arcade.color.RED)

        arcade.draw_rectangle_filled(50, 20, width=health_width, height=self.HEALTHBAR_HEIGHT, color=arcade.color.GREEN)