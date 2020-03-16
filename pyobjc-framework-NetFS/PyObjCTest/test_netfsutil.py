import NetFS
import objc
from PyObjCTools.TestSupport import TestCase


class TestNetFS(TestCase):
    def testFunctions(self):
        self.assertResultHasType(
            NetFS.NetFSCFStringtoCString, objc._C_PTR + objc._C_CHAR_AS_TEXT
        )
        self.assertResultIsNullTerminated(NetFS.NetFSCFStringtoCString)
