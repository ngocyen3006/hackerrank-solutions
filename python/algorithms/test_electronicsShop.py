from unittest import TestCase
from electronicsShop import getMoneySpent


class TestGetMoneySpent(TestCase):
    def test_result_greater_than_zero(self):
        self.assertEqual(getMoneySpent([3, 1], [5, 2, 8], 10), 9)

    def test_result_lesser_than_zero(self):
        self.assertEqual(getMoneySpent([4], [5], 5), -1)
