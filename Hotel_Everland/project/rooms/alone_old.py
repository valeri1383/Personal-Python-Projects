#from Personal_Projects.Hotel_Everland.project.rooms.room import Room
from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, 1)

