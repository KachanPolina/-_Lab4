import unittest
from lab5 import calculate_nights_total, add_city_tax


class hotel_accommodation_cost(unittest.TestCase):
    def test_calculate_nights_total(self):
        self.assertEqual(calculate_nights_total(5, 500), 5 * 500)
        self.assertEqual(calculate_nights_total(7, 265.12), 7 * 265.12)

    def test_calculate_nights_total_negative(self):
        self.assertEqual(calculate_nights_total(0, 500), 0)
        self.assertEqual(calculate_nights_total(12, 0), 0)
        self.assertEqual(calculate_nights_total(0, 0), 0)

    def test_add_city_tax(self):
        self.assertEqual(add_city_tax(5, 500, 200), 5 * 500 + 200)
        self.assertEqual(add_city_tax(7, 265.12, 800), 7 * 265.12 + 800)
        self.assertEqual(add_city_tax(1, 654, 20), 1 * 654 + 20)
        self.assertEqual(add_city_tax(2, 100, 10), 2 * 100 + 10)
        self.assertEqual(add_city_tax(3, 200, 0), 3 * 200 + 0)

    def test_add_city_tax_negative(self):
        self.assertEqual(calculate_nights_total(0, 200), 0)


if __name__ == "__main__":
    unittest.main()
