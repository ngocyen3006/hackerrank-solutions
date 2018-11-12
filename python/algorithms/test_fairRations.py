from unittest import TestCase
from fairRations import fairRations

with open("fairRations.txt") as file:
    B = list(map(int, file.readline().split()))


class TestFairRations(TestCase):
    def test_output_is_NO(self):
        self.assertEqual("NO", fairRations([1, 2]))

    def test_N_lesser_Ten(self):
        self.assertEqual(4, fairRations([4, 5, 6, 7]))
        self.assertEqual(4, fairRations([2, 3, 4, 5, 6]))

    def test_N_is_large(self):
        self.assertEqual(970, fairRations(B))
