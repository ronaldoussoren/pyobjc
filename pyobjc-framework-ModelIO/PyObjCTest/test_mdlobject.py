from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import ModelIO

    class TestMDLObject (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(ModelIO.MDLObject.hidden)
            self.assertArgIsBOOL(ModelIO.MDLObject.setHidden_, 0)

if __name__ == "__main__":
    main()
