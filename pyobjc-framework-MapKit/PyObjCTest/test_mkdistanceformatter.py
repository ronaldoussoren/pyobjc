from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKDistanceFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MapKit.MKDistanceFormatterUnitStyle)
        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleDefault, 0)
        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleAbbreviated, 1)
        self.assertEqual(MapKit.MKDistanceFormatterUnitStyleFull, 2)

        self.assertIsEnumType(MapKit.MKDistanceFormatterUnits)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsDefault, 0)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsMetric, 1)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsImperial, 2)
        self.assertEqual(MapKit.MKDistanceFormatterUnitsImperialWithYards, 3)
