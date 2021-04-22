# from Personal_Projects.Hotel_Everland.project.appliances.fridge import Fridge
# from Personal_Projects.Hotel_Everland.project.appliances.laptop import Laptop
# from Personal_Projects.Hotel_Everland.project.appliances.tv import TV
# from Personal_Projects.Hotel_Everland.project.rooms.room import Room

from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV().get_monthly_expense(), Fridge().get_monthly_expense(), Laptop().get_monthly_expense()] * self.members_count
        self.expenses = sum([x for x in self.appliances])
