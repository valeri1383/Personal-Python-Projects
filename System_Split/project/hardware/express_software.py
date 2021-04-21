#from Personal_Projects.System_Split.project.software.software import Software
from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, 'Express', capacity_consumption, int(memory_consumption * 2))


