
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    import Quartz
except ImportError:
    Quartz = None

class TestCarbonUtils (TestCase):
    @onlyOn32Bit
    def testFunctions(self):
        if Quartz is None:
            self.fail("Quartz is not installed")

        WebInitForCarbon()

        img = NSImage.imageNamed_('NSHelpCursor')
        self.assertIsInstance(img, NSImage)

        ref = WebConvertNSImageToCGImageRef(img)
        if ref is not None:
            self.assertIsInstance(ref, Quartz.CGImageRef)

if __name__ == "__main__":
    main()
