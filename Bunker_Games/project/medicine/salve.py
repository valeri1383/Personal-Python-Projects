#from Personal_Projects.Bunker_Games.project.medicine.medicine import Medicine
from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        super().__init__(50)