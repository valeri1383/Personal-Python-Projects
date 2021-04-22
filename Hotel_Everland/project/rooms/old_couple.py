# from Personal_Projects.Hotel_Everland.project.appliances.fridge import Fridge
# from Personal_Projects.Hotel_Everland.project.appliances.stove import Stove
# from Personal_Projects.Hotel_Everland.project.appliances.tv import TV
# from Personal_Projects.Hotel_Everland.project.rooms.room import Room

from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name,pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV().get_monthly_expense(), Fridge().get_monthly_expense(), Stove().get_monthly_expense()] * 2
        self.expenses = sum([x for x in self.appliances])

