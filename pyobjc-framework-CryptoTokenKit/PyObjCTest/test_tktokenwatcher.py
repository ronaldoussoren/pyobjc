import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CryptoTokenKit

    class TestTKTokenWatcher (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertArgIsBlock(CryptoTokenKit.TKTokenWatcher.initWithInsertionHandler_, 0, b'v@')
            self.assertArgIsBlock(CryptoTokenKit.TKTokenWatcher.addRemovalHandler_forTokenID_, 0, b'v@')

        @min_os_level('10.13')
        def testConstants(self):
            self.assertArgIsBlock(CryptoTokenKit.TKTokenWatcher.setInsertionHandler_, 0, b'v@')

if __name__ == "__main__":
    main()
