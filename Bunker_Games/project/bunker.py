class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supply = [el for el in self.supplies if el.__class__.__name__ == 'FoodSupply']
        if len(food_supply) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supply

    @property
    def water(self):
        water_supply = [el for el in self.supplies if el.__class__.__name__ == 'WaterSupply']
        if len(water_supply) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supply
    
    @property
    def painkillers(self):
        painkiller_supply = [el for el in self.medicine if el.__class__.__name__ == 'Painkiller']
        if len(painkiller_supply) == 0:
            raise IndexError("There are no painkillers left!")
        return painkiller_supply

    @property
    def salves(self):
        salves_list = [el for el in self.medicine if el.__class__.__name__ == 'Salve']
        if len(salves_list) == 0:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                pill = self.painkillers[-1]
                del self.painkillers[-1]
            elif medicine_type == 'Salve':
                pill = self.salves[-1]
                del self.salves[-1]
            pill.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == 'FoodSupply':
                supply = self.supplies[-1]
                del self.supplies[-1]
            elif sustenance_type == 'WaterSupply':
                supply = self.supplies[-1]
                del self.supplies[-1]
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')


