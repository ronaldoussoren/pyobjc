from PyObjCTools.TestSupport import *

import AppKit

try:
    unicode
except NameError:
    unicode = str

class TestNSSharingService (TestCase):
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


if __name__ == "__main__":
    main()
