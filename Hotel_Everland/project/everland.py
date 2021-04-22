class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        room_cost = sum([x.room_cost for x in self.rooms])
        expenses = sum([x.expenses for x in self.rooms])
        return f"Monthly consumption: {(room_cost + expenses):.2f}$."

    def pay(self):
        result = ''
        for idx, x in enumerate(self.rooms):
            if x.budget >= x.room_cost:
                result += f"{x.family_name} paid {(x.expenses + x.room_cost):.2f}$ and have {x.budget:.2f}$ left."
                x.budget -= x.expenses + x.room_cost
            else:
                result += f"{x.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(x)
            if idx < len(self.rooms) - 1:
                result += '\n'
        return result

    def status(self):
        result = f'Total population: {sum(x.members_count for x in self.rooms)}\n'
        for x in self.rooms:
            result += f'{x.family_name} with {x.members_count} members. Budget: {x.budget:.2f}$, Expenses: {x.expenses:.2f}$\n'
            if len(x.children) > 0:
                for idx, c in enumerate(x.children):
                    result += f"--- Child {idx + 1} monthly cost: {(c.cost * 30):.2f}$\n"
            result += f'--- Appliances monthly cost: {sum(x.appliances):.2f}$\n'
        return result

