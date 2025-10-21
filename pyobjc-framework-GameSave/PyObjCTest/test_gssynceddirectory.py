from PyObjCTools.TestSupport import TestCase

import GameSave


class TestGSSyncedDirectory(TestCase):
    def test_enum(self):
        self.assertIsEnumType(GameSave.GSSyncState)
        self.assertEqual(GameSave.GSSyncStateReady, 0)
        self.assertEqual(GameSave.GSSyncStateOffline, 1)
        self.assertEqual(GameSave.GSSyncStateLocal, 2)
        self.assertEqual(GameSave.GSSyncStateSyncing, 3)
        self.assertEqual(GameSave.GSSyncStateConflicted, 4)
        self.assertEqual(GameSave.GSSyncStateError, 5)
        self.assertEqual(GameSave.GSSyncStateClosed, 6)

    def test_methods(self):
        self.assertResultIsBOOL(GameSave.GSSyncedDirectoryVersion.isLocal)

        self.assertArgIsBlock(
            GameSave.GSSyncedDirectory.triggerPendingUploadWithCompletionHandler_,
            0,
            b"vZ",
        )
        self.assertArgIsBlock(
            GameSave.GSSyncedDirectory.finishSyncingWithCompletionHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            GameSave.GSSyncedDirectory.finishSyncing_completionHandler_, 1, b"v"
        )
