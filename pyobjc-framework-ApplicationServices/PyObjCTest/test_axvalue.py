import HIServices
from PyObjCTools.TestSupport import TestCase


class TestAXVAlue(TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kAXValueTypeCGPoint, 1)
        self.assertEqual(HIServices.kAXValueTypeCGSize, 2)
        self.assertEqual(HIServices.kAXValueTypeCGRect, 3)
        self.assertEqual(HIServices.kAXValueTypeCFRange, 4)
        self.assertEqual(HIServices.kAXValueTypeAXError, 5)
        self.assertEqual(HIServices.kAXValueTypeIllegal, 0)

        self.assertEqual(HIServices.kAXValueCGPointType, HIServices.kAXValueTypeCGPoint)
        self.assertEqual(HIServices.kAXValueCGSizeType, HIServices.kAXValueTypeCGSize)
        self.assertEqual(HIServices.kAXValueCGRectType, HIServices.kAXValueTypeCGRect)
        self.assertEqual(HIServices.kAXValueCFRangeType, HIServices.kAXValueTypeCFRange)
        self.assertEqual(HIServices.kAXValueAXErrorType, HIServices.kAXValueTypeAXError)
        self.assertEqual(HIServices.kAXValueIllegalType, HIServices.kAXValueTypeIllegal)

    def test_types(self):
        self.assertIsCFType(HIServices.AXValueRef)

    def test_functions(self):
        v = HIServices.AXValueGetTypeID()
        self.assertIsInstance(v, int)

        HIServices.AXValueGetType

    def test_manual_functions(self):
        with self.subTest("CGPoint"):
            val = HIServices.AXValueCreate(HIServices.kAXValueTypeCGPoint, (1, 2))
            self.assertIsInstance(val, HIServices.AXValueRef)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCGPoint, None
            )
            self.assertIs(ok, True)
            self.assertEqual(res, (1, 2))

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCGSize, None
            )
            self.assertIs(ok, False)
            self.assertIs(res, None)

            with self.assertRaises(TypeError):
                HIServices.AXValueCreate(HIServices.kAXValueTypeCGPoint, 42)

        with self.subTest("CGSize"):
            val = HIServices.AXValueCreate(HIServices.kAXValueTypeCGSize, (1, 2))
            self.assertIsInstance(val, HIServices.AXValueRef)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCGSize, None
            )
            self.assertIs(ok, True)
            self.assertEqual(res, (1, 2))

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCFRange, None
            )
            self.assertIs(ok, False)
            self.assertIs(res, None)

            with self.assertRaises(TypeError):
                HIServices.AXValueCreate(HIServices.kAXValueTypeCGSize, 42)

        with self.subTest("CGRect"):
            val = HIServices.AXValueCreate(
                HIServices.kAXValueTypeCGRect, ((1, 2), (3, 4))
            )
            self.assertIsInstance(val, HIServices.AXValueRef)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCGRect, None
            )
            self.assertIs(ok, True)
            self.assertEqual(res, ((1, 2), (3, 4)))

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCFRange, None
            )
            self.assertIs(ok, False)
            self.assertIs(res, None)

            with self.assertRaises(TypeError):
                HIServices.AXValueCreate(HIServices.kAXValueTypeCGRect, 42)

        with self.subTest("CFRange"):
            val = HIServices.AXValueCreate(HIServices.kAXValueTypeCFRange, (1, 2))
            self.assertIsInstance(val, HIServices.AXValueRef)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCFRange, None
            )
            self.assertIs(ok, True)
            self.assertEqual(res, (1, 2))

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCGSize, None
            )
            self.assertIs(ok, False)
            self.assertIs(res, None)

            with self.assertRaises(TypeError):
                HIServices.AXValueCreate(HIServices.kAXValueTypeCFRange, 42)

        with self.subTest("AXError"):
            val = HIServices.AXValueCreate(
                HIServices.kAXValueTypeAXError, HIServices.kAXErrorNotEnoughPrecision
            )
            self.assertIsInstance(val, HIServices.AXValueRef)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeAXError, None
            )
            self.assertIs(ok, True)
            self.assertEqual(res, HIServices.kAXErrorNotEnoughPrecision)

            ok, res = HIServices.AXValueGetValue(
                val, HIServices.kAXValueTypeCFRange, None
            )
            self.assertIs(ok, False)
            self.assertIs(res, None)

            with self.assertRaises(ValueError):
                HIServices.AXValueCreate(HIServices.kAXValueTypeAXError, (1, 2))

        with self.assertRaises(ValueError):
            HIServices.AXValueCreate(55, (1, 2))

        with self.assertRaises(ValueError):
            HIServices.AXValueGetValue(val, 99, None)
