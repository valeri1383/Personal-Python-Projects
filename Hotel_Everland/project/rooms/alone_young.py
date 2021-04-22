# from Personal_Projects.Hotel_Everland.project.appliances.tv import TV
# from Personal_Projects.Hotel_Everland.project.rooms.room import Room

from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV().get_monthly_expense()]