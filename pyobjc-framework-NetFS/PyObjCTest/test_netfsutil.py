from PyObjCTools.TestSupport import *
import NetFS


class TestNetFS (TestCase):

    def testFunctions(self):
        self.assertResultHasType(NetFS.NetFSCFStringtoCString, objc._C_PTR + objc._C_CHAR_AS_TEXT)
        self.assertResultIsNullTerminated(NetFS.NetFSCFStringtoCString)

if __name__ == "__main__":
    main()
