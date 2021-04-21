from Personal_Projects.System_Split.project.software.light_software import LightSoftware


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.capacity >= software.capacity_consumption and self.memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        self.software_components.remove(software)

    def length(self):
        return len(self.software_components)





