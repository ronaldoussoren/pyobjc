
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Foundation import NSMutableData

class TestCGPDFContext (TestCase):
    def testFunctions(self):
        data = NSMutableData.data()
        self.failUnlessIsInstance(data, CFMutableDataRef)

        consumer = CGDataConsumerCreateWithCFData(data)
        self.failUnlessIsInstance(consumer, CGDataConsumerRef)

        self.failUnlessArgIsIn(CGPDFContextCreate, 1)
        self.failUnlessResultIsCFRetained(CGPDFContextCreate)
        context = CGPDFContextCreate(consumer, None, None)
        self.failUnlessIsInstance(context, CGContextRef)

        CGPDFContextClose(context)

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

        CGPDFContextClose(context)

    def testConstants(self):
        self.failUnlessIsInstance(kCGPDFContextMediaBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextCropBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextBleedBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextTrimBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextArtBox, unicode)
        self.failUnlessIsInstance(kCGPDFContextTitle, unicode)
        self.failUnlessIsInstance(kCGPDFContextAuthor, unicode)
        self.failUnlessIsInstance(kCGPDFContextSubject, unicode)
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
