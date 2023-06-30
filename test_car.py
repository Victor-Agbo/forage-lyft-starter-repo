import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindle_battery import SpindleBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCapulet(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 300001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 6000010
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())


class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(last_service_date)
        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(last_service_date)
        self.assertFalse(car.needs_service())


class TestSpindle(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        car = SpindleBattery(last_service_date)
        self.assertTrue(car.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SpindleBattery(last_service_date)
        self.assertFalse(car.needs_service())


class TestCarrigan(unittest.TestCase):
    def test_wrong_array_size(self):
        self.assertRaises(IndexError, CarriganTire, [1, 1, 1, 1, 1])

    def test_wrong_array_input(self):
        self.assertRaises(ValueError, CarriganTire, [1, 1, 1.1, 1])

    def test_needs_service_true(self):
        tire = CarriganTire([0.8, 0.9, 0.8, 1])
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_false(self):
        tire = CarriganTire([0.8, 0.89, 0.8, 0.4])
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_wrong_array_size(self):
        self.assertRaises(IndexError, OctoprimeTire, [1, 1, 1, 1, 1])

    def test_wrong_array_input(self):
        self.assertRaises(ValueError, OctoprimeTire, [1, 1, 1.1, 1])

    def test_needs_service_true(self):
        tire = OctoprimeTire([0.8, 0.9, 0.8, 1])
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_false(self):
        tire = OctoprimeTire([0.8, 0.89, 0.8, 0.4])
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
