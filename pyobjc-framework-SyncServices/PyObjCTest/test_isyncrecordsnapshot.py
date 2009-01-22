
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncRecordSnapshot (TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessArgHasType(ISyncRecordSnapshot.recordIdentifierForReference_isModified_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)

if __name__ == "__main__":
    main()
