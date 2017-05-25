from PyObjCTools.TestSupport import *

import iTunesLibrary
import objc

class TestITLibMediaEntity (TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaEntity, objc.objc_class)

    def testMethods(self):
        self.assertArgIsBlock(iTunesLibrary.ITLibMediaEntity.enumerateValuesForProperties_usingBlock_, 1, b'v@@o^Z')
        self.assertArgIsBlock(iTunesLibrary.ITLibMediaEntity.enumerateValuesExceptForProperties_usingBlock_, 1, b'v@@o^Z')

    def testConstants(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaEntityPropertyPersistentID, unicode)



if __name__ == "__main__":
    main()
