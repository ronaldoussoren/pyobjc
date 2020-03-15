import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSEnumeratorInteraction(TestCase):
    def setUp(self):
        self.arrayContainer = Foundation.NSArray.arrayWithArray_(range(100))

    def testNoFastEnumeration(self):
        self.assertNotHasAttr(Foundation, "NSFastEnumerationState")

    def testInOperator(self):
        y = []
        for x in self.arrayContainer.objectEnumerator():
            y.append(x)

        self.assertEqual(len(y), len(self.arrayContainer))
        for i in range(len(y)):
            self.assertEqual(y[i], self.arrayContainer[i])
