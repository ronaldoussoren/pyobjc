from PyObjCTools.TestSupport import *

import AppKit

class TestNSSharingServiceHelper (AppKit.NSObject):
    def showRelativeToRect_ofView_preferredEdge_(self, r, v, e): pass

class TestNSSharingService (TestCase):
    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSSharingServiceNameCloudSharing, unicode)

        self.assertEqual(AppKit.NSCloudKitSharingServiceStandard, 0)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowPublic, 1 << 0)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowPrivate, 1 << 1)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowReadOnly, 1 << 4)
        self.assertEqual(AppKit.NSCloudKitSharingServiceAllowReadWrite, 1 << 5)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnTencentWeibo, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnLinkedIn, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsFacebookProfileImage, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsLinkedInProfileImage, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnFacebook, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnTwitter, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostOnSinaWeibo, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameComposeEmail, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameComposeMessage, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameSendViaAirDrop, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToSafariReadingList, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToIPhoto, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameAddToAperture, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsTwitterProfileImage, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNameUseAsDesktopPicture, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostImageOnFlickr, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnVimeo, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnYouku, unicode)
        self.assertIsInstance(AppKit.NSSharingServiceNamePostVideoOnTudou, unicode)

        self.assertEqual(AppKit.NSSharingContentScopeItem, 0)
        self.assertEqual(AppKit.NSSharingContentScopePartial, 1)
        self.assertEqual(AppKit.NSSharingContentScopeFull, 2)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBlock(AppKit.NSSharingService.initWithTitle_image_alternateImage_handler_, 3, b'v')
        self.assertResultIsBOOL(AppKit.NSSharingService.canPerformWithItems_)

    @min_sdk_level('10.7')
    def testProtocolObjects(self):
        objc.protocolNamed('NSSharingServiceDelegate')
        objc.protocolNamed('NSSharingServicePickerDelegate')

    def testProtocol(self):
        self.assertArgHasType(TestNSSharingServiceHelper.showRelativeToRect_ofView_preferredEdge_, 0, AppKit.NSRect.__typestr__)
        self.assertArgHasType(TestNSSharingServiceHelper.showRelativeToRect_ofView_preferredEdge_, 2, objc._C_NSUInteger)

    @min_sdk_level('10.12')
    def testProtocolObjects(self):
        objc.protocolNamed('NSCloudSharingServiceDelegate')



if __name__ == "__main__":
    main()
