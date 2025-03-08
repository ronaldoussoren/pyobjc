from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit
import objc


class TestWKWebExtensionTabHelper(WebKit.NSObject):
    def setParentTab_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def isPinnedForWebExtensionContext_(self, a):
        return 1

    def setPinned_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def isReaderModeAvailableForWebExtensionContext_(self, a):
        return 1

    def isReaderModeActiveForWebExtensionContext_(self, a):
        return 1

    def setReaderModeActive_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def isPlayingAudioForWebExtensionContext_(self, a):
        return 1

    def isMutedForWebExtensionContext_(self, a):
        return 1

    def setMuted_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def sizeForWebExtensionContext_(self, a):
        return 1

    def zoomFactorForWebExtensionContext_(self, a):
        return 1

    def setZoomFactor_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def isLoadingCompleteForWebExtensionContext_(self, a):
        return 1

    def detectWebpageLocaleForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def takeSnapshotUsingConfiguration_forWebExtensionContext_completionHandler_(
        self, a, b, c
    ):
        pass

    def loadURL_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def reloadFromOrigin_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def goBackForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def goForwardForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def activateForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def isSelectedForWebExtensionContext_(self, a):
        return 1

    def setSelected_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def duplicateUsingConfiguration_forWebExtensionContext_completionHandler_(
        self, a, b, c
    ):
        pass

    def closeForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def shouldGrantPermissionsOnUserGestureForWebExtensionContext_(self, a):
        return 1

    def shouldBypassPermissionsForWebExtensionContext_(self, a):
        return 1


class TestWKWebExtensionTab(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionTabChangedProperties)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesNone, 0)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesLoading, 1 << 1)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesMuted, 1 << 2)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesPinned, 1 << 3)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesPlayingAudio, 1 << 4)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesReaderMode, 1 << 5)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesSize, 1 << 6)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesTitle, 1 << 7)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesURL, 1 << 8)
        self.assertEqual(WebKit.WKWebExtensionTabChangedPropertiesZoomFactor, 1 << 9)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionDataRecordErrorDomain, str)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setParentTab_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isPinnedForWebExtensionContext_
        )

        self.assertArgIsBOOL(
            TestWKWebExtensionTabHelper.setPinned_forWebExtensionContext_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setPinned_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isReaderModeAvailableForWebExtensionContext_
        )
        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isReaderModeActiveForWebExtensionContext_
        )

        self.assertArgIsBOOL(
            TestWKWebExtensionTabHelper.setReaderModeActive_forWebExtensionContext_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setReaderModeActive_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isPlayingAudioForWebExtensionContext_
        )
        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isMutedForWebExtensionContext_
        )

        self.assertArgIsBOOL(
            TestWKWebExtensionTabHelper.setMuted_forWebExtensionContext_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setMuted_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultHasType(
            TestWKWebExtensionTabHelper.sizeForWebExtensionContext_,
            WebKit.CGSize.__typestr__,
        )
        self.assertResultHasType(
            TestWKWebExtensionTabHelper.zoomFactorForWebExtensionContext_, objc._C_DBL
        )

        self.assertArgHasType(
            TestWKWebExtensionTabHelper.setZoomFactor_forWebExtensionContext_completionHandler_,
            0,
            objc._C_DBL,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setZoomFactor_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isLoadingCompleteForWebExtensionContext_
        )

        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.detectWebpageLocaleForWebExtensionContext_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.takeSnapshotUsingConfiguration_forWebExtensionContext_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.loadURL_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBOOL(
            TestWKWebExtensionTabHelper.reloadFromOrigin_forWebExtensionContext_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.reloadFromOrigin_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.goBackForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.goForwardForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.activateForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )
        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.isSelectedForWebExtensionContext_
        )

        self.assertArgIsBOOL(
            TestWKWebExtensionTabHelper.setSelected_forWebExtensionContext_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.setSelected_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.duplicateUsingConfiguration_forWebExtensionContext_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionTabHelper.closeForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )

        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.shouldGrantPermissionsOnUserGestureForWebExtensionContext_
        )
        self.assertResultIsBOOL(
            TestWKWebExtensionTabHelper.shouldBypassPermissionsForWebExtensionContext_
        )
