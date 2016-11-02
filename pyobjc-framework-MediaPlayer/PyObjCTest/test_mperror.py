from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPError (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(MediaPlayer.MPErrorDomain, unicode)

if __name__ == "__main__":
    main()
