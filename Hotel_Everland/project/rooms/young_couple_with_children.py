# from Personal_Projects.Hotel_Everland.project.appliances.fridge import Fridge
# from Personal_Projects.Hotel_Everland.project.appliances.laptop import Laptop
# from Personal_Projects.Hotel_Everland.project.appliances.tv import TV
# from Personal_Projects.Hotel_Everland.project.rooms.room import Room
# from Personal_Projects.Hotel_Everland.project.people.child import Child

from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren (Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30
        self.children = [*children]
        self.appliances = [TV().get_monthly_expense(), Fridge().get_monthly_expense(), Laptop().get_monthly_expense()] * self.members_count
        self.children_expenses = [x.cost for x in self.children] * 30
        self.expenses = sum([x for x in self.appliances]) + sum(self.children_expenses)



