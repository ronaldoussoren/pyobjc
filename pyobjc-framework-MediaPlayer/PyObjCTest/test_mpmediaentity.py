from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPMediaEntity(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(MediaPlayer.MPMediaEntity.canFilterByProperty_)

        self.assertArgIsBlock(
            MediaPlayer.MPMediaEntity.enumerateValuesForProperties_usingBlock_,
            1,
            b"v@@o^Z",
        )

    @min_os_level("10.12")
    def test_constants(self):
        self.assertIsInstance(MediaPlayer.MPMediaEntityPropertyPersistentID, str)
