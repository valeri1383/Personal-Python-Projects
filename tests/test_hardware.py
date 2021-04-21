import unittest

# from Personal_Projects.System_Split.project.hardware.hardware import Hardware
# from Personal_Projects.System_Split.project.software.light_software import LightSoftware

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):

    def test_set_attr(self):
        hardware = Hardware('test', 'SSD', 512, 16)
        self.assertEqual(hardware.name, 'test')
        self.assertEqual(hardware.type, 'SSD')
        self.assertEqual(hardware.capacity, 512)
        self.assertEqual(hardware.memory, 16)

    def test_install_soft_raise_ex_when_capacity_or_memory_not_enough(self):
        with self.assertRaises(Exception) as ex:
            hardware = Hardware('test', 'SSD', 512, 16)
            software = LightSoftware('test', 550, 20)
            hardware.install(software)

        self.assertIsNotNone(ex.exception)

    def test_install_soft_when_capacity_or_memory_enough(self):
        hardware = Hardware('test', 'SSD', 512, 16)
        software = LightSoftware('test', 10, 5)
        hardware.install(software)
        self.assertEqual(len(hardware.software_components), 1)

    def test_uninstall_method(self):
        hardware = Hardware('test', 'SSD', 512, 16)
        software = LightSoftware('test', 10, 5)
        hardware.install(software)
        self.assertEqual(len(hardware.software_components), 1)
        hardware.uninstall(software)
        self.assertEqual(len(hardware.software_components), 0)

