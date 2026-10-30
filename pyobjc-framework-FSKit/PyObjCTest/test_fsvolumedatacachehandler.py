from PyObjCTools.TestSupport import TestCase, min_sdk_level

import FSKit


class TestFSVolumeDataCacheHandlerHelper(FSKit.NSObject):
    # FSVolumeDataCacheHandler

    def isDataCacheInhibited(self):
        return 1

    def openItem_modes_cacheMode_context_replyHandler_(self, a, b, c, d, e):
        pass

    def closeItem_context_replyHandler_(self, a, b, c):
        pass

    def upgradeItem_cacheMode_context_replyHandler_(self, a, b, c, d):
        pass


class TestFSVolumeDataCacheHandler(TestCase):
    def test_enums(self):
        self.assertIsEnumType(FSKit.FSDataCacheMode)
        self.assertEqual(FSKit.FSDataCacheModeNone, 0)
        self.assertEqual(FSKit.FSDataCacheModeReadWithCache, 1)
        self.assertEqual(FSKit.FSDataCacheModeReadWriteWithCache, 2)

        self.assertIsEnumType(FSKit.FSKernelCacheCoherencyType)
        self.assertEqual(FSKit.FSKernelCacheCoherencyTypeNoCache, 0)
        self.assertEqual(FSKit.FSKernelCacheCoherencyTypeReadCache, 1)
        self.assertEqual(FSKit.FSKernelCacheCoherencyTypeWriteThrough, 2)
        self.assertEqual(FSKit.FSKernelCacheCoherencyTypeWriteBack, 3)

        self.assertIsEnumType(FSKit.FSKernelCacheCoherencyAction)
        self.assertEqual(FSKit.FSKernelCacheCoherencyActionPush, 0)
        self.assertEqual(FSKit.FSKernelCacheCoherencyActionPushInvalidate, 1)
        self.assertEqual(FSKit.FSKernelCacheCoherencyActionInvalidate, 2)
        self.assertEqual(FSKit.FSKernelCacheCoherencyActionUpdate, 3)
        self.assertEqual(FSKit.FSKernelCacheCoherencyActionRevoke, 4)

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("FSVolumeDataCacheHandler", FSKit)

    def test_protocol_methods(self):
        with self.subTest("FSVolumeDataCacheHandler"):
            self.assertResultIsBOOL(
                TestFSVolumeDataCacheHandlerHelper.isDataCacheInhibited
            )

            self.assertArgHasType(
                TestFSVolumeDataCacheHandlerHelper.openItem_modes_cacheMode_context_replyHandler_,
                1,
                b"Q",
            )
            self.assertArgHasType(
                TestFSVolumeDataCacheHandlerHelper.openItem_modes_cacheMode_context_replyHandler_,
                2,
                b"q",
            )
            self.assertArgIsBlock(
                TestFSVolumeDataCacheHandlerHelper.openItem_modes_cacheMode_context_replyHandler_,
                4,
                b"v@@",
            )

            self.assertArgIsBlock(
                TestFSVolumeDataCacheHandlerHelper.closeItem_context_replyHandler_,
                2,
                b"v",
            )

            self.assertArgHasType(
                TestFSVolumeDataCacheHandlerHelper.upgradeItem_cacheMode_context_replyHandler_,
                1,
                b"q",
            )
            self.assertArgIsBlock(
                TestFSVolumeDataCacheHandlerHelper.upgradeItem_cacheMode_context_replyHandler_,
                3,
                b"v@@",
            )
