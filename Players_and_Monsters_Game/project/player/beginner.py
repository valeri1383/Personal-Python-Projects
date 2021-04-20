#from Personal_Projects.Players_and_Monsters_Game.project.player.player import Player
from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super().__init__(username, 50)


