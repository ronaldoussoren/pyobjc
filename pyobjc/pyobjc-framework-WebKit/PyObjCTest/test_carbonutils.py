
from PyObjCTools.TestSupport import *
from WebKit import *
import Quartz

class TestCarbonUtils (TestCase):
    @onlyOn32Bit
    def testFunctions(self):
        WebInitForCarbon()

        img = NSImage.imageNamed_('NSAddTemplate')
        self.failUnlessIsInstance(img, NSImage)

        ref = WebConvertNSImageToCGImageRef(img)
        if ref is not None:
            self.failUnlessIsInstance(ref, Quartz.CGImageRef)

if __name__ == "__main__":
    main()
