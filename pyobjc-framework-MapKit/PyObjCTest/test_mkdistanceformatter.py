from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKDistanceFormatter(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(MapKit.MKDistanceFormatterUnitsDefault, 0)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsMetric, 1)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsImperial, 2)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsImperialWithYards, 3)

        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleDefault, 0)
        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleAbbreviated, 1)
        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleFull, 2)
