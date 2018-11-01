from unittest import TestCase
from countingValleys import countingValleys


class TestCountingValleys(TestCase):
    def test_zero_valley(self):
        self.assertEqual(countingValleys(10, "UDUUUDUDDD"), 0)

    def test_one_valley(self):
        self.assertEqual(countingValleys(10, "DDUDDUUDUU"), 1)
        self.assertEqual(countingValleys(8, "UDDDUDUU"), 1)

    def test_two_valleys(self):
        self.assertEqual(countingValleys(12, "DDUUUUDDDDUU"), 2)
