# from Personal_Projects.Players_and_Monsters_Game.project.battle_field import BattleField
# from Personal_Projects.Players_and_Monsters_Game.project.card.card_repository import CardRepository
# from Personal_Projects.Players_and_Monsters_Game.project.card.magic_card import MagicCard
# from Personal_Projects.Players_and_Monsters_Game.project.card.trap_card import TrapCard
# from Personal_Projects.Players_and_Monsters_Game.project.player.advanced import Advanced
# from Personal_Projects.Players_and_Monsters_Game.project.player.beginner import Beginner
# from Personal_Projects.Players_and_Monsters_Game.project.player.player_repository import PlayerRepository

from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.battle_field import BattleField


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.cards_repository = CardRepository()

    def add_player(self, type, username):
        if type == 'Beginner':
            p = Beginner(username)
        elif type == 'Advanced':
            p = Advanced(username)
        self.player_repository.add(p)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == 'Magic':
            c = MagicCard(name)
        elif type == 'Trap':
            c = TrapCard(name)
        self.cards_repository.add(c)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        card = self.cards_repository.find(card_name)
        user = self.player_repository.find(username)
        user.card_repositoy.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        battle_field = BattleField()
        battle_field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        text = ''
        for p in self.player_repository.players:
            text += f'Username: {p.username} - Health: {p.health} - Cards {p.card_repository.count}\n'
            for c in p.card_repository:
                text += f'Card: {c.name} - Damage: {c.damage_points}'
        return text
