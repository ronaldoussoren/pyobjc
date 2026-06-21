import iTunesLibrary
import objc
from PyObjCTools.TestSupport import TestCase


class TestITLibMediaEntity(TestCase):
    def test_classes(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaEntity, objc.objc_class)

    def test_methods(self):
        self.assertArgIsBlock(
            iTunesLibrary.ITLibMediaEntity.enumerateValuesForProperties_usingBlock_,
            1,
            b"v@@o^Z",
        )
        self.assertArgIsBlock(
            iTunesLibrary.ITLibMediaEntity.enumerateValuesExceptForProperties_usingBlock_,
            1,
            b"v@@o^Z",
        )

    def test_constants(self):
        self.assertIsInstance(iTunesLibrary.ITLibMediaEntityPropertyPersistentID, str)
