import HIServices
import sys
from PyObjCTools.TestSupport import *

class TestHIShape (TestCase):
    def testTypes(self):
        self.assertIsCFType(HIServices.HIShapeRef)

    def testFunctions(self):
        self.assertIsInstance(HIServices.HIShapeGetTypeID(), (int, long))

        self.assertResultIsCFRetained(HIServices.HIShapeCreateEmpty)

        self.assertResultIsCFRetained(HIServices.HIShapeCreateWithRect)
        self.assertArgIsIn(HIServices.HIShapeCreateWithRect, 0)

        self.assertResultIsCFRetained(HIServices.HIShapeCreateCopy)
        self.assertResultIsCFRetained(HIServices.HIShapeCreateIntersection)
        self.assertResultIsCFRetained(HIServices.HIShapeCreateDifference)
        self.assertResultIsCFRetained(HIServices.HIShapeCreateUnion)
        self.assertResultIsCFRetained(HIServices.HIShapeCreateXor)

        self.assertResultIsBOOL(HIServices.HIShapeIsEmpty)
        self.assertResultIsBOOL(HIServices.HIShapeIsRectangular)

        self.assertResultIsBOOL(HIServices.HIShapeContainsPoint)
        self.assertArgIsIn(HIServices.HIShapeContainsPoint, 1)

        self.assertResultIsBOOL(HIServices.HIShapeIntersectsRect)
        self.assertArgIsIn(HIServices.HIShapeIntersectsRect, 1)

        self.assertResultIsFixedSize(HIServices.HIShapeIntersectsRect, 1)
        self.assertArgIsOut(HIServices.HIShapeGetBounds, 1)

        HIServices.HIShapeReplacePathInCGContext

        if sys.maxsize < 2 ** 32:
            HIShapeEnumerateProcPtr = b'ii^{__HIShape=}n^{CGRect={CGPoint=ff}{CGSize=ff}}^v'
        else:
            HIShapeEnumerateProcPtr = b'ii^{__HIShape=}n^{CGRect={CGPoint=dd}{CGSize=dd}}^v'

        self.assertArgIsFunction(HIServices.HIShapeEnumerate, 2, HIShapeEnumerateProcPtr, False)

        self.assertResultIsCFRetained(HIServices.HIShapeCreateMutable)
        self.assertResultIsCFRetained(HIServices.HIShapeCreateMutableCopy)

        self.assertResultIsCFRetained(HIServices.HIShapeCreateMutableWithRect)
        self.assertArgIsIn(HIServices.HIShapeCreateMutableWithRect, 0)

        HIServices.HIShapeSetEmpty
        HIServices.HIShapeSetWithShape
        HIServices.HIShapeIntersect
        HIServices.HIShapeDifference
        HIServices.HIShapeUnion
        HIServices.HIShapeXor
        HIServices.HIShapeOffset
        HIServices.HIShapeInset

        self.assertArgIsIn(HIServices.HIShapeUnionWithRect, 1)


    def testConstants(self):
        self.assertEqual(HIServices.kHIShapeEnumerateInit, 1)
        self.assertEqual(HIServices.kHIShapeEnumerateRect, 2)
        self.assertEqual(HIServices.kHIShapeEnumerateTerminate, 3)


        self.assertEqual(HIServices.kHIShapeParseFromTop, 0)
        self.assertEqual(HIServices.kHIShapeParseFromBottom, 1 << 0)
        self.assertEqual(HIServices.kHIShapeParseFromLeft, 0)
        self.assertEqual(HIServices.kHIShapeParseFromRight, 1 << 1)
        self.assertEqual(HIServices.kHIShapeParseFromTopLeft,
            HIServices.kHIShapeParseFromTop | HIServices.kHIShapeParseFromLeft)
        self.assertEqual(HIServices.kHIShapeParseFromBottomRight,
            HIServices.kHIShapeParseFromBottom | HIServices.kHIShapeParseFromRight)





if __name__ == "__main__":
    main()
