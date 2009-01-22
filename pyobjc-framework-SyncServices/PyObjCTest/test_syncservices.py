'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import SyncServices

class TestSyncServices (TestCase):
    def testClasses(self):
        self.assert_( hasattr(SyncServices, 'ISyncClient') )
        self.assert_( isinstance(SyncServices.ISyncClient, objc.objc_class) )


if __name__ == "__main__":
    main()

