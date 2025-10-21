from PyObjCTools.TestSupport import TestCase

import GameSave


class TestGameSave(TestCase):
    def test_callable_metadata_sane(self):
        self.assertCallableMetadataIsSane(GameSave)

    def test_constants(self):
        self.assertIsInstance(GameSave.GameSaveVersionNumber, float)
        self.assertNotHasAttr(GameSave, "GameSaveVersionString")
