import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLengthFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSLengthFormatterUnit)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSLengthFormatterUnitMillimeter, 8)
        self.assertEqual(Foundation.NSLengthFormatterUnitCentimeter, 9)
        self.assertEqual(Foundation.NSLengthFormatterUnitMeter, 11)
        self.assertEqual(Foundation.NSLengthFormatterUnitKilometer, 14)
        self.assertEqual(Foundation.NSLengthFormatterUnitInch, (5 << 8) + 1)
        self.assertEqual(Foundation.NSLengthFormatterUnitFoot, (5 << 8) + 2)
        self.assertEqual(Foundation.NSLengthFormatterUnitYard, (5 << 8) + 3)
        self.assertEqual(Foundation.NSLengthFormatterUnitMile, (5 << 8) + 4)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Foundation.NSLengthFormatter.isForPersonHeightUse)
        self.assertArgIsBOOL(Foundation.NSLengthFormatter.setForPersonHeightUse_, 0)

        self.assertResultIsBOOL(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_
        )
        self.assertArgIsOut(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_, 0
        )
        self.assertArgIsOut(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_, 2
        )
