from unittest import TestCase
from saveThePrisoner import saveThePrisoner


class TestSaveThePrisoner(TestCase):
    def test_aswer(self):
        testCase = {
            "144 797951344 1": 112,
            "78 631228415 77": 75,
            "14 828540146 13": 12,
            "17 900306316 1": 1,
            "999999998 199360437 1": 199360437,
            "91 111224659 1": 91,
            "999999998 999999997 1": 999999997,
            "5 815446299 4": 2,
            "169 647839529 169": 167,
            "15 855047220 12": 11,
            "12 276834827 2": 12,
            "43 476872149 17": 15, "105 468562081 105": 105,
            "457 359999921 457": 455,
            "764720478 764720478 764720477": 764720476
        }

        for k in testCase.keys():
            n, m, s = k.split()
            n = int(n)
            m = int(m)
            s = int(s)
            self.assertEqual(testCase[k], saveThePrisoner(n, m, s))
