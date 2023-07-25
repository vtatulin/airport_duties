import unittest
from basic_duties import WDuty, _merge


class TestStringMethods(unittest.TestCase):

    def test_merge_two_inside(self):
        w_duties = [WDuty(start=1, duration=6, display_h=1), WDuty(start=2, duration=1, display_h=1)]
        w_merged = _merge(w_duties)
        self.assertEqual(1, len(w_merged))
        self.assertEqual(1, w_merged[0].start)
        self.assertEqual(6, w_merged[0].duration)

    def test_merge_two_unmergeble(self):
        w_duties = [WDuty(start=1, duration=1, display_h=1),
                    WDuty(start=3, duration=1, display_h=1),
                    WDuty(start=6, duration=1, display_h=1)
                    ]
        w_merged = _merge(w_duties)
        self.assertEqual(3, len(w_merged))

    def test_three_connected(self):
        w_duties = [WDuty(start=1, duration=1, display_h=1),
                    WDuty(start=2, duration=1, display_h=1),
                    WDuty(start=3, duration=1, display_h=1)
                    ]
        w_merged = _merge(w_duties)
        self.assertEqual(1, len(w_merged))
        self.assertEqual(3, w_merged[0].duration)
