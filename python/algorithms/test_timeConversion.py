from unittest import TestCase
from timeConversion import timeConversion


class TestTimeConversion(TestCase):
    def test_input_is_midnight(self):
        self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")
        self.assertEqual(timeConversion("12:05:15AM"), "00:05:15")

    def test_input_is_the_morning(self):
        self.assertEqual(timeConversion("10:00:00AM"), "10:00:00")
        self.assertEqual(timeConversion("11:50:00AM"), "11:50:00")

    def test_input_is_midday(self):
        self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")

    def test_input_is_noon(self):
        self.assertEqual(timeConversion("01:00:00PM"), "13:00:00")
        self.assertEqual(timeConversion("11:00:00PM"), "23:00:00")
