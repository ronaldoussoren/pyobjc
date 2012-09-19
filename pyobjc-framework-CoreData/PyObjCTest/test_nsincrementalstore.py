import objc
from PyObjCTools.TestSupport import *
import CoreData

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestNSIncrementalStore (TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(CoreData.NSIncrementalStore.loadMetadata_)
        self.assertArgIsOut(CoreData.NSIncrementalStore.loadMetadata_, 0)
        self.assertArgIsOut(CoreData.NSIncrementalStore.executeRequest_withContext_error_, 2)
        self.assertArgIsOut(CoreData.NSIncrementalStore.newValuesForObjectWithID_withContext_error_, 2)
        self.assertArgIsOut(CoreData.NSIncrementalStore.newValueForRelationship_forObjectWithID_withContext_error_, 3)
        self.assertArgIsOut(CoreData.NSIncrementalStore.obtainPermanentIDsForObjects_error_, 1)

if __name__ == "__main__":
    main()
