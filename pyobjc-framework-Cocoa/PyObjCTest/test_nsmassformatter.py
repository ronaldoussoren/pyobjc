import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMassFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSMassFormatterUnit)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSMassFormatterUnitGram, 11)
        self.assertEqual(Foundation.NSMassFormatterUnitKilogram, 14)
        self.assertEqual(Foundation.NSMassFormatterUnitOunce, (6 << 8) + 1)
        self.assertEqual(Foundation.NSMassFormatterUnitPound, (6 << 8) + 2)
        self.assertEqual(Foundation.NSMassFormatterUnitStone, (6 << 8) + 3)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(Foundation.NSMassFormatter.isForPersonMassUse)
        self.assertArgIsBOOL(Foundation.NSMassFormatter.setForPersonMassUse_, 0)

        self.assertResultIsBOOL(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_
        )
        self.assertArgIsOut(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_, 0
        )
        self.assertArgIsOut(
            Foundation.NSLengthFormatter.getObjectValue_forString_errorDescription_, 2
        )
