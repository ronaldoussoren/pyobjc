import Cocoa
from PyObjCTools.TestSupport import TestCase, onlyOn32Bit
import WebKit

try:
    import Quartz
except ImportError:
    Quartz = None


class TestCarbonUtils(TestCase):
    @onlyOn32Bit
    def testFunctions(self):
        if Quartz is None:
            self.fail("Quartz is not installed")

        WebKit.WebInitForCarbon()

        # img = NSImage.imageNamed_('NSHelpCursor')
        img = Cocoa.NSImage.imageNamed_(Cocoa.NSImageNameUserAccounts)
        self.assertIsInstance(img, Cocoa.NSImage)

        ref = Cocoa.WebConvertNSImageToCGImageRef(img)
        if ref is not None:
            self.assertIsInstance(ref, Quartz.CGImageRef)
