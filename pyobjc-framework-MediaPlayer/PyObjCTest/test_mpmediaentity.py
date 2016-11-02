from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPMediaEntity (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPMediaEntity.canFilterByProperty_)

            self.assertArgIsBlock(MediaPlayer.MPMediaEntity.enumerateValuesForProperties_usingBlock_, 1, b'v@@o^Z')

        @min_os_level('10.12')
        def testConstants(self):
            self.assertIsInstance(MediaPlayer.MPMediaEntityPropertyPersistentID, unicode)

if __name__ == "__main__":
    main()
