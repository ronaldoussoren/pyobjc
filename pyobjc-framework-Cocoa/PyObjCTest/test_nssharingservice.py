import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSharingServiceHelper(AppKit.NSObject):
    def showRelativeToRect_ofView_preferredEdge_(self, r, v, e):
        pass


class TestNSSharingService(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSSharingServiceName, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSCloudKitSharingServiceOptions)
        self.assertIsEnumType(AppKit.NSSharingContentScope)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSSharingServiceNameCloudSharing, str)

        self.assertEqual(AppKit.NSCloudKitSharingServiceStandard, 0)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowPublic, 1 << 0)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowPrivate, 1 << 1)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowReadOnly, 1 << 4)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowReadWrite, 1 << 5)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnTencentWeibo, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnLinkedIn, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsFacebookProfileImage, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsLinkedInProfileImage, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnFacebook, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnTwitter, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnSinaWeibo, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameComposeEmail, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameComposeMessage, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameSendViaAirDrop, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToSafariReadingList, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToIPhoto, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToAperture, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsTwitterProfileImage, str)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsDesktopPicture, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostImageOnFlickr, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnVimeo, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnYouku, str)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnTudou, str)

        self.assertEqual(AppKit.NSSharingContentScopeItem, 0)
        self.assertEqual(AppKit.NSSharingContentScopePartial, 1)
        self.assertEqual(AppKit.NSSharingContentScopeFull, 2)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            AppKit.NSSharingService.initWithTitle_image_alternateImage_handler_, 3, b"v"
        )
        self.assertResultIsBOOL(AppKit.NSSharingService.canPerformWithItems_)

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSSharingServiceDelegate")
        self.assertProtocolExists("NSSharingServicePickerDelegate")

    def testProtocol(self):
        self.assertArgHasType(
            TestNSSharingServiceHelper.showRelativeToRect_ofView_preferredEdge_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSharingServiceHelper.showRelativeToRect_ofView_preferredEdge_,
            2,
            objc._C_NSUInteger,
        )

    @min_sdk_level("10.12")
    def testProtocolObjects10_12(self):
        self.assertProtocolExists("NSCloudSharingServiceDelegate")
