#from Personal_Projects.Players_and_Monsters_Game.project.card.card import Card
from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        super().__init__(name, 5, 80)
