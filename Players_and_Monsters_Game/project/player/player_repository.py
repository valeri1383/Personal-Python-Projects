#from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player_obj):
        try:
            player = [p for p in self.players if p.username == player_obj.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            self.players.append(player_obj)
            self.count += 1

    def remove(self, player_name):
        if player_name == '':
            raise ValueError("Player cannot be an empty string!")
        player = [p for p in self.players if p.username == player_name][0]
        self.players.remove(player)
        self.count -= 1

    def find(self, player_name):
        player = [p for p in self.players if p.username == player_name][0]
        return player




