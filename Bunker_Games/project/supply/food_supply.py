#from Personal_Projects.Bunker_Games.project.supply.supply import Supply
from project.supply.supply import Supply


class FoodSupply(Supply):

    def __init__(self):
        super().__init__(20)

