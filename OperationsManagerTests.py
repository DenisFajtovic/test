import unittest
from unittest.mock import patch
from Dodatak_A import OperationsManager

class OperationsManagerTests(unittest.TestCase):

    def test_perform_division(self):
        manager = OperationsManager(20, 2)
        result = manager.perform_division()
        self.assertEqual(result, 10)

    def test_perform_division_by_zero(self):
        manager = OperationsManager(10, 0)
        result = manager.perform_division()
        self.assertEqual(result, float('nan'))

    def test_perform_division_with_zero(self):
        manager = OperationsManager(0, 10)
        result = manager.perform_division()
        self.assertEqual(result, 0)

    def test_perform_division_with_string(self):
        manager = OperationsManager("ananas", 8)
        #result = manager.perform_division()
        self.assertRaises(TypeError, manager.perform_division)

    def test_perform_division_by_string(self):
        manager = OperationsManager(8, "ananas")
        #result = manager.perform_division()
        self.assertRaises(TypeError, manager.perform_division)

    def test_perform_division_string_by_string(self):
        manager = OperationsManager("keks", "ananas")
        #result = manager.perform_division()
        self.assertRaises(TypeError, manager.perform_division)


if __name__ == '__main__':
    unittest.main()