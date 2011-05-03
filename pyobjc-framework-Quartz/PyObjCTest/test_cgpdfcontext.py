
from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
from Foundation import NSMutableData

class TestCGPDFContext (TestCase):
    @min_os_level('10.5')
    def testFunctions10_5(self):
        # Note actual test is in the function below this one.
        CGPDFContextClose

    def testFunctions(self):
        data = NSMutableData.data()
        self.assertIsInstance(data, CFMutableDataRef)

        consumer = CGDataConsumerCreateWithCFData(data)
        self.assertIsInstance(consumer, CGDataConsumerRef)

        self.assertArgIsIn(CGPDFContextCreate, 1)
        self.assertResultIsCFRetained(CGPDFContextCreate)
        context = CGPDFContextCreate(consumer, None, None)
        self.assertIsInstance(context, CGContextRef)

        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)

        self.assertResultIsCFRetained(CGPDFContextCreateWithURL)
        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertArgIsIn(CGPDFContextCreateWithURL, 1)
        context = CGPDFContextCreateWithURL(url, None, None)
        self.assertIsInstance(context, CGContextRef)

        CGPDFContextBeginPage(context, None)

        CGPDFContextSetURLForRect(context, url, ((0, 0), (10, 10)))
        CGPDFContextAddDestinationAtPoint(context, "target", (50, 50))

        CGPDFContextSetDestinationForRect(context, "target", ((100, 120), (50, 60)))

        CGPDFContextEndPage(context)

        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCGPDFContextSubject, unicode)

    def testConstants(self):
        self.assertIsInstance(kCGPDFContextMediaBox, unicode)
        self.assertIsInstance(kCGPDFContextCropBox, unicode)
        self.assertIsInstance(kCGPDFContextBleedBox, unicode)
        self.assertIsInstance(kCGPDFContextTrimBox, unicode)
        self.assertIsInstance(kCGPDFContextArtBox, unicode)
        self.assertIsInstance(kCGPDFContextTitle, unicode)
        self.assertIsInstance(kCGPDFContextAuthor, unicode)
        self.assertIsInstance(kCGPDFContextKeywords, unicode)
        self.assertIsInstance(kCGPDFContextCreator, unicode)
        self.assertIsInstance(kCGPDFContextOwnerPassword, unicode)
        self.assertIsInstance(kCGPDFContextUserPassword, unicode)
        self.assertIsInstance(kCGPDFContextEncryptionKeyLength, unicode)
        self.assertIsInstance(kCGPDFContextAllowsPrinting, unicode)
        self.assertIsInstance(kCGPDFContextAllowsCopying, unicode)
        self.assertIsInstance(kCGPDFContextOutputIntent, unicode)
        self.assertIsInstance(kCGPDFXOutputIntentSubtype, unicode)
        self.assertIsInstance(kCGPDFXOutputConditionIdentifier, unicode)
        self.assertIsInstance(kCGPDFXOutputCondition, unicode)
        self.assertIsInstance(kCGPDFXRegistryName, unicode)
        self.assertIsInstance(kCGPDFXInfo, unicode)
        self.assertIsInstance(kCGPDFXDestinationOutputProfile, unicode)
        self.assertIsInstance(kCGPDFContextOutputIntents, unicode)





if __name__ == "__main__":
    main()
