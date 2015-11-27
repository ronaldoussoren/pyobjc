'''
Some simple tests to check that the framework is properly wrapped.
'''
from PyObjCTools.TestSupport import *
import objc
import CFOpenDirectory

class TestCFOpenDirectory (TestCase):
    def testClasses(self):
        self.assertIsCFType(CFOpenDirectory.ODContextRef)
        self.assertIsCFType(CFOpenDirectory.ODNodeRef)
        self.assertIsCFType(CFOpenDirectory.ODQueryRef)
        self.assertIsCFType(CFOpenDirectory.ODRecordRef)
        self.assertIsCFType(CFOpenDirectory.ODSessionRef)

    def testConstants(self):
        self.assertIsInstance(CFOpenDirectory.kODErrorDomainFramework, unicode)



if __name__ == "__main__":
    main()
