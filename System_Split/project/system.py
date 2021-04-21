# from Personal_Projects.System_Split.project.hardware.hardware import Hardware
# from Personal_Projects.System_Split.project.hardware.heavy_hardware import HeavyHardware
# from Personal_Projects.System_Split.project.hardware.power_hardware import PowerHardware
# from Personal_Projects.System_Split.project.software.express_software import ExpressSoftware
# from Personal_Projects.System_Split.project.software.light_software import LightSoftware


from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception:
            return Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception:
            return Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [x for x in System._hardware if x.name == hardware_name][0]
        software = [x for x in System._software if x.name == software_name][0]
        if hardware != [] and software != []:
            hardware.uninstall(software)
        else:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System()._hardware)}\n'
        result += f'Software Components: {len(System()._software)}\n'
        result += f'Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}\n'
        result += f'Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n'
            result += f'Express Software Components: {len([x for x in hardware.software_components if x.type == "Express"])}\n'
            result += f'Light Software Components: {len([x for x in hardware.software_components if x.type == "Light"])}\n'
            result += f'Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}\n'
            result += f'Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}\n'
            result += f'Type: {hardware.type}\n'
            result += f'Software Components: {", ".join([x.name for x in hardware.software_components])}\n'
        return result
