
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
        self.failUnlessIsInstance(data, CFMutableDataRef)

        consumer = CGDataConsumerCreateWithCFData(data)
        self.failUnlessIsInstance(consumer, CGDataConsumerRef)

        self.failUnlessArgIsIn(CGPDFContextCreate, 1)
        self.failUnlessResultIsCFRetained(CGPDFContextCreate)
        context = CGPDFContextCreate(consumer, None, None)
        self.failUnlessIsInstance(context, CGContextRef)

        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)

        self.failUnlessResultIsCFRetained(CGPDFContextCreateWithURL)
        url = CFURLCreateWithFileSystemPath(None,
            "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessArgIsIn(CGPDFContextCreateWithURL, 1)
        context = CGPDFContextCreateWithURL(url, None, None)
        self.failUnlessIsInstance(context, CGContextRef)

        CGPDFContextBeginPage(context, None)

        CGPDFContextSetURLForRect(context, url, ((0, 0), (10, 10)))
        CGPDFContextAddDestinationAtPoint(context, "target", (50, 50))

        CGPDFContextSetDestinationForRect(context, "target", ((100, 120), (50, 60)))

        CGPDFContextEndPage(context)

        if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCGPDFContextSubject, unicode)

    def testConstants(self):
        self.failUnlessIsInstance(kCGPDFContextMediaBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextCropBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextBleedBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextTrimBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextArtBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextTitle, unicode)
        self.failUnlessIsInstance(kCGPDFContextAuthor, unicode)
        self.failUnlessIsInstance(kCGPDFContextKeywords, unicode)
        self.failUnlessIsInstance(kCGPDFContextCreator, unicode)
        self.failUnlessIsInstance(kCGPDFContextOwnerPassword, unicode)
        self.failUnlessIsInstance(kCGPDFContextUserPassword, unicode)
        self.failUnlessIsInstance(kCGPDFContextEncryptionKeyLength, unicode)
        self.failUnlessIsInstance(kCGPDFContextAllowsPrinting, unicode)
        self.failUnlessIsInstance(kCGPDFContextAllowsCopying, unicode)
        self.failUnlessIsInstance(kCGPDFContextOutputIntent, unicode)
        self.failUnlessIsInstance(kCGPDFXOutputIntentSubtype, unicode)
        self.failUnlessIsInstance(kCGPDFXOutputConditionIdentifier, unicode)
        self.failUnlessIsInstance(kCGPDFXOutputCondition, unicode)
        self.failUnlessIsInstance(kCGPDFXRegistryName, unicode)
        self.failUnlessIsInstance(kCGPDFXInfo, unicode)
        self.failUnlessIsInstance(kCGPDFXDestinationOutputProfile, unicode)
        self.failUnlessIsInstance(kCGPDFContextOutputIntents, unicode)





if __name__ == "__main__":
    main()
