class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card_obj):
        try:
            card = [c for c in self.cards if c.name == card_obj.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.cards.append(card_obj)
            self.count += 1

    def remove(self, card_name):
        if card_name == '':
            raise ValueError("Card cannot be an empty string!")
        card = [c for c in self.cards if c.name == card_name][0]
        self.cards.remove(card)
        self.count -= 1

    def find(self, card_name):
        card = [c for c in self.cards if c.name == card_name][0]
        return card
